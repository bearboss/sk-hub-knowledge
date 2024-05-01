title: Shiro相关

date: 2021-05-28 15:20:36

tags: Shiro

categories: Shiro

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/15.jpg)

</span>

<!--more-->

# 概述

- Shiro是一款权限校验框架，可自定义配置角色权限

# 初体验

-   SimpleAccountRealm  普通数组形式
-   IniRealm            文件配置形式
-   JdbcRealm           数据库配置
-   自定义 extends AuthorizingRealm 
    
```
public void testActhentication(){
    //创建SecurityManager shiro环境
    DefaultSecurityManager defaultSecurityManager = new DefaultSecurityManager();
    defaultSecurityManager.setRealm(simpleAccountRealm); #上方的四个Realm
    //主体认证请求
    SecurityUtils.setSecurityManager(defaultSecurityManager);
    Subject subject = SecurityUtils.getSubject();
    UsernamePasswordToken token = new UsernamePasswordToken("mask","123456");
    subject.login(token);
    System.out.println("isfalse:"+subject.isAuthenticated());
    subject.checkRole("admin");
    //subject.logout();
    //System.out.println("isfalse:"+subject.isAuthenticated());
}
```

# 整合spring

## web.xml

     <filter>
        <filter-name>shiroFilter</filter-name>
        <filter-class>org.springframework.web.filter.DelegatingFilterProxy</filter-class>
    </filter>
    
    <filter-mapping>
        <filter-name>shiroFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>

## spring.xml
    <!--定义ShiroFilterFactoryBean--> 
    <bean id="shiroFilter" class="org.apache.shiro.spring.web.ShiroFilterFactoryBean">
        <property name="securityManager" ref="securityManager"></property>
        <property name="loginUrl" value="login.html"></property>
        <property name="unauthorizedUrl" value="403.html"></property>
        <property name="filterChainDefinitions">
            <value>
                /login.html = anon
                /test = anon
                /test.do = anon
                /testRoles = roles["admin","admin1"]
                /testRoles1 = rolesOr["admin","admin1"]
                /subLogin = anon
                /* = authc
            </value>
        </property>
        <property name="filters">
            <map>
                <entry key="rolesOr" value-ref="rolesOrFilter" />
            </map>
        </property>
    </bean>
    <!--定义securityManager-->
    <bean id="securityManager" class="org.apache.shiro.web.mgt.DefaultWebSecurityManager">
        <property name="realm" ref="realm"></property>
    </bean>
    <!--自定义realm-->
    <bean id="realm" class="natapp.liujinliang.realm.CustomRealm">
        <property name="credentialsMatcher" ref="credentialsMatcher" ></property>
    </bean>
    <!--设置加密-->
    <bean id="credentialsMatcher" class="org.apache.shiro.authc.credential.HashedCredentialsMatcher">
        <property name="hashAlgorithmName" value="md5" />
        <property name="hashIterations" value="1" />
    </bean>
    
    <!-- 自定义filter  继承extends AuthorizationFilter -->
    <bean id="rolesOrFilter" class="natapp.liujinliang.filter.RolesOrFilter" />

## RolesOrFilter类

    public class RolesOrFilter extends AuthorizationFilter {
        @Override
        protected boolean isAccessAllowed(ServletRequest req,ServletResponse resp, Object object) throws Exception {
            Subject subject = getSubject(req, resp);
            String[] roles = (String[]) object;
            if (roles == null || roles.length == 0) {
                return true;
            }
            for (String role : roles) {
                if (subject.hasRole(role)) {
                    return true;
                }
            }
            return false;
        }
    }
    
## 判断登录

    public String subLogin(User user) {
        Subject subject = SecurityUtils.getSubject();
        UsernamePasswordToken token = new UsernamePasswordToken(user.getUsername(), user.getPassword());
        try {
            subject.login(token);
        } catch (Exception e) {
            return e.getMessage();
        }	
        // 编码方式判断是否具有管理员身份
        if (subject.hasRole("admin")) {
            return "有admin权限";
        }
        return "无admin权限";
	}
	
## 使用注解

    @RequiresPermissions("xxxx")#要求权限
    @RequiresRoles("admin")；#要求admin的角色

### 引入依赖

			<dependency>
			    <groupId>org.aspectj</groupId>
			    <artifactId>aspectjweaver</artifactId>
			    <version>1.8.9</version>
			</dependency>

### spring-mvc.xml

    <!-- 开启AoP -->
    <aop:config proxy-target-class="true"/>
    <!-- 保证 Shiro内部生命周期 -->
    <bean class="org.apache.shiro.spring.LifecycleBeanPostProcessor"></bean>
    <!-- 开启Shiro授权生效 -->
    <bean id="" class="org.apache.shiro.spring.security.interceptor.AuthorizationAttributeSourceAdvisor"></bean>	


## shiro-过滤器

		anno （不需要认证）, authBasic,authc（需要认证）, user（存在用户）,logout
		perms（具备权限）,roles（具备角色）,ssl,port

## redis实现session共享

> 序列化和反序列化

    SerializationUtils.serialize();//序列化
    SerializationUtils.deserialize();//反序列化
			
> 集合工具类

    CollectionUtils.isEmpty();	
			
> 创建类 重写 extend AbstractSessionDao	(com.imooc.session.SessionDao)

    #doCreate的时候记得要捆绑sessionId
        assignSessionId(sessionId,session);
    #spring.xml
        <bean class="org.apache.shiro.session.mgt.DefaultWebSessionManager" id="sessionManager">
            <property name="sessionDao" ref="sessionDao">
        </bean>
        <bean class="com.imooc.session.SessionDao" id="sessionDao"/>
    
        <bean id="securityManager" class="org.apache.shiro.web.mgt.DefaultWebSecurityManager">
            <property name="realm" ref="realm"/>
            <property name="sessionManager" ref="sessionManager"/>
        </bean>	
        
### 换成自定义sessionManager 

> spring.xml

    <bean class="com.imooc.session.CustomSessionManager" id="sessionManager">
        <property name="sessionDao" ref="sessionDao">
    </bean>
    
### 访问多次redis改造

> 继承DefaultWebSessionManager|重写retrieveSession|存在request中
				
        ServlertRequest request =null;
        if(sessionKey instanceof WebSessionKey){
            request = ((WebsessionKKey)sessionKey).getServletRequest(); 	
        }
						
## shiro缓存管理

> 角色什么的存在redis

    CacheManager Cache
    //返回cache实例
    class RedisCacheManager implements CacheManager		
    {
        return RedisCache();
    }
    
    //重写cahce实例
    class RedisCache implement Cache<K,V>	{
        get
        put
        remove
        ....
    }

### spring.xml

    <bean class="com.imooc.cache.RedisCacheManager" id="cacheManager"/>
            
    <bean id="securityManager" class="org.apache.shiro.web.mgt.DefaultWebSecurityManager">
        <property name="realm" ref="realm"/>
        <property name="sessionManager" ref="sessionManager"/>
        <property name="cacheManager" ref="cacheManager"/>
    </bean>
			
## shiro记住我

> cookie | Spring.xml

    <bean class="org.apache.shiro.web.mgt.CooikeRememberManager" id="CooikeRememberManager">
        <property name="cooike" ref="cooike"/>
    </bean>
    <bean class="org.apache.shiro.web.servlet.SimpleCooike" id="cooike">
        <constructor-arg value="rememberMe"/><!--构造前台传的参数-->
        <property name="maxAge" value="30000S"/>
    </bean>
    <!--注入到securityManager-->
    <bean id="securityManager" class="org.apache.shiro.web.mgt.DefaultWebSecurityManager">
        <property name="realm" ref="realm"/>
        <property name="sessionManager" ref="sessionManager"/>
        <property name="cacheManager" ref="cacheManager"/>
        <property name="rememberManager" ref="CooikeRememberManager"/>
    </bean>












