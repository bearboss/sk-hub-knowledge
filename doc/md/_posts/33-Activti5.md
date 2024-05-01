title: Activti5

date: 2021-06-04 15:20:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/33.jpg)

</span>

<!--more-->

# Activiti的25张表

* Activiti的运行支持，必须要有Activiti的25张表，主要是在流程运行过程中，记录存储一些参与流程的用户主体，组，以及流程定义的存储，流程执行时候的一些信息，以及流程的历史信息等

* 我们先写一个小实例，来把Activiti的25张表自动生成出来；

* 我们先建一个Maven项目 ActivitiDemo1

* pom.xml里加上 Activiti支持，以及mysql驱动包。

    ```
    <dependencies>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-engine</artifactId>
            <version>5.19.0.2</version>
        </dependency>
        
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-spring</artifactId>
            <version>5.19.0.2</version>
        </dependency>
        
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-bpmn-model</artifactId>
            <version>5.19.0.2</version>
        </dependency>
        
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.38</version>
        </dependency>
    
    </dependencies>
    ```

* 然后我们写一个测试方法，testCreateTable

* 并且在创建db_activiti数据库；

* 我们要先来获取流程引擎配置，然后来配置流程引擎，要配置驱动包，url，数据库用户名，密码；

* 还要设置schema，这里的schema要设置成update。这样可以自动更新

* 配置后，我们通过配置来获取流程引擎。创建实例的时候我们就可以自动生成需要的25张表。

* 代码：

    ```
    package com.java1234.activiti.test;
     
    import org.activiti.engine.ProcessEngine;
    import org.activiti.engine.ProcessEngineConfiguration;
    import org.junit.Test;
     
    public class ActivitiTest01 {
     
        /**
         * 生成25张Activiti表
         */
        @Test
        public void testCreateTable() {
            // 引擎配置
            ProcessEngineConfiguration pec=ProcessEngineConfiguration.createStandaloneProcessEngineConfiguration();
            pec.setJdbcDriver("com.mysql.jdbc.Driver");
            pec.setJdbcUrl("jdbc:mysql://localhost:3306/db_activiti");
            pec.setJdbcUsername("root");
            pec.setJdbcPassword("123456");
             
            /**
             * false 不能自动创建表
             * create-drop 先删除表再创建表
             * true 自动创建和更新表  
             */
            pec.setDatabaseSchemaUpdate(ProcessEngineConfiguration.DB_SCHEMA_UPDATE_TRUE);
             
            // 获取流程引擎对象
            ProcessEngine processEngine=pec.buildProcessEngine();
        }
     
    }
    ```

* 搞定

    ```
    ACT_RE_*: 'RE'表示repository。 这个前缀的表包含了流程定义和流程静态资源 （图片，规则，等等）。
    
    ACT_RU_*: 'RU'表示runtime。 这些运行时的表，包含流程实例，任务，变量，异步任务，等运行中的数据。
    
     Activiti只在流程实例执行过程中保存这些数据， 在流程结束时就会删除这些记录。 这样运行时表可以一直很小速度很快。
    
    ACT_ID_*: 'ID'表示identity。 这些表包含身份信息，比如用户，组等等。
    
    ACT_HI_*: 'HI'表示history。 这些表包含历史数据，比如历史流程实例， 变量，任务等等。
    
    ACT_GE_*: 'GE'表示general。通用数据， 用于不同场景下，如存放资源文件。
    ```

# 引入Activiti配置文件activiti.cfg.xml

* 前面我们用代码实现了生成25张activiti表，今天我们用Activiti提供的activiti.cfg.xml配置文件来简化实现前面的功能；

* [官方文档参考地址](http://activiti.org/userguide/index.html#configuration)

* 我们先在src/test/resources下创建一个xml文件 名字是：activiti.cfg.xml

* 然后我们从官方文档贴下参考的xml代码：

    ```
    <beans xmlns="http://www.springframework.org/schema/beans"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.springframework.org/schema/beans   http://www.springframework.org/schema/beans/spring-beans.xsd">
     
      <bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
     
        <property name="jdbcUrl" value="jdbc:h2:mem:activiti;DB_CLOSE_DELAY=1000" />
        <property name="jdbcDriver" value="org.h2.Driver" />
        <property name="jdbcUsername" value="sa" />
        <property name="jdbcPassword" value="" />
     
        <property name="databaseSchemaUpdate" value="true" />
     
        <property name="jobExecutorActivate" value="false" />
        <property name="asyncExecutorEnabled" value="true" />
        <property name="asyncExecutorActivate" value="false" />
     
        <property name="mailServerHost" value="mail.my-corp.com" />
        <property name="mailServerPort" value="5025" />
      </bean>
     
    </beans>
    ```

* 这里的话，我们要根据我们的项目 修改jdbcUrl jdbcDriver jdbcUsername jdbcPassword 当然还有下面的配置我们可以去掉一些 后面会降到这些配置的用途；

* 修改完后的xml如下：

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <beans xmlns="http://www.springframework.org/schema/beans"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.springframework.org/schema/beans   http://www.springframework.org/schema/beans/spring-beans.xsd">
     
      <bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
     
        <property name="jdbcUrl" value="jdbc:mysql://localhost:3306/db_activiti" />
        <property name="jdbcDriver" value="com.mysql.jdbc.Driver" />
        <property name="jdbcUsername" value="root" />
        <property name="jdbcPassword" value="123456" />
     
        <property name="databaseSchemaUpdate" value="true" />
     
      </bean>
     
    </beans>
    ```

* 接下来我们就是要通过代码来读取配置文件，然后获取工作流引擎实例：

* 代码如下：
    
    ```
    /**
     * 使用xml配置 简化
     */
    @Test
    public void testCreateTableWithXml(){
        // 引擎配置
        ProcessEngineConfiguration pec=ProcessEngineConfiguration.createProcessEngineConfigurationFromResource("activiti.cfg.xml");
        // 获取流程引擎对象
        ProcessEngine processEngine=pec.buildProcessEngine();
    }
    ```

* 然后我们测试的时候 先把前面db_activiti数据下的表 全部删除；然后运行上面的测试类，我们会发现 表自动生成了：

* 表依然是前面的25张表；

* 我们会发现，使用xml配置会简化很多东西。。

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/77.html)