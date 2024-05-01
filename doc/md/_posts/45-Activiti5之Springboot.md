title: Activiti5之Springboot

date: 2021-06-10 10:01:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/45.jpg)

</span>

<!--more-->

# Activiti5之Springboot

> pom.xml

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>
        <parent>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>2.5.0</version>
            <relativePath/> <!-- lookup parent from repository -->
        </parent>
        <groupId>com.imooc</groupId>
        <artifactId>activiti5</artifactId>
        <version>0.0.1-SNAPSHOT</version>
        <name>activiti5</name>
        <description>Demo project for Spring Boot</description>
        <properties>
            <java.version>1.8</java.version>
            <activiti.version>5.22.0</activiti.version>
        </properties>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-web</artifactId>
            </dependency>
            <dependency>
                <groupId>org.mybatis.spring.boot</groupId>
                <artifactId>mybatis-spring-boot-starter</artifactId>
                <version>2.2.0</version>
            </dependency>
    
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <scope>runtime</scope>
            </dependency>
            <dependency>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <optional>true</optional>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-test</artifactId>
                <scope>test</scope>
            </dependency>
            <!--spring activiti start-->
    
            <dependency>
                <groupId>org.activiti</groupId>
                <artifactId>activiti-spring-boot-starter-basic</artifactId>
                <version>${activiti.version}</version>
            </dependency>
            <dependency>
                <groupId>org.activiti</groupId>
                <artifactId>activiti-spring-boot-starter-actuator</artifactId>
                <version>${activiti.version}</version>
            </dependency>
            <dependency>
                <groupId>org.activiti</groupId>
                <artifactId>activiti-rest</artifactId>
                <version>${activiti.version}</version>
                <exclusions>
                    <exclusion>
                        <artifactId>slf4j-log4j12</artifactId>
                        <groupId>org.slf4j</groupId>
                    </exclusion>
                </exclusions>
            </dependency>
    
            <dependency>
                <groupId>org.activiti</groupId>
                <artifactId>activiti-diagram-rest</artifactId>
                <version>${activiti.version}</version>
            </dependency>
            <dependency>
                <groupId>org.activiti</groupId>
                <artifactId>activiti-simple-workflow</artifactId>
                <version>${activiti.version}</version>
            </dependency>
            <dependency>
                <groupId>org.activiti</groupId>
                <artifactId>activiti-spring</artifactId>
                <version>${activiti.version}</version>
            </dependency>
    
            <dependency>
                <groupId>org.apache.xmlgraphics</groupId>
                <artifactId>batik-codec</artifactId>
                <version>1.7</version>
            </dependency>
            <dependency>
                <groupId>org.apache.xmlgraphics</groupId>
                <artifactId>batik-css</artifactId>
                <version>1.7</version>
            </dependency>
            <dependency>
                <groupId>org.apache.xmlgraphics</groupId>
                <artifactId>batik-svg-dom</artifactId>
                <version>1.7</version>
            </dependency>
            <dependency>
                <groupId>org.apache.xmlgraphics</groupId>
                <artifactId>batik-svggen</artifactId>
                <version>1.7</version>
            </dependency>
            <dependency>
                <groupId>org.activiti</groupId>
                <artifactId>activiti-explorer</artifactId>
                <version>${activiti.version}</version>
                <exclusions>
                    <exclusion>
                        <artifactId>slf4j-log4j12</artifactId>
                        <groupId>org.slf4j</groupId>
                    </exclusion>
                </exclusions>
            </dependency>
            <!--spring activiti end-->
    
            <!-- 读取解析yml配置 -->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-configuration-processor</artifactId>
                <optional>true</optional>
            </dependency>
    
    </dependencies>
    
        <build>
            <plugins>
                <plugin>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-maven-plugin</artifactId>
                    <configuration>
                        <excludes>
                            <exclude>
                                <groupId>org.projectlombok</groupId>
                                <artifactId>lombok</artifactId>
                            </exclude>
                        </excludes>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    
    </project>
    ```


> 去掉@SpringBootApplication(exclude = {SecurityAutoConfiguration.class})

    ```
    @SpringBootApplication(exclude = {SecurityAutoConfiguration.class})
    public class Activiti5Application {
    
        public static void main(String[] args) {
            SpringApplication.run(Activiti5Application.class, args);
        }
    
    }
    ```
> ActivitiConfig

    ```
    @Component
    public class ActivitiConfig implements ProcessEngineConfigurationConfigurer {
    
        @Autowired
        DataSource dataSource;
    
        @Override
        public void configure(SpringProcessEngineConfiguration processEngineConfiguration) {
    
            processEngineConfiguration.setActivityFontName("宋体");
            processEngineConfiguration.setLabelFontName("宋体");
            processEngineConfiguration.setAnnotationFontName("宋体");
    
            processEngineConfiguration.setDbIdentityUsed(false);
            processEngineConfiguration.setDatabaseSchemaUpdate("true");
            processEngineConfiguration.setDeploymentMode("never-fail");
            processEngineConfiguration.setDataSource(dataSource);
            processEngineConfiguration.setHistoryLevel(HistoryLevel.FULL);
    
        }
    
    
    }
    ```
    
> application.yml

    ```
    server:
      servlet:
        context-path: /
      port: 5000
    
    spring:
      datasource:
        url: jdbc:mysql://localhost:3306/activiti5?characterEncoding=UTF-8&nullCatalogMeansCurrent=true&serverTimezone=GMT&useSSL=false
        password: root
        username: root
        driver-class-name: com.mysql.cj.jdbc.Driver
    
      activiti:
        check-process-definitions: false
        history-level: full
        database-schema-update: true
        deployment-mode:  never-fail
    ```
    
> resources下创建processes文件夹

> 测试

    ```
    @SpringBootTest
    class Activiti5ApplicationTests {
    
        @Autowired
        RepositoryService repositoryService;
    
        @Test
        void contextLoads0() {
            Deployment deploy = repositoryService.
                    createDeployment().addClasspathResource("processes/1.bpmn").name("八戒执行名称22222").deploy();
            System.out.println(deploy.getName());
        }
    }    
    ```
