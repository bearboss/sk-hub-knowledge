title: Springboot2.0兼容Activiti6.0.0

date: 2021-06-01 15:20:36

tags: Activiti

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/28.jpg)

</span>

<!--more-->

# 下载activiti源码

* [git](https://github.com/Activiti/Activiti)
*  切换分支：git checkout -b study6 activiti-6.0.0

# 创建springboot-web项目
* ![](/images/activiti/spring/1.jpg)
* ![](/images/activiti/spring/2.jpg)
* 增加监控(pom.xml)
```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-hateoas</artifactId>
</dependency>
```
* application.yml
```
management.endpoints.jmx.exposure.include='*'
```
* 引入activiti
```
<!--activiti心跳监控-->
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring-boot-starter-actuator</artifactId>
    <version>6.0.0</version>
</dependency>
<!--activiti-->
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring-boot-starter-basic</artifactId>
    <version>6.0.0</version>
</dependency>
```
# 修改activiti6.0.0源码

* 将module中的activiti-spring-boot添加为maven子模块
* 修改activiti-spring-boot的pom.xml，修改boot版本[2.0.0.RELEASE]
* ![](/images/activiti/spring/3.png)
* Reimport basic项目

# 修改报错信息 

## ProcessEngineEndpoint

* 修改前
* ![](/images/activiti/spring/4.jpg)
* 修改后
* ![](/images/activiti/spring/5.jpg)

## ProcessEngineMvcEndpoint

* 修改前
* ![](/images/activiti/spring/6.jpg)
* 修改后
* ![](/images/activiti/spring/7.jpg)

## EndpointAutoConfiguration

* 修改前
* ![](/images/activiti/spring/8.jpg)
* 修改后
* ![](/images/activiti/spring/9.jpg)

## DataSourceProcessEngineAutoConfiguration
* 修改前
* ![](/images/activiti/spring/10.jpg)
* 修改后
* ![](/images/activiti/spring/11.jpg)
## SecurityAutoConfiguration
* 修改前
* ![](/images/activiti/spring/12.jpg)
* 修改后
* ![](/images/activiti/spring/13.jpg)

##编译 打包
> mvn clean test-compile

>修改发布版本
* ![](/images/activiti/spring/14.jpg)

>修改父工程对应版本
* ![](/images/activiti/spring/15.jpg)

>修改当前pom文件所有activiti相关的为6.0.0
* ![](/images/activiti/spring/16.jpg)

> mvn clean install

# 引入项目activiti/6.0.0-boot2

* pom.xml

    ```
    <dependency>
        <groupId>org.activiti</groupId>
        <artifactId>activiti-spring-boot-starter-actuator</artifactId>
        <version>6.0.0</version>
    </dependency>
    <dependency>
        <groupId>org.activiti</groupId>
        <artifactId>activiti-spring-boot-starter-basic</artifactId>
        <version>6.0.0-boot2</version>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>8.0.19</version>
    </dependency>
    <!-- Druid依赖 -->
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>druid</artifactId>
        <version>1.0.25</version>
    </dependency>
    ```
* 添加数据库
    ```
    spring:
      datasource:
        dirver-class-name: com.mysql.cj.jdbc.Driver'
        url: jdbc:mysql://127.0.0.1:3306/activiti6unit?useTimezone=true&serverTimezone=Asia/Shanghai&useUnicode=true&characterEncoding=UTF-8&useSSL=true
        username: root
        password: root
        #druid连接池配置
        type: com.alibaba.druid.pool.DruidDataSource
    ```
* 增加resource/processes文件夹
* * my-process.bpmn20.xml
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:activiti="http://activiti.org/bpmn"
        xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC"
        xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" typeLanguage="http://www.w3.org/2001/XMLSchema"
        expressionLanguage="http://www.w3.org/1999/XPath" targetNamespace="http://www.activiti.org/test">
        <process id="my-process">
            <startEvent id="start" />
            <sequenceFlow id="flow1" sourceRef="start" targetRef="someTask" />
            <userTask id="someTask" name="Activiti is awesome!" />
            <sequenceFlow id="flow2" sourceRef="someTask" targetRef="end" />
            <endEvent id="end" />
        </process>
    </definitions>
    ```
* 测试
    ```
    @Autowired
    RuntimeService runtimeService;
    
    @Test
    public void contextLoads() {
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("my-process");
        logger.info("'''''{}",processInstance);
    }
    ```
# activiti检测
    ```
    <dependency>
        <groupId>org.activiti</groupId>
        <artifactId>activiti-spring-boot-starter-actuator</artifactId>
        <version>6.0.0</version>
    </dependency>
    
    management:
      endpoints:
        web:
          exposure:
            include: '*'
    ```
* http://127.0.0.1:8080/actuator/activiti
* * ![](/images/activiti/spring/17.jpg)

# idea编辑bpmn文件

* 自带插件 Jboss jBPM
* * 手写xml可提示节点名
* 画图工具 actiBPM
* * 可画图

# 总结

* 测试版本为2.0.0-RELEASE!!!
