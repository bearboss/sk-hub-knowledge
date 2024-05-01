title: SpringBoot整合整理

date: 2021-05-28 15:20:36

tags: SpringBoot

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/17.jpg)

</span>

<!--more-->

# 静态文件配置项

    spring.mvc.static-path-pattern=/static/**
    
    
    
    @Configuration
    public class InterceptorConfig extends WebMvcConfigurationSupport {
    
        @Override
        protected void addResourceHandlers(ResourceHandlerRegistry registry) {
            registry.addResourceHandler("/**")
                    .addResourceLocations("/", "classpath:/static");
            super.addResourceHandlers(registry);
        }
    }
    
    http://127.0.0.1:8080/static/1.jpg
    


# jackson使用

	实体类里面：
	@JsonIgnore -字段忽略
	@JsonFormat(pattern="yyyy-MM-dd hh:mm:ss a",locale="zh",timezone="GMT+8")//格式化时间
	@JsonInclude(Include.NON_NULL)//有值的时候显示，没有值不显示

# spring-boot 热部署

* devtools可以实现页面热部署
* * 即页面修改后会立即生效，这个可以直接在application.properties文件中配置spring.thymeleaf.cache=false来实现
* 实现类文件热部署（类文件修改后不会立即生效），实现对属性文件的热部署。
* * 即devtools会监听classpath下的文件变动，并且会立即重启应用（发生在保存时机）
* * 注意：因为其采用的虚拟机机制，该项重启是很快的
* * * （1）base classloader （Base类加载器）：加载不改变的Class，例如：第三方提供的jar包
* * * （2）restart classloader（Restart类加载器）：加载正在开发的Class
* * 为什么重启很快，因为重启的时候只是加载了在开发的Class，没有重新加载第三方的jar包。

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <!-- optional=true, 依赖不会传递, 该项目依赖devtools; 
        之后依赖boot项目的项目如果想要使用devtools, 需要重新引入 -->
    <optional>true</optional>
</dependency>
```

## 模板开启热部署

    spring.freemarker.cache=false
    spring.thymeleaf.cache=true

## 开启监听

    spring.devtools.restart.enabled=true

## 监听源

    spring.devtools.restart.additional-paths=src/main/java

## 监听mybatis

    restart.include.mapper=/mapper-[\\w-\\.]+jar
    restart.include.pagehelper=/pagehelper-[\\w-\\.]+jar

## 排除某些文件

    spring.devtools.restart.exclude=static/**,public/**
    spring.devtools.restart.exclude=WEB-INF/**

# 加载.properties文件

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-configuration-processor</artifactId>
        <optional>true</optional>
    </dependency>
    
    jdbc.properties
        mysql.jdbc.driver = "com.mysql.jdbc.driver"
        mysql.jdbc.url = "com.mysql.jdbc.driver"
        mysql.jdbc.user = "com.mysql.jdbc.driver"
        mysql.jdbc.password = "com.mysql.jdbc.driver"
    
    @Configuration
    @ConfigurationProperties(prefix="cmysql.jdbc")
    @PropertySource(value="classpath:jdbc.properties")
    public class Resource{
        private string driver
        private string url
        private string user
        private string password
    }

# tomcat修改

    server.session-timeout=60
    server.port=8088
    server.error.path=/error
    server.context-path=/IMooc
    server.address=192.168.1.2
    server.tomcat.uri-encoding=UTF-8


# 加载freemarker模板引擎

    #加入依赖
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-freemarker</artifactId>
    </dependency>
    #开启指定根目录
    spring.freemarker.template-loader-path=classpath:/templates
    # 关闭缓存
    spring.freemarker.cache=false
    spring.freemarker.charset=UTF-8
    spring.freemarker.check-template-location=true
    spring.freemarker.content-type=text/html
    spring.freemarker.expose-request-attributes=true
    spring.freemarker.expose-session-attributes=true
    spring.freemarker.request-context-attribute=request
    spring.freemarker.suffix=.ftl

# 加载 thymeleaf 模板

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
    spring.thymeleaf.prefix=classpath:/templates/
    spring.thymeleaf.suffix=.html
    spring.thymeleaf.mode=HTML5
    spring.thymeleaf.encoding=UTF-8
    spring.thymeleaf.servlet.content-type=text/html
    #开启/关闭缓存
    spring.thymeleaf.cache=false

# thymeleaf 常用标签使用方法

	条件判断:th:if	th:unless 
	循环：th:each 	th:switch
	
	#text与utext text 是原封不动显示，utext可以解析成html
	#th:href = "@{http://www.baidu.com}"  
		th:href="@{/Controller/behavior(parentId=${menuBean.id},type=${type})}" 多参数以？的形式
		th:href="@{/menu/{type}/{parentId}/menusEdit.do(parentId=${menuBean.id},type=${type})}" 多参数以/xx/2/3/xx的形式
	#th:src = "@{/static/js/test.js}"#需要指定静态文件位置
	#form表单
		th:object和*{name} 等同于   ${user.name}
		th:adtion="@{/th/postfrom}" th:object="${user}" th:method="post"
		input  th:field="*{name}" #value
	#if判断	
	th:if="${user.age} == 18"等于
	th:if="${user.age} gt 18"大于
	th:if="${user.age} lt 18"小于
	th:if="${user.age} ge 18"大等于
	th:if="${user.age} le 18"小等于
	#选择下拉框框
	th:selected ="${user.age} eq 18" 
	#th:each
		th:each="person:${userList}"
			th:text="${person.name}"
			th:text="${person.age}"
			th:text="${#data.format(user.birthday,"yyyy-MM-dd hh:mm:ss")}"
	#th:switch
			th:switch="${user.name}"
				th:case="Lee"
				th:case="Lee"
				th:case="*"
	#页面读取i18n配置文件数据
		#application.properties
			spring.messages.basename=i18n/messages
			spring.messages.cache-seconds=3600
			spring.messages.encoding=UTF-8
		/resources/i18n/messages.properties
			roles.manager=manager
			roles.superadmin=superadmin
		页面引用
			th:case="#{roles.manager}"

# springBoot配置全局异常捕获

    1.加一个异常类
        @ControllerAdvice
    2异常方法接收异常并且传入异常	
        @ExceptionHandler(value = Exception.class)
    3.判断是不是ajax
        public static boolean isAjax(HttpServletRequest httpRequest){
            return  (httpRequest.getHeader("X-Requested-With") != null  
                        && "XMLHttpRequest"
                            .equals( httpRequest.getHeader("X-Requested-With").toString()) );
        }	

# SpringBoot 整合mybatis

    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>druid</artifactId>
        <version>1.1.10</version>
    </dependency> 
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.44</version>
    </dependency>
    <dependency>
        <groupId>tk.mybatis</groupId>
        <artifactId>mapper-spring-boot-starter</artifactId>
        <version>2.0.2</version>
    </dependency>
    <dependency>
        <groupId>com.github.pagehelper</groupId>
        <artifactId>pagehelper-spring-boot-starter</artifactId>
        <version> 1.2.5</version>
    </dependency>
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>druid-spring-boot-starter</artifactId>
        <version>1.1.10</version>
    </dependency>
    <dependency>
        <groupId>org.mybatis.generator</groupId>
        <artifactId>mybatis-generator-core</artifactId>
        <version>1.3.6</version>
    </dependency>
    ############################################################
    #
    # 配置阿里数据源
    #
    ############################################################
    spring.datasource.url=jdbc:mysql://localhost:3306/leecx
    spring.datasource.username=root
    spring.datasource.password=root
    spring.datasource.driver-class-name=com.mysql.jdbc.Driver
    spring.datasource.druid.initial-size=1
    spring.datasource.druid.min-idle=1
    spring.datasource.druid.max-active=20
    spring.datasource.druid.test-on-borrow=true
    spring.datasource.druid.stat-view-servlet.allow=true
    ############################################################
    #
    # mybatis 配置
    #
    ############################################################
    # mybatis 配置
    mybatis.type-aliases-package=com.imooc.pojo
    mybatis.mapper-locations=classpath:mapper/*.xml
    #通用mapper配置
    mapper.mappers=com.imooc.utils.MyMapper
    mapper.not-empty=false
    mapper.identity=MYSQL
    # 分页插件配置
    pagehelper.helperDialect=mysql
    pagehelper.reasonable=true
    pagehelper.supportMethodsArguments=true
    pagehelper.params=count=countSql

# 使用gen自动生成代码

    （1）创建generatorConfig.xml
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE generatorConfiguration
                PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
                "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">
        <generatorConfiguration>
            <context id="MysqlContext" targetRuntime="MyBatis3Simple" defaultModelType="flat">
                <property name="beginningDelimiter" value="`"/>
                <property name="endingDelimiter" value="`"/>
    
                <plugin type="tk.mybatis.mapper.generator.MapperPlugin">
                    <property name="mappers" value="com.imooc.utils.MyMapper"/>
                </plugin>
    
                <jdbcConnection driverClass="com.mysql.jdbc.Driver"
                                connectionURL="jdbc:mysql://localhost:3306/leecx"
                                userId="root"
                                password="root">
                </jdbcConnection>
    
                <!-- 对于生成的pojo所在包 -->
                <javaModelGenerator targetPackage="com.imooc.pojo" targetProject="src/main/java"/>
    
                <!-- 对于生成的mapper所在目录 -->
                <sqlMapGenerator targetPackage="mapper" targetProject="src/main/resources"/>
    
                <!-- 配置mapper对应的java映射 -->
                <javaClientGenerator targetPackage="com.imooc.mapper" targetProject="src/main/java"
                                     type="XMLMAPPER"/>
    
                <table tableName="sys_user"></table>
                 
            </context>
        </generatorConfiguration>
    （2） 使用mvn创建 创建插件-然后双击运行-
          使用代码：
            public void generator() throws Exception{
                List<String> warnings = new ArrayList<String>();
                boolean overwrite = true;
                //指定 逆向工程配置文件
                File configFile = new File("generatorConfig.xml"); 
                ConfigurationParser cp = new ConfigurationParser(warnings);
                Configuration config = cp.parseConfiguration(configFile);
                DefaultShellCallback callback = new DefaultShellCallback(overwrite);
                MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config,
                        callback, warnings);
                myBatisGenerator.generate(null);
            } 
            public static void main(String[] args) throws Exception {
                try {
                    GeneratorDisplay generatorSqlmap = new GeneratorDisplay();
                    generatorSqlmap.generator();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }

# pageHelper 使用方法

    // 开始分页
    PageHelper.startPage(page, pageSize);自动拦截并分页	

# 事务

    1、增删改
    @Transactional(propagation=Propagation.REQUIRED 
    2、查
    @Transactional(propagation=Propagation.SUPPORTS      

# 引入redis	

## 依赖

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
    </dependency>

## 配置

	# Redis\数据库索引，默认0
	spring.redis.database=1
	# Redis服务器地址
	spring.redis.host=192.168.1.191
	# Redis端口
	spring.redis.port=6379
	# Redis密码
	spring.redis.password=
	# 连接池最大连接数，-1表示无限制
	spring.redis.pool.max-active=1000
	# 连接池阻塞最大等待时间
	spring.redis.pool.max-wait=-1
	#最大空闲连接数
	spring.redis.pool.max-idle=10
	# 最小空闲连接数
	spring.redis.pool.min-idle=2
	# 连接超时时间（毫秒）
	spring.redis.timeout=0

## 引入类

	@Autowired
	private StringRedisTemplate stringRedisTemplate;
	#直接存字符串
	stringRedisTemplate.opsForValue().set("imooc","范德萨范德萨");
	#存json字符串
	Map<String,Object> map = new HashMap<String, Object>();
	map.put("id","1");
	map.put("name","小明");
	JSONObject s = JSONObject.fromObject(map);
	stringRedisTemplate.opsForValue().set("json:user",s.toString());
	String m = stringRedisTemplate.opsForValue().get("json:user");
	JSONObject obj =JSONObject.fromObject(m);
	System.out.println(obj.getInt("id"));

## 工具类

    @Component
    public class RedisOperator {
        @Autowired
        private StringRedisTemplate redisTemplate;
        // Key（键），简单的key-value操作
        /**
         * 实现命令：TTL key，以秒为单位，返回给定 key的剩余生存时间(TTL, time to live)。
         * 
         * @param key
         * @return
         */
        public long ttl(String key) {
            return redisTemplate.getExpire(key);
        }
        /**
         * 实现命令：expire 设置过期时间，单位秒
         * 
         * @param key
         * @return
         */
        public void expire(String key, long timeout) {
            redisTemplate.expire(key, timeout, TimeUnit.SECONDS);
        }
        /**
         * 实现命令：INCR key，增加key一次
         * 
         * @param key
         * @return
         */
        public long incr(String key, long delta) {
            return redisTemplate.opsForValue().increment(key, delta);
        }
        /**
         * 实现命令：KEYS pattern，查找所有符合给定模式 pattern的 key
         */
        public Set<String> keys(String pattern) {
            return redisTemplate.keys(pattern);
        }
        /**
         * 实现命令：DEL key，删除一个key
         * 
         * @param key
         */
        public void del(String key) {
            redisTemplate.delete(key);
        }
        // String（字符串）
        /**
         * 实现命令：SET key value，设置一个key-value（将字符串值 value关联到 key）
         * 
         * @param key
         * @param value
         */
        public void set(String key, String value) {
            redisTemplate.opsForValue().set(key, value);
        }
        /**
         * 实现命令：SET key value EX seconds，设置key-value和超时时间（秒）
         * 
         * @param key
         * @param value
         * @param timeout
         *            （以秒为单位）
         */
        public void set(String key, String value, long timeout) {
            redisTemplate.opsForValue().set(key, value, timeout, TimeUnit.SECONDS);
        }
        /**
         * 实现命令：GET key，返回 key所关联的字符串值。
         * 
         * @param key
         * @return value
         */
        public String get(String key) {
            return (String)redisTemplate.opsForValue().get(key);
        }
        // Hash（哈希表）
        /**
         * 实现命令：HSET key field value，将哈希表 key中的域 field的值设为 value
         * 
         * @param key
         * @param field
         * @param value
         */
        public void hset(String key, String field, Object value) {
            redisTemplate.opsForHash().put(key, field, value);
        }
        /**
         * 实现命令：HGET key field，返回哈希表 key中给定域 field的值
         * 
         * @param key
         * @param field
         * @return
         */
        public String hget(String key, String field) {
            return (String) redisTemplate.opsForHash().get(key, field);
        }
        /**
         * 实现命令：HDEL key field [field ...]，删除哈希表 key 中的一个或多个指定域，不存在的域将被忽略。
         * 
         * @param key
         * @param fields
         */
        public void hdel(String key, Object... fields) {
            redisTemplate.opsForHash().delete(key, fields);
        }
        /**
         * 实现命令：HGETALL key，返回哈希表 key中，所有的域和值。
         * 
         * @param key
         * @return
         */
        public Map<Object, Object> hgetall(String key) {
            return redisTemplate.opsForHash().entries(key);
        }
        // List（列表）
        /**
         * 实现命令：LPUSH key value，将一个值 value插入到列表 key的表头
         * 
         * @param key
         * @param value
         * @return 执行 LPUSH命令后，列表的长度。
         */
        public long lpush(String key, String value) {
            return redisTemplate.opsForList().leftPush(key, value);
        }
        /**
         * 实现命令：LPOP key，移除并返回列表 key的头元素。
         * 
         * @param key
         * @return 列表key的头元素。
         */
        public String lpop(String key) {
            return (String)redisTemplate.opsForList().leftPop(key);
        }
        /**
         * 实现命令：RPUSH key value，将一个值 value插入到列表 key的表尾(最右边)。
         * 
         * @param key
         * @param value
         * @return 执行 LPUSH命令后，列表的长度。
         */
        public long rpush(String key, String value) {
            return redisTemplate.opsForList().rightPush(key, value);
        }
    }

# 任务TASK

    使用注解@EnableScheduling开启定时任务
        #放在springboot启动文件上面
    
    定义@Component作为组件被容器扫描
        private static final SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
        
        @Scheduled(fixedRate = 3000)#定义每过3秒执行任务
        @Scheduled(cron = "4-40 * * * * ?")#corn表达式
        public void task(){
            System.out.println("现在的时间"+dataformat.format(new Date()));
        }

#  spring执行异步任务

    使用注解@EnableAsync开启异步任务
        #放在springboot启动文件上面
    @Async 注解在方法上。不注解就是同步任务
    示例------
    @Async
    public Future<Boolean> doTask11() throws Exception {
        long start = System.currentTimeMillis();
        Thread.sleep(1000);
        long end = System.currentTimeMillis();
        System.out.println("任务1耗时:" + (end - start) + "毫秒");
        return new AsyncResult<>(true);
    }	

# spring-boot 拦截器

    使用注解@Configuration配置拦截器
    继承WebMvcConfigurerAdapter
    重写addInterceptors添加需要的拦截器地址
    
    @Configuration
    public class WebMvcConfigurer extends WebMvcConfigurerAdapter {
        @Override
        public void addInterceptors(InterceptorRegistry registry) {
            /**
             * 拦截器按照顺序执行
             */
            registry.addInterceptor(new TwoInterceptor()).addPathPatterns("/two/**")
                                                         .addPathPatterns("/one/**");
            registry.addInterceptor(new OneInterceptor()).addPathPatterns("/one/**");
            
            super.addInterceptors(registry);
        }
    }
    OneInterceptor，TwoInterceptor 是实现 HandlerInterceptor 接口的里面的方法，实现具体的代码











