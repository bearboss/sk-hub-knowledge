title: Spring基础

date: 2021-05-28 15:20:36

tags: SpringBoot

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/16.jpg)

</span>

<!--more-->

# BeanDefinitionBuilder通过代码配置到spring容器
```
    // 	创建一个Spring的beanDefinition
    BeanDefinitionBuilder factory = BeanDefinitionBuilder.rootBeanDefinition(SpringJobScheduler.class);
    factory.setInitMethodName("init");
    factory.setScope("prototype");
    
    //	1.添加bean构造参数，相当于添加自己的真实的任务实现类
    if (!ElasticJobTypeEnum.SCRIPT.getType().equals(jobTypeName)) {
      factory.addConstructorArgValue(confBean);
    }
    //	2.添加注册中心
    factory.addConstructorArgValue(this.zookeeperRegistryCenter);
    //	3.添加LiteJobConfiguration
    factory.addConstructorArgValue(jobConfig);

    //	4.如果有eventTraceRdbDataSource 则也进行添加
    if (StringUtils.hasText(eventTraceRdbDataSource)) {
      BeanDefinitionBuilder rdbFactory = BeanDefinitionBuilder.rootBeanDefinition(JobEventRdbConfiguration.class);
      rdbFactory.addConstructorArgReference(eventTraceRdbDataSource);
      factory.addConstructorArgValue(rdbFactory.getBeanDefinition());
    }
    
    //  5.添加监听
    List<?> elasticJobListeners = getTargetElasticJobListeners(conf);
    factory.addConstructorArgValue(elasticJobListeners);
    
    // 	接下来就是把factory 也就是 SpringJobScheduler注入到Spring容器中
    DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();

    String registerBeanName = conf.name() + "SpringJobScheduler";
    defaultListableBeanFactory.registerBeanDefinition(registerBeanName, factory.getBeanDefinition());
    SpringJobScheduler scheduler = (SpringJobScheduler)applicationContext.getBean(registerBeanName);
    scheduler.init();
```
# springboot-starter整合执行mybatis
```
查看https://gitee.com/onlyyou19930510/rabbitmq-demo/tree/master/rabbit-parent/rabbit-core-producer/src/main/java/com/bfxy/rabbit/producer/config/database
```
# 项目运行就执行建表语句
```
  @Autowired
	private DataSource rabbitProducerDataSource;

	@Value("classpath:rabbit-producer-message-schema.sql")
	private Resource schemaScript;

	@Bean
	public DataSourceInitializer initDataSourceInitializer() {
		System.err.println("--------------rabbitProducerDataSource-----------:" + rabbitProducerDataSource);
		final DataSourceInitializer initializer = new DataSourceInitializer();
		initializer.setDataSource(rabbitProducerDataSource);
		initializer.setDatabasePopulator(databasePopulator());
		return initializer;
	}

	private DatabasePopulator databasePopulator() {
		final ResourceDatabasePopulator populator = new ResourceDatabasePopulator();
		populator.addScript(schemaScript);
		return populator;
	}

```
# mybatis 日志只打印SQL,不要记录
```
# 配置文件
mybatis-plus:
  configuration:
    log-impl: org.apache.ibatis.logging.slf4j.Slf4jImpl
# 如果是没有日志工具类就引入
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-to-slf4j</artifactId>
  <version>2.17.2</version>
  <exclusions>
      <exclusion>
          <artifactId>slf4j-api</artifactId>
          <groupId>org.slf4j</groupId>
      </exclusion>
      <exclusion>
          <artifactId>log4j-api</artifactId>
          <groupId>org.apache.logging.log4j</groupId>
      </exclusion>
  </exclusions>
</dependency>

# 日志的xml logback-spring.xml -  主要是mybatis的日志是debug级别

<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <!--可在 application-xx.yml 文件中配置 logback.path 覆盖默认值-->
  <springProperty scope="context" name="LOG_PATH" source="logback.path" defaultValue="logs"/>
  <!--  设置控制台颜色  -->
  <conversionRule conversionWord="clr"
                  converterClass="org.springframework.boot.logging.logback.ColorConverter"/>
  <conversionRule conversionWord="wex"
                  converterClass="org.springframework.boot.logging.logback.WhitespaceThrowableProxyConverter"/>
  <conversionRule conversionWord="wEx"
                  converterClass="org.springframework.boot.logging.logback.ExtendedWhitespaceThrowableProxyConverter"/>
  <!--  定义控制台和文件记录的日志格式  -->
  <property name="CONSOLE_LOG_PATTERN"
            value="${CONSOLE_LOG_PATTERN:-%clr(%d{${LOG_DATEFORMAT_PATTERN:-yyyy-MM-dd HH:mm:ss.SSS}}){faint} %X{traceId:-} %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta} %clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %L %clr(:){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}"/>
  <property name="FILE_LOG_PATTERN"
            value="${CONSOLE_LOG_PATTERN:-%clr(%d{${LOG_DATEFORMAT_PATTERN:-yyyy-MM-dd HH:mm:ss.SSS}}){faint} %X{traceId:-} %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta} %clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %L %clr(:){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}"/>
  <!--  定义控制台和文件记录的日志格式  -->
  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>${CONSOLE_LOG_PATTERN}</pattern>
      <charset>UTF-8</charset>
    </encoder>
  </appender>
  <!--  定义控制台和文件记录的日志格式  -->
  <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <!-- 追加日志到原文件结尾 -->
    <Prudent>true</Prudent>
    <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
      <!--格式化输出：%d表示日期，%thread表示线程名，%-5level：级别从左显示5个字符宽度 %method 方法名  %L 行数 %msg：日志消息，%n是换行符-->
      <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %X{traceId:-} [%thread] %-5level %logger{56}.%method:%L - %msg%n</pattern>
      <charset>utf-8</charset>
    </encoder>
    <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
      <!--日志文件输出的文件名 每小时生成日志文件-->
      <FileNamePattern>${LOG_PATH}/%d{yyyy-MM-dd}.%i.log</FileNamePattern>
      <!--日志文件保留天数-->
      <MaxHistory>30</MaxHistory>
      <!-- 除按日志记录之外，还配置了日志文件不能超过100M(默认)，若超过100M，日志文件会以索引0开始， -->
      <maxFileSize>100MB</maxFileSize>
      <!--  日志文件大小和超过10GMB会清空之前的 -->
      <totalSizeCap>10GB</totalSizeCap>
    </rollingPolicy>
  </appender>
  <!--  SpringBoot 默认的  -->
  <logger name="org.springframework" level="ERROR"/>
  <logger name="org.apache" level="ERROR"/>
  <logger name="java.beans" level="ERROR"/>
  <logger name="org.mybatis" level="DEBUG"/>
  <logger name="org.apache.catalina.startup.DigesterFactory" level="ERROR"/>
  <logger name="org.apache.catalina.util.LifecycleBase" level="ERROR"/>
  <logger name="org.apache.coyote.http11.Http11NioProtocol" level="ERROR"/>
  <logger name="org.apache.sshd.common.util.SecurityUtils" level="ERROR"/>
  <logger name="org.apache.tomcat.util.net.NioSelectorPool" level="ERROR"/>
  <logger name="org.eclipse.jetty.util.component.AbstractLifeCycle" level="ERROR"/>
  <logger name="org.hibernate.validator.internal.util.Version" level="ERROR"/>
  
  
    <appender name="SQL" class="ch.qos.logback.core.rolling.RollingFileAppender">
      <file>${LOG_HOME_PATH}/${APP_DIR}/log_sql.log</file>
      <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
          <fileNamePattern>${LOG_HOME_PATH}/${APP_DIR}/sql/log-sql-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
          <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
              <maxFileSize>100MB</maxFileSize>
          </timeBasedFileNamingAndTriggeringPolicy>
          <!--日志文件保留天数-->
          <maxHistory>30</maxHistory>
      </rollingPolicy>
      <append>true</append>
      <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
          <pattern>%d{yyyy-MM-ddHH:mm:ss.SSS} %-5level %logger Line:%-3L - %msg%n</pattern>
          <charset>utf-8</charset>
      </encoder>
  </appender>
  
  <logger name="com.wugui.datax.admin.mapper.JobRegistryMapper" level="off"/>
  <logger name="com.wugui.datax.admin.mapper.JobGroupMapper" level="off"/>
  <logger name="com.wugui.datax.admin.mapper.JobInfoMapper.scheduleJobQuery" level="off"/>
  <logger name="com.wugui.datax.admin.mapper.JobLogMapper.findFailJobLogIds" level="off"/>
  <logger name="com.wugui.datax.admin.mapper.JobLogMapper.findLogReport" level="off"/>
  <logger name="com.wugui.datax.admin.mapper.JobLogReportMapper.update" level="off"/>
  <!--mybatis log configure-->
  <logger name="com.xxx.xxx.xxxx.mapper" level="DEBUG">
      <appender-ref ref="SQL"/>
  </logger>
  
  <root level="INFO">
    <appender-ref ref="FILE"/>
    <appender-ref ref="CONSOLE"/>
  </root>
</configuration>
```
# 获取应用上下文的四种方式 
```
1. ApplicationContextInitializer 容器创建完成之后的回调
    @SpringBootApplication
    public class SpringDemoApplication {
      public static void main(String[] args) {
        SpringApplication springApplication = new SpringApplication(SpringDemoApplication.class);
        springApplication.addInitializers(new UseIntitiallizer());
        springApplication.run(args);
      }
    }
    public class UseIntitiallizer implements ApplicationContextInitializer<ConfigurableApplicationContext> {
      @Override
      public void initialize(ConfigurableApplicationContext configurableApplicationContext) {
        ApplicationContextStore.setApplicationContext(configurableApplicationContext);
      }
    }
2. ApplicationListener 观察者模式
  @Component
  public class UseListener implements ApplicationListener<ApplicationContextEvent> {
    @Override
    public void onApplicationEvent(ApplicationContextEvent applicationContextEvent) {
      System.out.println(applicationContextEvent.getApplicationContext());
    }
  }
3.Springboot 启动程序的返回
	ConfigurableApplicationContext run = springApplication.run(args);
4.ApplicationContextAware 接口- 常用的工具类实现
  @Component
  public class UseAwre implements ApplicationContextAware {
    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
      System.out.println(applicationContext);
    }
  }
```
# spring启动的时候收集BEAN放进MAp - BeanPostProcessor
```
#bean定义完成了之后会进行回调的方法,可用于收集bean

@Service
public class DecodeerManager implements BeanPostProcessor {
	private static final Map<VideoType, IDecoder> videoIndex = new HashMap<>(16);
	public String decode(VideoType type,String data){
		IDecoder decoder = videoIndex.get(type);
		return decoder.decode(data);
	}
  //收集所有的bean
	@Override
	public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
		if (!(bean instanceof IDecoder)) return bean;
		IDecoder decoder = (IDecoder) bean;
		VideoType type = decoder.type();
		if (videoIndex.containsKey(type)) {
			throw new RuntimeException("重复注册");
		}
		videoIndex.put(type, decoder);
		return BeanPostProcessor.super.postProcessBeforeInitialization(bean, beanName);
	}
	@Override
	public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
		return BeanPostProcessor.super.postProcessAfterInitialization(bean, beanName);
	}
}
```
# BeanFactoryPostProcessor
```
spring提供一个bean的工厂, 可以定义bean的属性,如修改第三方的源码
@Service
public class ThiryClassBeanFactory implements BeanFactoryPostProcessor {

	@Override
	public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
		BeanDefinition beanDefinition = beanFactory.getBeanDefinition("thiryClass");
		beanDefinition.setScope(BeanDefinition.SCOPE_PROTOTYPE);
	}
}
```
# @Transactional
```
/** 主动捕获了异常, 导致事务不能回滚 */
void CatchExceptionCanNotRollback();

/** 不是 unchecked 异常, 事务不能回滚 */
void NotRuntimeExceptionCanNotRollback() throws CustomException;

/** unchecked 异常可以回滚 */
void RuntimeExceptionCanRollback();

/** 指定 rollbackFor , 事务可以回滚*/
void AssignExceptionCanRollback() throws CustomException;

/** 同一个类中, 一个不标注事务的方法去调用标注了事务的方法, 事务会失效 */
void NonTransactionalCanNotRollback();

// 传播行为 Propagation
REQUIRED:
  使用当前的事务，如果当前没有事务，则自己新建一个事务，子方法是必须运行在事务中
  如果当前存在事务，则加入这个事务，成为一个整体。
  举例:领导没饭吃，我有钱，我会自己买了自己吃;领导有的吃，会分给你一起吃
SUPPORTS:
  如果当前有事务，则使用事务;如果当前没有事务，则不使用事务。
  举例:领导没饭吃，我也没饭吃;领导有饭吃，我也有饭吃。
MANDATORY:
  该传播属性强制必须存在一个事务，如果不存在，则抛出异常
  举例:领导必须管饭，不管饭没饭吃，我就不乐意了，就不干了 (抛出异常)
REQUIRESNEW: 
  如果当前有事务，则挂起该事务，并且自己创建一个新的事务给自己使用
  如果没有事务,则同REQUIRED
  举例:领导有饭吃，我偏不要，我自己买了自己吃
NOT_SUPPORTED
  如果当前有事务，则把事务挂起，自己不适用事务去运行数据库操作
  举例:领导有饭吃，分一点给你，我太忙了，放一边，我不吃
NEVER
  如果当前有事务存在，则抛出异常
  举例:领导有饭给你吃，我不想吃我热爱工作，我抛出异常
NESTED
  嵌套事务
  如果当前有事务，则开启子事务 (嵌套事务)，套事务是独立提交或者回滚如果当前没有事务，则同 REQUIRED。
  但是如果主事务提交，则会携带子事务一起提交如果主事务回滚，则子事务会一起回滚。相反，子事务异常，则父事务可以回滚或不回滚。
  举例: 领导决策不对，老板怪罪，领导带着小弟一同受罪。小弟出了差错，领导可以推卸责任。
```
# jackson时间反序列化
```
@DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss") Date date 支持GET
@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8") 内部支持,兼容性不好

#局部自定义
@JsonDeserialize(using = DateJacksonConverter.class)

# 全局
@Configuration
public class DateConverterConfig {

    @Bean
    public DateJacksonConverter dateJacksonConverter() {
        return new DateJacksonConverter();
    }

    @Bean
    public Jackson2ObjectMapperFactoryBean jackson2ObjectMapperFactoryBean(
            @Autowired DateJacksonConverter dateJacksonConverter
    ) {
        Jackson2ObjectMapperFactoryBean jackson2ObjectMapperFactoryBean =
                new Jackson2ObjectMapperFactoryBean();
        jackson2ObjectMapperFactoryBean.setDeserializers(dateJacksonConverter);

        return jackson2ObjectMapperFactoryBean;
    }
}

@Slf4j
public class DateJacksonConverter extends JsonDeserializer<Date> {

    private static final String[] pattern = new String[] {
            "yyyy-MM-dd HH:mm:ss", "yyyy/MM/dd"
    };

    @Override
    public Date deserialize(JsonParser jsonParser, DeserializationContext context)
            throws IOException, JsonProcessingException {

        Date targetDate = null;
        String originDate = jsonParser.getText();

        if (StringUtils.isNotEmpty(originDate)) {

            try {
                long longDate = Long.parseLong(originDate.trim());
                targetDate = new Date(longDate);
            } catch (NumberFormatException pe) {
                try {
                    targetDate = DateUtils.parseDate(
                            originDate, DateJacksonConverter.pattern
                    );
                } catch (ParseException ex) {
                    log.error("parse error: {}", ex.getMessage());
                    throw new IOException("parse error");
                }
            }
        }

        return targetDate;
    }

    @Override
    public Class<?> handledType() {
        return Date.class;
    }
}
```
# 过滤器和拦截器
```
#过滤器
@ServletComponentScan("com.imooc.spring.escape") 启动类添加

@WebFilter(urlPatterns = "/*", filterName = "LogFilter")
public class LogFilter implements Filter {}
 
#拦截器
@Component
public class LogInterceptor implements HandlerInterceptor {}

@Component
@Configuration
public class WebInterceptorAdapter implements WebMvcConfigurer {

    @Override
    public void addInterceptors(InterceptorRegistry registry) {

        registry.addInterceptor(new LogInterceptor()).addPathPatterns("/**").order(0);
        registry.addInterceptor(new UpdateLogInterceptor())
                .addPathPatterns("/**").order(1);

        registry.addInterceptor(new UserIdInterceptor()).addPathPatterns("/**")
                .order(3);
    }
}
```
# spring 异步化改造

```
1. 改造@aysnc
@Configuration
public class AsyncConfig extends AsyncConfigurerSupport {
	@Bean(name = "asyncExecutor")
	public Executor asyncExecutor() {
		ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
		executor.setCorePoolSize(3);
		executor.setMaxPoolSize(3);
		executor.setQueueCapacity(100);
		executor.setThreadNamePrefix("AsyncMvc-");
		executor.initialize();
		return executor;
		// if you define this bean ONLY,
		// you can you use @Async("asyncExecutor") at method level
	}

//    @Override
//    public Executor getAsyncExecutor() {
//        return asyncExecutor();
//        // this is a more appropriate way:
//        //      - implements AsyncConfigurer
//        //      - override getAsyncExecutor method
//    }

	@Override
	public Executor getAsyncExecutor() {
		return new DelegatingSecurityContextExecutor(asyncExecutor());
	}
}
2.@Async 增加到service方法上, 注意同一个类调用, 方法体不是public注解不生效,还是同步
3.接口层改造
@Controller
@RequestMapping("/subscriptions")
public class SubscriptionController {
	@Autowired
	private RSubscriptionService rSubscriptionService;

	@Autowired
	private RStockService rStockService;

	@PostMapping
	public DeferredResult<String> addSubscription(@ModelAttribute(value = "stockSymbol") StockSymbol symbol) {
		DeferredResult<String> result = new DeferredResult<>();
		String name = SecurityContextHolder.getContext().getAuthentication().getName();
		ForkJoinPool.commonPool().submit(() -> {
			try {
				rSubscriptionService.addSubscriptionAsync(name, symbol.getSymbol()).get(5, TimeUnit.SECONDS);
				result.setResult("redirect:/subscriptions?added=" + symbol.getSymbol());
			} catch (Exception e) {
				result.setErrorResult(e);
			}
		});
		return result;
	}

	@GetMapping
	public CompletableFuture<String> subscription(Model model) {
		String name = SecurityContextHolder.getContext().getAuthentication().getName();
		CompletableFuture<String> getSubscriptionModelFuture = rSubscriptionService.findByEmail(name)
				.thenApplyAsync((subscriptions) -> {
					model.addAttribute("email", name);
					model.addAttribute("subscriptions", subscriptions);
					return "subscription";
				});
		return getSubscriptionModelFuture;
	}

	@GetMapping
	private WebAsyncTask<String> getStocks(Model model) {
		Callable<String> callable = () -> {
			List<Stock> stocks;
			stocks = rStockService.getAllStocksAsync().get();
			model.addAttribute("stocks", stocks);
			model.addAttribute("stockSymbol", new StockSymbol());
			return "stocks";
		};
		return new WebAsyncTask<>(callable);
	}
}
```
# 科里化
```
@Data
public class StockModelA {
    private String symbol;
    private String name;

    public StockModelA(String symbol, String name) {
        this.symbol = symbol;
        this.name = name;
    }
}
@Data
public class StockModelB {
    private String symbol;
    private String name;
    private String description;
    private BigDecimal currentPrice;
    private BigDecimal prevClosePrice;

    public StockModelB(String symbol, String name, String description, BigDecimal currentPrice, BigDecimal prevClosePrice) {
        this.symbol = symbol;
        this.name = name;
        this.description = description;
        this.currentPrice = currentPrice;
        this.prevClosePrice = prevClosePrice;
    }
}

# 不停地初始化多个参数.科里化

@Test
public void testSimpleStockModelCreation() {
    BiFunction<String, String, StockModelA> StockModelCreator = (symbol, name) -> new StockModelA(symbol, name);

    Function<String, Function<String, StockModelA>> CurryingStockModelInnerClassCreator =
            symbol -> name -> new StockModelA(symbol, name);

}

@Test
public void testMoreAttrStockModelCreation() {
    Function<String, Function<String, Function<String, Function<BigDecimal, Function<BigDecimal, StockModelB>>>>>
            curryingStockModelCreator =
            symbol -> name -> desc -> currPrice -> prevPrice -> new StockModelB(symbol, name, desc, currPrice, prevPrice);

    StockModelB demoStockModel = curryingStockModelCreator
            .apply("SYMBOL")
            .apply("NAME")
            .apply("DESCRIPTION")
            .apply(new BigDecimal("1.00"))
            .apply(new BigDecimal("0.99"));
}
@Test
public void testPartialModelCreation() {
    Function<String, Function<String, Function<String, Function<BigDecimal, Function<BigDecimal, StockModelB>>>>>
            curryingStockModelCreator =
            symbol -> name -> desc -> currPrice -> prevPrice -> new StockModelB(symbol, name, desc, currPrice, prevPrice);

    Function<BigDecimal, Function<BigDecimal, StockModelB>>
            partialStockModelCreator =
            currPrice -> prevPrice -> curryingStockModelCreator
                    .apply("SYMBOL")
                    .apply("NAME")
                    .apply("DESCRIPTION")
                    .apply(currPrice)
                    .apply(prevPrice);
    StockModelB fromPartialCreated = partialStockModelCreator
            .apply(new BigDecimal("1.00"))
            .apply(new BigDecimal("0.99"));
    System.out.println(fromPartialCreated);
}
```
# 静态文件下载
```
/**
	 * 获取js文件
	 */
@RequestMapping(value = "/datax/js", method = RequestMethod.GET)
public void js(HttpServletResponse response) {
  try {
    response.setHeader("Content-Type", "application/javascript");
    InputStream resourceAsStream = this.getClass().getClassLoader().getResourceAsStream("templates/jquery-3.6.0.min.js");
    byte[] tempbytes = new byte[2048];
    int byteread = 0;
    while ((byteread = resourceAsStream.read(tempbytes)) != -1) {
      response.getOutputStream().write(tempbytes, 0, byteread);
    }
    response.getOutputStream().flush();
  } catch (Exception e) {
    e.printStackTrace();
  }
}
```
