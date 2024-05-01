title: Activiti5流程变量

date: 2021-06-04 19:25:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/36.jpg)

</span>

<!--more-->

# 流程变量

* 在流程实例运行过程中，难免要记录或者保存一些数据，然后运行到某个节点的时候，取数据查看，或者是后面学到流程分支的时候 判断流程走向，都要用到一些数据存储。
* 这里就引入了一个新的概念，流程变量，顾名思义，就是流程中用来存储数据的变量；
* Activiti中基本支持所有的基本数据类型作为流程变量，以及支持序列化对象，所以也可以存一个对象；当然实际开发的话，还是要建立一些业务表，来存储业务数据；简单的数据，可以存到到流程变量，比较方便；
* 根据一个流程定义可以启动很多流程实例，每个流程实例里的流程变量都是独立的，互不影响，这个概念要分清楚；
* 下面我来通过一些实例，来学习下流程变量，以及Activiti给我们提供的接口；
* 首先我来画一个新的流程定义：
    ![](/images/activiti/activiti5/a.jpg)
* 一个学生请假流程，流程定义的Id，Name大家自己取下名字，以及“提交请假申请”，“辅导员审批”任务节点的办理人大家自己随便搞个即可；
* 接下来新建一个ProcessVariableTest.java测试类：
* 我们把前面写的代码copy过来改改：
* 首先是deploy流程部署方法：

    ```
    import org.activiti.engine.ProcessEngine;
    import org.activiti.engine.ProcessEngines;
    import org.activiti.engine.repository.Deployment;
    import org.junit.Test;
     
    public class ProcessVariableTest {
     
        /**
         * 获取默认的流程引擎实例 会自动读取activiti.cfg.xml文件 
         */
        private ProcessEngine processEngine=ProcessEngines.getDefaultProcessEngine();
         
        /**
         * 部署流程定义
         */
        @Test
        public void deploy(){
            // 获取部署对象
            Deployment deployment=processEngine.getRepositoryService() // 部署Service
                         .createDeployment()  // 创建部署
                         .addClasspathResource("diagrams/StudentLeaveProcess.bpmn")  // 加载资源文件
                         .addClasspathResource("diagrams/StudentLeaveProcess.png")   // 加载资源文件
                         .name("学生请假流程")  // 流程名称
                         .deploy(); // 部署
            System.out.println("流程部署ID:"+deployment.getId());
            System.out.println("流程部署Name:"+deployment.getName());
        }
    }
    /**
     * 启动流程实例
     */
    @Test
    public void start(){
        // 启动并获取流程实例
        ProcessInstance processInstance=processEngine.getRuntimeService() // 运行时流程实例Service
            .startProcessInstanceByKey("studentLeaveProcess"); // 流程定义表的KEY字段值
        System.out.println("流程实例ID:"+processInstance.getId());
        System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());
    }
    ```

* 然后我们运行start方法 ，启动流程实例，这样一个新的流程实例就产生并且开始运行了。
* 这时候到了 “学生请假提交”任务节点，这时候我们可以添加一些流程变量，比如请假日期，请假天数，请假原因，当然这里为了演示Activiti还支持序列化对象，
* 我们这里再加一个请假的学生对象信息；
* 所以我们建一个实现了序列化接口的实体类Student:

    ```
    import java.io.Serializable;
     
    public class Student implements  Serializable{
     
        /**
         * 
         */
        private static final long serialVersionUID = 1L;
         
        private Integer id;
        private String name;
         
        public Integer getId() {
            return id;
        }
        public void setId(Integer id) {
            this.id = id;
        }
        public String getName() {
            return name;
        }
        public void setName(String name) {
            this.name = name;
        }
        public static long getSerialversionuid() {
            return serialVersionUID;
        }
    }
    ```
    ```
    /**
     * 设置流程变量以及值
     */
    @Test
    public void setVariablesValues(){
        TaskService taskService=processEngine.getTaskService(); // 任务Service
        String taskId="2504"; // 任务id
        taskService.setVariableLocal(taskId, "days", 2); // 存Integer类型
        taskService.setVariable(taskId, "date", new Date()); // 存日期类型
        taskService.setVariable(taskId, "reason", "发烧"); // 存字符串
        Student student=new Student();
        student.setId(1);
        student.setName("张三");
        taskService.setVariable(taskId, "student", student);  // 存序列化对象
    }
    ```
* 这里我们来说明下，首先要设置流程变量，我们需要获取Service，这里的话，TaskService可以设置变量，RuntimeService也可以设置流程变量。
* 假如节点不是任务节点的时候，我们只能用RuntimeService。接口和方法和TaskService一样的；
* 这里我们设置了 请假日期，请假天数，请假理由，请假对象。当然这里set变量的时候 需要一个任务ID，大家可以从任务表里去找；
* 后面的变量都是key:value形式，这里的key当然也可以用中文，设置的时候也可以一次性设置多个变量，都有重载方法的；大家自行研究下；
* 我们执行下这个方法，会对应的把数据库查询到对应的流程变量表中，当然那个对象序列的话，特殊点，存到了字节文件表里去了；
* 当然这里还要讲一个概念，就是全局流程实例变量和任务节点本地变量；
* setVariableLocal 和 setVariable  前者仅仅在某个任务节点有作用 后者在整个流程实例都有效；
* 一般开发用后者即可。后面我们可以演示下效果；

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

* 我们执行completeTask即可；这样我们的执行到了 “辅导员审批”任务节点；
* 我们可以来获取“学生请假提交”任务节点设置的流程变量值；

    ```
    /**
     * 获取流程变量以及值
     */
    @Test
    public void getVariablesValue(){
        TaskService taskService=processEngine.getTaskService(); // 任务Service
        String taskId="7502"; // 任务id
        Integer days=(Integer) taskService.getVariable(taskId, "days");
        Date date=(Date) taskService.getVariable(taskId, "date");
        String reason=(String) taskService.getVariable(taskId, "reason");
        Student student=(Student) taskService.getVariable(taskId, "student");
        System.out.println("请假天数："+days);
        System.out.println("请假日期："+date);
        System.out.println("请假原因："+reason);
        System.out.println("请假对象："+student.getId()+","+student.getName());
    }
    ```

* 这里的任务Id是新的，我们可以去运行时任务表里去找；
* 我们运行下，结果如下：

    ```
    SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    SLF4J: Defaulting to no-operation (NOP) logger implementation
    SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
    请假天数：null
    请假日期：Tue Apr 26 13:32:22 CST 2016
    请假原因：发烧
    请假对象：1,张三
    ```

* 我们发现，天数没取到，原因上面讲了，是任务节点本地变量，只有在前面那个节点作用域内有效，所以在这个节点是取不到的；
* 其他的数据都取到了，包括对象；
* OK 我们先把流程走完，继续执行completeTask方法 ，当然任务ID现在变成了7502,你们的改成对应的即可；
* OK。这样流程是完了，这里关于流程变量，我们还可以在启动流程的时候设置，
    ![](/images/activiti/activiti5/b.jpg)
* 完成当前任务，流向下一个节点的时候，也可以设置流程变量：
    ![](/images/activiti/activiti5/a.png)
* 当然流程变量不能什么数据都放里面，有些复杂的，大块数据，我们要自己定义业务表

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/84.html)