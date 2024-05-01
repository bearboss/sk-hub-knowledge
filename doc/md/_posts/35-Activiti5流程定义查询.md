title: Activiti5流程定义查询

date: 2021-06-04 18:20:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/35.jpg)

</span>

<!--more-->

# 流程定义查询

* 流程定义的查询，本质的话就是通过Activiti框架提供的API对act_re_procdef进行查询操作；

* 我们可以通过API 把act_re_procdef表所有列的数据全部查询出来；以后开发系统的时候 管理员用户可以通过用户界面来维护这些数据；

* Activiti给我们提供非常丰富的API，用来模拟SQL查询，包括通过某些字段查询，模糊查询，分页查询，排序等等；

    ```
    /**
     * 查询流程定义 返回流程定义集合 ---对应act_re_procdef
     */
    @Test
    public void list(){
        List<ProcessDefinition> pdList=processEngine.getRepositoryService() // 获取service类
            .createProcessDefinitionQuery() // 创建流程定义查询
            .processDefinitionKey("myFirstProcess") // 通过key查询
            .list(); // 返回一个集合
        for(ProcessDefinition pd:pdList){
            System.out.println("ID_："+pd.getId());
            System.out.println("NAME_："+pd.getName());
            System.out.println("KEY_："+pd.getKey());
            System.out.println("VERSION_："+pd.getVersion());
            System.out.println("===================");
        }
    }
    ```
  
* 这里我们通过流程定义的KEY查询返回一个集合。然后我们输入流程定义表的部分关键字段

  ```   
    运行输入：
    SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    SLF4J: Defaulting to no-operation (NOP) logger implementation
    SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
    ID_：myFirstProcess:1:4
    NAME_：My First process
    KEY_：myFirstProcess
    VERSION_：1
    ===================
    ID_：myFirstProcess:2:7504
    NAME_：My First process
    KEY_：myFirstProcess
    VERSION_：2
    ===================
    ```

* 当然我们也可以通过流程定义ID来查询某个流程定义；单个返回结果；

    ```
    /**
     * 通过ID查询当个流程定义
     */
    @Test
    public void getById(){
        ProcessDefinition pd=processEngine.getRepositoryService() // 获取service类
                .createProcessDefinitionQuery() // 创建流程定义查询
                .processDefinitionId("myFirstProcess:1:4") // 通过id查询
                .singleResult(); // 查询返回当个结果
        System.out.println("ID_："+pd.getId());
        System.out.println("NAME_："+pd.getName());
        System.out.println("KEY_："+pd.getKey());
        System.out.println("VERSION_："+pd.getVersion());
    }
    ```

* 这里我们主要用到singleResult()方法；

    ```
    运行结果：
    
    SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    SLF4J: Defaulting to no-operation (NOP) logger implementation
    SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
    ID_：myFirstProcess:1:4
    NAME_：My First process
    KEY_：myFirstProcess
    VERSION_：1
    ```

* 模拟条件查询，可以根据某些字段查询，以及Like模糊查询；

* 模拟SQL 排序查询；

* 当然可以升序降序； .orderByProcessDefinitionKey().desc()  或者.acc()；

* 还有listPage 分页查询；


# Activiti流程定义删除


* 前面我们把流程定义添加 查询讲了，现在讲下流程定义的删除；

* 比如我们某个流程定义不需要，我们要删除它；这时候我们可以通过接口，通过流程定义部署ID来删除流程定义；

    ```
    /**
     * 删除流程定义
     */
    @Test
    public void delete(){
        processEngine.getRepositoryService()
            .deleteDeployment("12501"); // 流程部署ID
        System.out.println("delete OK！");
    }
    ```

* 上面那种有个问题，一般情况不会有问题，但是，假如这个流程定义的流程实例在运行活动中，未完结。

* 这时候我们执行上面的代码，会报错；

* 本质的话，就是数据库里的数据 有主外键关联，不能删除；


* 我们实际情况的，假如一个流程定义都不需要了。那那些活动的流程实例也直接了当的级联删除；

* 所以我们这里要搞级联删除

* 这时候 任何情况都能直接删除流程定义； 我们开发的时候就用这种；

    ```
    /**
     * 级联删除 已经在使用的流程实例信息也会被级联删除
     */
    @Test
    public void deleteCascade(){
        processEngine.getRepositoryService()
            .deleteDeployment("12501", true); // 默认是false true就是级联删除
        System.out.println("delete cascade OK!");
    }

    ```
# Activiti获取流程定义图图片

* 在开发流程管理系统的时候，一般在流程定义模块，我们都要求能够查看某个流程定义的流程图片，

* 对应的数据表act_ge_bytearray的BYTES_字段；

* Activiti给我们提供了接口，可以返回一个资源文件输入流，然后我们可以得到一张图片，存到本地服务器，然后我们可以通过图片路径在网页上显示，

* 来实现管理员查询流程定义图片的功能；

* 可能你们的和我的流程部署ID 资源名称不一样，写上对应的即可，然后运行方法。我们会在D盘发现一个图片，即流程定义图图片。

* 实际开发的时候，我们把图片存到项目路径下，然后名字的话，可以根据当前日期年月日时分秒来命名，然后得到路径后，在新的页面，或者是模态窗口里显示图片；

    ```
    我们代码里用到了apache的commons包里的FileUtils类，所以我们在下pom.xml里加下commons_io的依赖：
    
    <dependency>
        <groupId>commons-io</groupId>
        <artifactId>commons-io</artifactId>
        <version>2.4</version>
    </dependency>
    ```
    ```
    /**
    * 通过流程部署ID获取流程图图片
    */
    @Test
    public void getImageById()throws Exception{
    InputStream inputStream=processEngine.getRepositoryService()
        .getResourceAsStream("10001", "helloWorld.png"); // 根据流程部署ID和资源名称获取输入流
    FileUtils.copyInputStreamToFile(inputStream, new File("D:/helloWorld.png"));
    }
    ```
    
# Activiti流程定义“修改”

* 前面讲了流程定义的添加，查询，删除。至于这个修改；我们今天来讨论下；
* 首先说下结论，流程定义是不能修改的；
* 这里举例子，假如一个流程定义的流程实例在活动运行中。假如可以修改，
* 本来要流转到A这个节点，因为流程定义修改了，流转到B这个节点。就不符合当时这个流程实例的初衷了；
* 所以一般开发的话，不能修改流程定义，我们是通过增加版本号的方式。来实现“修改”的；
* 在设计流程图的时候，这里的Id 对应到数据库里的就是那个Key值  只要Id相同。就算是同一个流程定义；
* 比如我们可以发布多次，Id一样，到数据库表那边 Key作为版本属性 值会增加；
* 我们一般启动流程实例的时候，我们用Key来启动。这样启动的时候 就是用的最新版本的流程定义来启动流程实例的；假如用流程定义Id来启动 很不推荐；
* 流程定义的Id值组成的话 是 key值:版本号:流程部署ID；

#Activiti查询最新版本的流程定义集合

* 因为每个流程定义都可能会有好几个版本，所以有时候我们有这样的需求，查询出最新版本的流程定义的集合；
* 怎么来实现呢？ 我们一般的思路是这样的。
* 第一步：我们通过Activiti接口来获取根据流程定义Version升序排序的流程定义的集合；
* 第二步：定义一个有序的Map， Map的key就是我们流程定义的Key，Map的值就是流程定义对象；
* 第三步：我们遍历第一步的集合，put(key,value)  假如Key相同，后者会覆盖前者；
* 第四步：我们获取Map的values。即我们需要的最新版本的流程定义的集合；
* 为了演示，我们搞一个MySecondProcess流程定义；
* 然后我们部署流程定义三次；
* 数据库表里对应的添加三条流程定义信息；
* 下面我们上代码。来实现我们要的功能；

    ```
    /**
     * 查询最新版本的流程定义
     */
    @Test
    public void listLastVersion()throws Exception{
         
        // 获取流程定义集合，根据Key升序排序
        List<ProcessDefinition> listAll=processEngine.getRepositoryService() // 获取service类
                .createProcessDefinitionQuery() // 创建流程定义查询
                .orderByProcessDefinitionVersion().asc() // 根据流程定义版本升序
                .list();
        // 定义有序Map 相同的key 假如添加map的值 后面的值会覆盖前面相同key的值
        Map<String,ProcessDefinition> map=new LinkedHashMap<String,ProcessDefinition>();
        // 遍历集合 根据key来覆盖前面的值 来保证最新的Key覆盖前面的所有老的Key的值 
        for(ProcessDefinition pd:listAll){
            map.put(pd.getKey(), pd);
        }
        List<ProcessDefinition> pdList=new LinkedList<ProcessDefinition>(map.values());
        for(ProcessDefinition pd:pdList){
            System.out.println("ID_："+pd.getId());
            System.out.println("NAME_："+pd.getName());
            System.out.println("KEY_："+pd.getKey());
            System.out.println("VERSION_："+pd.getVersion());
            System.out.println("===================");
        }
    }
    ```
    
# Activiti删除Key相同的所有流程定义

* 有时候我们一个流程定义不需要的，包括所有版本，这时候我们在用户界面上一个一个删除太麻烦；
* 所有有时候我们又这样的需求，一下子把所有Key相同的流程定义全部删除；
* 我们的思路是这样的；
* 第一步：根据Key获取所有的流程定义；
* 第二步：遍历集合，获取每个流程定义的流程部署Id
* 第三步：我们根据流程部署Id即可删除所有的流程定义；

    ```
    /**
     * 删除所有Key相同的流程定义
     * @throws Exception
     */
    @Test
    public void deleteByKey()throws Exception{
        List<ProcessDefinition> pdList=processEngine.getRepositoryService()  // 获取service类
                .createProcessDefinitionQuery() // 创建流程定义查询
                .processDefinitionKey("mySecondProcess") // 根据Key查询
                .list();
        for(ProcessDefinition pd:pdList){  // 遍历集合 获取流程定义的每个部署Id，根据这个id来删除所有流程定义
            processEngine.getRepositoryService()
            .deleteDeployment(pd.getDeploymentId(), true); 
        }
    }
    ```
    
#Activiti 查询流程实例状态

* 在开发中，我们有时候需要查看下某个流程实例的状态，运行中 Or 执行结束 ？
* 这时候我们可以用流程实例Id去运行时执行表去查，假如能查到数据，说明流程实例还是运行，假如没查到，就说明这个流程实例已经运行结束了；

    ```
    /**
     * 查询流程状态（正在执行 or 已经执行结束）
     */
    @Test
    public void processState(){
        ProcessInstance pi=processEngine.getRuntimeService() // 获取运行时Service
            .createProcessInstanceQuery() // 创建流程实例查询
            .processInstanceId("22501") // 用流程实例ID查询
            .singleResult();
        if(pi!=null){
            System.out.println("流程正在执行！");
        }else{
            System.out.println("流程已经执行结束！");
        }
    }
    ```

# Activiti 历史任务查询

* 实际工作流项目中，有一个功能叫做 历史任务查询。
* 我们其实查询的是历史任务实例表；
* 当然这个表的话，不管是已经完结的任务 还是正在执行的任务，都会记录下这个表里。Activiti给我们提供了一个接口 finished；
* 加了之后 就是查询已经完结的任务； 同理还有一个接口unfinished 顾名思义，就是查询未完结的任务；当然这两个都不加，就是把所有任务都查询出来；

    ```
    /**
     * 历史任务查询
     */
    @Test
    public void historyTaskList(){
        List<HistoricTaskInstance> list=processEngine.getHistoryService() // 历史任务Service
                .createHistoricTaskInstanceQuery() // 创建历史任务实例查询
                .taskAssignee("java1234_小锋") // 指定办理人
                .finished() // 查询已经完成的任务  
                .list();
        for(HistoricTaskInstance hti:list){
            System.out.println("任务ID:"+hti.getId());
            System.out.println("流程实例ID:"+hti.getProcessInstanceId());
            System.out.println("班里人："+hti.getAssignee());
            System.out.println("创建时间："+hti.getCreateTime());
            System.out.println("结束时间："+hti.getEndTime());
            System.out.println("===========================");
        }
    }
    ```
# Activiti 查询历史流程实例

* 开发中 有时候我们也需要通过流程实例ID来查询历史流程实例。
* 其实本质就是查询历史流程实例表；
* 这里有一点说下 这个表的id和流程实例id始终是一样的。所以Activiti没有提供获取流程实例id的接口；
* 因为直接getId()获取的值和流程实例Id是一样的；

    ```
    /**
     * 查询历史流程实例
     */
    @Test
    public void getHistoryProcessInstance(){
        HistoricProcessInstance hpi= processEngine.getHistoryService() // 历史任务Service
            .createHistoricProcessInstanceQuery() // 创建历史流程实例查询
            .processInstanceId("2501") // 指定流程实例ID
            .singleResult();
        System.out.println("流程实例ID:"+hpi.getId());
        System.out.println("创建时间："+hpi.getStartTime());
        System.out.println("结束时间："+hpi.getEndTime());
    }
    ```
# Activiti历史活动查询

* 在流程系统开发中，我们有这样一种需求，
* 当流程实例完成后，我们要查下流程活动具体的执行情况，比如这个流程实例什么时候开始的，什么时候结束的，
* 以及中间具体的执行步骤，这时候，我们需要查询历史流程活动执行表，act_hi_actinst
    ![](/images/activiti/activiti5/d.jpg)
* 比如上面这个流程；
* Activiti提供了丰富的接口让我们查询历史活动，上代码：

    ```
        /**
         * 历史活动查询
         */
        @Test
        public void historyActInstanceList(){
            List<HistoricActivityInstance> list=processEngine.getHistoryService() // 历史任务Service
                    .createHistoricActivityInstanceQuery() // 创建历史活动实例查询
                    .processInstanceId("27501") // 指定流程实例id
                    .finished() // 查询已经完成的任务  
                    .list();
            for(HistoricActivityInstance hai:list){
                System.out.println("任务ID:"+hai.getId());
                System.out.println("流程实例ID:"+hai.getProcessInstanceId());
                System.out.println("活动名称："+hai.getActivityName());
                System.out.println("办理人："+hai.getAssignee());
                System.out.println("开始时间："+hai.getStartTime());
                System.out.println("结束时间："+hai.getEndTime());
                System.out.println("===========================");
            }
        }
    ```
    
    ```
    执行结果：
    
    任务ID:27502
    
    流程实例ID:27501
    
    活动名称：Start
    
    办理人：null
    
    开始时间：Thu Jun 30 10:13:20 CST 2016
    
    结束时间：Thu Jun 30 10:13:20 CST 2016
    
    ===========================
    
    任务ID:27503
    
    流程实例ID:27501
    
    活动名称：学生请假申请
    
    办理人：张三
    
    开始时间：Thu Jun 30 10:13:20 CST 2016
    
    结束时间：Thu Jun 30 10:16:13 CST 2016
    
    ===========================
    
    任务ID:30001
    
    流程实例ID:27501
    
    活动名称：班长审批
    
    办理人：李四
    
    开始时间：Thu Jun 30 10:16:13 CST 2016
    
    结束时间：Thu Jun 30 10:16:36 CST 2016
    
    ===========================
    
    任务ID:32501
    
    流程实例ID:27501
    
    活动名称：班主任审批
    
    办理人：王五
    
    开始时间：Thu Jun 30 10:16:36 CST 2016
    
    结束时间：Thu Jun 30 10:16:57 CST 2016
    
    ===========================
    
    任务ID:35001
    
    流程实例ID:27501
    
    活动名称：End
    
    办理人：null
    
    开始时间：Thu Jun 30 10:16:57 CST 2016
    
    结束时间：Thu Jun 30 10:16:57 CST 2016
    
    ===========================
    ```

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/84.html)