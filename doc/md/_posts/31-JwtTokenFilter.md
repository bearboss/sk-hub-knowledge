title: JwtTokenFilter

date: 2021-06-03 15:20:36

tags: Jwt

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/31.jpg)

</span>

<!--more-->

# JwtTokenFilter

    ```
    import com.alibaba.fastjson.JSON;
    import com.alibaba.fastjson.JSONObject;
    import com.organic.common.util.JwtUtils;
    import com.organic.common.util.RedisUtil;
    import com.organic.common.util.ResultUtil;
    import com.organic.common.util.SpringUtil;
    import lombok.extern.slf4j.Slf4j;
    import org.springframework.data.redis.RedisConnectionFailureException;
    import org.springframework.util.StringUtils;
    import org.springframework.web.servlet.HandlerInterceptor;
    import org.springframework.web.servlet.ModelAndView;
    
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    import java.nio.charset.StandardCharsets;
    
    /**
     * @author MEIXIONG058
     * @date 2019-6-24
     * <p></p>
     */
    @Slf4j
    public class JwtTokenFilter implements HandlerInterceptor {
        private final String[] ss = new String[]{"/image/qr", "/export","/error","/not"};
    
        public boolean run(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
            for (String s : ss) {
                if (request.getRequestURI().contains(s)) {
                    return true;
                }
            }
            String authToken = request.getHeader("AuthToken");
            if (StringUtils.isEmpty(authToken)) {
                authToken = request.getParameter("AuthToken");
                if (StringUtils.isEmpty(authToken)) {
                    return context(response, "AuthToken is NULL ", 403);
                }
            }
            //通过新key去解密数据层
            String userId;
            try {
                userId = JwtUtils.verifyTokenGetUserId(authToken);
            } catch (Exception e) {
                log.error(e.getMessage(), e);
                return context(response, e.getMessage(), 403);
            }
            try {
                RedisUtil redisUtil = (RedisUtil) SpringUtil.getBean("redisUtil");
                String token = (String) redisUtil.get("user:" + userId);
                if (token == null) {
                    return context(response, "TOKEN已经过期", 403);
                }
                if (!token.equals(authToken)) {
                    return context(response, "TOKEN未匹配", 403);
                }
                //多加10分钟过期时间 - 删除用户需要重新清空redis
                redisUtil.set("user:" + userId, authToken, 3600L);
            } catch (RedisConnectionFailureException e) {
                return context(response, "redis连接失败", 403);
            }
            return true;
        }
    
        private boolean context(HttpServletResponse response, String resultInfo, int statusCode) throws Exception {
            response.setCharacterEncoding(StandardCharsets.UTF_8.toString());
            response.setContentType("application/json;charset=UTF-8");
            response.setStatus(200);
            response.getWriter().print(JSON.toJSONString(ResultUtil.error(statusCode, resultInfo)));
            return false;
        }
    
        @Override
        public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
            return run(request, response, handler);
        }
    
        @Override
        public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
    
        }
    
        @Override
        public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
    
        }
    }
    ```

# JwtUtils 

    ```
    import com.auth0.jwt.JWT;
    import com.auth0.jwt.JWTCreator;
    import com.auth0.jwt.JWTVerifier;
    import com.auth0.jwt.algorithms.Algorithm;
    import com.auth0.jwt.interfaces.Claim;
    import com.auth0.jwt.interfaces.DecodedJWT;
    
    import java.util.Date;
    import java.util.HashMap;
    import java.util.Map;
    
    public class JwtUtils {
    
        private final static String SECRET = "sds3434ads@#@$@$fd33gf545gfg";
    
        public static String createToken(Map<String, String> params) {
            return createToken(params, SECRET);
        }
    
        /**
         * JWT 生成Token
         *
         * @param params 参数map
         * @param secret 加密secret
         * @return
         * @throws Exception
         */
        public static String createToken(Map<String, String> params, String secret) {
            Date iatDate = new Date();
            // header Map
            Map<String, Object> map = new HashMap<>();
            map.put("alg", "HS256");
            map.put("typ", "JWT");
            JWTCreator.Builder builder = JWT.create().withHeader(map);
            for (String key : params.keySet()) {
                builder = builder.withClaim(key, params.get(key));
            }
            String token = builder.withIssuedAt(iatDate).sign(Algorithm.HMAC256(secret));
            return token;
        }
    
        public static Map<String, Claim> verifyToken(String token) {
            return verifyToken(token, SECRET);
        }
    
        /**
         * 解密token
         *
         * @param token
         * @param secret
         * @return
         */
        public static Map<String, Claim> verifyToken(String token, String secret) {
            DecodedJWT jwt = null;
            JWTVerifier verifier = JWT.require(Algorithm.HMAC256(secret)).build();
            jwt = verifier.verify(token);
            return jwt.getClaims();
        }
    
    
        public static String verifyTokenGetUserId(String token) {
            return verifyTokenGetUserId(token, SECRET);
        }
    
        /**
         * 解密token
         *
         * @param token
         * @param secret
         * @return
         */
        public static String verifyTokenGetUserId(String token, String secret) {
            DecodedJWT jwt = null;
            JWTVerifier verifier = JWT.require(Algorithm.HMAC256(secret)).build();
            jwt = verifier.verify(token);
            Map<String, Claim> map = jwt.getClaims();
            Claim claim = map.get("userId");
            return claim.asString();
        }
    }
    ```