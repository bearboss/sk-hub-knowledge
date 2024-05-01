title: Activti5-hello

date: 2021-06-04 17:20:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/34.jpg)

</span>

<!--more-->

# Activiti Hello实现


* 首先第一步，我们要操作流程，必须获取流程引擎实例；
    ```
    /**
     * 获取默认的流程引擎实例 会自动读取activiti.cfg.xml文件 
     */
    private ProcessEngine processEngine=ProcessEngines.getDefaultProcessEngine();
    
    ```

* 第二步，我们需要把前面我们绘制的流程定义图，部署下（底层是解析XML，然后把数据存到数据库的表中去）；
    ```
    /**
     * 部署流程定义
     */
    @Test
    public void deploy(){
        // 获取部署对象
        Deployment deployment=processEngine.getRepositoryService() // 部署Service
                     .createDeployment()  // 创建部署
                     .addClasspathResource("diagrams/helloWorld.bpmn")  // 加载资源文件
                     .addClasspathResource("diagrams/helloWorld.png")   // 加载资源文件
                     .name("HelloWorld流程")  // 流程名称
                     .deploy(); // 部署
        System.out.println("流程部署ID:"+deployment.getId());
        System.out.println("流程部署Name:"+deployment.getName());
    }
    
    ```
* 第三步：我们要启动流程实例，这样一个流程才开始；
    ```
    /**
     * 启动流程实例
     */
    @Test
    public void start(){
        // 启动并获取流程实例
        ProcessInstance processInstance=processEngine.getRuntimeService() // 运行时流程实例Service
            .startProcessInstanceByKey("myFirstProcess"); // 流程定义表的KEY字段值
        System.out.println("流程实例ID:"+processInstance.getId());
        System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());
    }
    ```
* 第四步：启动流程后，我们流程会走到helloWorld节点，我们来查看下"java1234_小锋"这个用户的任务；
    ```
    /**
     * 查看任务
     */
    @Test
    public void findTask(){
        // 查询并且返回任务即可
        List<Task> taskList=processEngine.getTaskService() // 任务相关Service
                .createTaskQuery()  // 创建任务查询
                .taskAssignee("java1234_小锋") // 指定某个人
                .list(); 
        for(Task task:taskList){
            System.out.println("任务ID:"+task.getId());
            System.out.println("任务名称："+task.getName());
            System.out.println("任务创建时间："+task.getCreateTime());
            System.out.println("任务委派人："+task.getAssignee());
            System.out.println("流程实例ID:"+task.getProcessInstanceId());
        }
    }
    ```
* 第五步：我们来完成helloWorld节点任务，让流程走完；

    ```
    /**
    * 完成任务
    */
    @Test
    public void completeTask(){
    processEngine.getTaskService() // 任务相关Service
            .complete("2504"); // 指定要完成的任务ID
    }
    ```

* 这里有个很重要的概念，流程定义和流程实例的关系。大家可以把流程定义和流程实例的关系，理解成类和对象的关系；

* 流程定义就是一个模版，流程实例就是通过模版搞出来的具体的可用的东西。

* 然后我们来运行deploy方法，部署流程定义，这时候我们的流程定义表会发生一些变化；

* * 首先act_re_deployment 流程定义部署表，插入了一条数据；

* * 然后act_re_prodef 流程定义表也会有插入一条数据；

* * 这里有流程定义id name key version等重要信息；后面可以通过接口来获取这些数据；

* *  还有一个act_ge_bytearray表 用来存资源信息；

* * 我们可以看到，把两个资源文件都存了  包括名称 以及文件内容；

* * 以上是部署流程定义 数据库表里发生的事情；


* 然后我们继续 ，下面来启动流程实例；

* * 运行start方法；

* * 启动流程，数据库流程运行表也会发生相应的变化；

* * 首先是运行时流程任务表：act_ru_task；插入了一条任务数据；

* * 这个表很重要，ID_是任务id 数据2504 PROC_INST_ID_是流程实例ID 2501 以及Name 创建时间等；

* * 接下来是act_ru_execution 运行时流程执行表；

* * 这里的话 存的流程执行相关信息；

* *  接下来是act_ru_identitylink 是于执行主体相关信息表

* * 当然我们这里是用具体的用户去执行的，group组的概念


* 流程实例启动完，接下来就到了helloWorld任务节点

* * 我们这时候可以来查看下"Java1234_小锋"任务

* * 运行findTask方法，控制台输出；

    ```
    SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    SLF4J: Defaulting to no-operation (NOP) logger implementation
    SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
    任务ID:2504
    任务名称：HelloWorld
    任务创建时间：Mon Apr 11 13:30:41 CST 2016
    任务委派人：java1234_小锋
    流程实例ID:2501
    ```

* * 说明这个用户有任务可以执行；

* * 我们继续走流程 执行completeTask方法；

* * 执行完后，流程其实就已经走完了。

* * 这时候我们再运行findTask，啥都没有输入，已经没有任务了；


* OK 流程执行完，数据库表会发生什么变化呢？

* * 首先ru开头的运行时候所有表的数据都没了，因为现在流程都走完了。不需要那些数据了；

* * 然后在hi开头的表里，存了不少数据，主要是用来归档查询用的；

* act_hi_taskinst 历史流程实例任务表加了一条任务数据；

* act_hi_procinst 历史流程实例实例表加了一条流程实例相关信息的数据（包括开始时间，结束时间等等信息）；

* act_hi_identitylink 历史流程实例参数者的表加了一条数据；

* act_hi_actinst 历史活动节点表加了三条流程活动节点信息的数据（每个流程实例具体的执行活动节点的信息）；


# Activiti流程定义部署之ZIP方式

* 前面的话，我们使用的是classpath加载资源文件方式来部署流程定义的，但是这种方式有局限性，只能适合小项目，固定写死的流程；

* 实际项目的话，需要来动态导入流程定义文件，通过把bpmn和png文件打包成zip压缩包，然后用户界面直接导入到系统，然后解析，部署流程定义；

* Activiti是支持这种方式的。今天我们来实现下这种方式；

* 首先第一步，把bpmn和png文件打成zip压缩包，放到diagrams文件夹下

* 之前使用方式

    ```
    import org.activiti.engine.ProcessEngine;
    import org.activiti.engine.ProcessEngines;
    import org.activiti.engine.repository.Deployment;
    import org.junit.Test;
     
    public class ProcessDefinition {
     
        /**
         * 获取默认的流程引擎实例 会自动读取activiti.cfg.xml文件 
         */
        private ProcessEngine processEngine=ProcessEngines.getDefaultProcessEngine();
         
        /**
         * 部署流程定义使用classpath方式
         */
        @Test
        public void deployWithClassPath(){
            // 获取部署对象
            Deployment deployment=processEngine.getRepositoryService() // 部署Service
                         .createDeployment()  // 创建部署
                         .addClasspathResource("diagrams/helloWorld.bpmn")  // 加载资源文件
                         .addClasspathResource("diagrams/helloWorld.png")   // 加载资源文件
                         .name("HelloWorld流程")  // 流程名称
                         .deploy(); // 部署
            System.out.println("流程部署ID:"+deployment.getId());
            System.out.println("流程部署Name:"+deployment.getName());
        }
         
    }
    ```

* 下面我们用zip方式来实现，新建一个deployWithZip方法

    ```
    /**
     * 部署流程定义使用zip方式
     */
    @Test
    public void deployWithZip(){
        InputStream inputStream=this.getClass()  // 获取当前class对象
                            .getClassLoader()   // 获取类加载器
                            .getResourceAsStream("diagrams/helloWorld.zip"); // 获取指定文件资源流
        ZipInputStream zipInputStream=new ZipInputStream(inputStream); // 实例化zip输入流对象
        // 获取部署对象
        Deployment deployment=processEngine.getRepositoryService() // 部署Service
                     .createDeployment()  // 创建部署
                     .name("HelloWorld流程2")  // 流程名称
                     .addZipInputStream(zipInputStream)  // 添加zip是输入流
                     .deploy(); // 部署
        System.out.println("流程部署ID:"+deployment.getId());
        System.out.println("流程部署Name:"+deployment.getName());
    }
    ```
    
    ```
    我们运行这个测试类：
    
    SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    SLF4J: Defaulting to no-operation (NOP) logger implementation
    SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
    流程部署ID:7501
    流程部署Name:HelloWorld流程2
    ```
# 数据库表

> 部署流程定义设计到的表

* act_re_deployment 部署流程表
* act_re_procdef    流程定义表
* act_ge_bytearray  资源文件表
* act_ge_property   系统配置表

> 启动流程实例

>> 流程实例运行时

* act_ru_execution      部署流程表
* act_ru_identitylink   身份联系表
* act_ru_task           任务表
* act_hi_actinst        历史 活动节点表
* act_hi_identitylink   历史 身份联系表
* act_hi_procinst       历史 流程实例表
* act_hi_taskinst       历史 流程任务表

> 流程实例结束时

* act_ru_execution      部署流程表 - 清空
* act_ru_identitylink   身份联系表 - 清空
* act_ru_task           任务表    - 清空
* act_hi_actinst        历史 活动节点表 
* act_hi_identitylink   历史 身份联系表
* act_hi_procinst       历史 流程实例表 - 增加结束时间
* act_hi_taskinst       历史 流程任务表

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/82.html)