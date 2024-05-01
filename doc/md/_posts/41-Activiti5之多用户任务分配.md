title: Activiti5之多用户任务分配

date: 2021-06-04 20:50:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/41.jpg)

</span>

<!--more-->

# Activiti5之多用户任务分配

> 我们在开发的时候，有一种情况是这样的，

> 我们有一个任务，可以让多个用户中的任何一个人办理即可，比如某个审批任务，

> 张三，李四，王五他们中的任何一人办理下都行，这时候，我们用到多用户任务分配。


# 方式一，直接流程图配置中写死


![](/images/activiti/activiti5/user/4.jpg)

* 这里我们分配三个人 中间用逗号隔开。

    ```
    import java.util.List;
     
    import org.activiti.engine.ProcessEngine;
    import org.activiti.engine.ProcessEngines;
    import org.activiti.engine.repository.Deployment;
    import org.activiti.engine.runtime.ProcessInstance;
    import org.activiti.engine.task.Task;
    import org.junit.Test;
     
    public class AssignTest1 {
     
        /**
         * 获取默认流程引擎实例，会自动读取activiti.cfg.xml文件
         */
        private ProcessEngine processEngine=ProcessEngines.getDefaultProcessEngine();
         
        /**
         * 部署流程定义
         */
        @Test
        public void deploy(){
            Deployment deployment=processEngine.getRepositoryService() // 获取部署相关Service
                    .createDeployment() // 创建部署
                    .addClasspathResource("diagrams/multiUserProcess.bpmn") // 加载资源文件
                    .addClasspathResource("diagrams/multiUserProcess.png") // 加载资源文件
                    .name("学生请假流程5") // 流程名称
                    .deploy(); // 部署
            System.out.println("流程部署ID:"+deployment.getId()); 
            System.out.println("流程部署Name:"+deployment.getName());
        }
         
        /**
         * 启动流程实例
         */
        @Test
        public void start(){
            ProcessInstance pi=processEngine.getRuntimeService() // 运行时Service
                .startProcessInstanceByKey("multiUserProcess"); // 流程定义表的KEY字段值
            System.out.println("流程实例ID:"+pi.getId());
            System.out.println("流程定义ID:"+pi.getProcessDefinitionId()); 
        }
         
         
        /**
         * 查看任务
         */
        @Test
        public void findTask(){
            List<Task> taskList=processEngine.getTaskService() // 任务相关Service
                .createTaskQuery() // 创建任务查询
                //.taskAssignee("李四") // 指定某个人
                .taskCandidateUser("张三") // 候选人查询
                .list();
            for(Task task:taskList){
                System.out.println("任务ID:"+task.getId()); 
                System.out.println("任务名称:"+task.getName());
                System.out.println("任务创建时间:"+task.getCreateTime());
                System.out.println("任务委派人:"+task.getAssignee());
                System.out.println("流程实例ID:"+task.getProcessInstanceId());
            }
        }
    
        /**
         * 完成任务
         */
        @Test
        public void completeTask(){
            processEngine.getTaskService() // 任务相关Service
                .complete("305004");
        }
    }
    ```

* 这里有几点说明下：
* * 1，任务查询的时候 ，我们用 taskCandidateUser 候选人查询方法，不能用taskAssignee 
* * 2，启动流程实例后，我们在act_ru_identitylink表，
![](/images/activiti/activiti5/user/5.jpg)
* 我们可以看到 activit的设计很巧妙， 在流程图里配置的用户 全是参与者participant，然后还有一份候选人candidate，
* 候选人绑定任务id，参与者绑定流程实例ID，这里我们可以通过Activiti的接口来增加或者减少候选人，大家自行查下文档。
* 我们用张三，李四，王五中的任何一人，都能查询到任务，最后任何一人完整任务即可；

## 方式二：使用流程变量

![](/images/activiti/activiti5/user/6.jpg)

* 我们启动流程的时候设置流程变量的值，其他的和上面一样，

    ```
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
     
    import org.activiti.engine.ProcessEngine;
    import org.activiti.engine.ProcessEngines;
    import org.activiti.engine.repository.Deployment;
    import org.activiti.engine.runtime.ProcessInstance;
    import org.activiti.engine.task.Task;
    import org.junit.Test;
     
    public class AssignTest2 {
     
        /**
         * 获取默认流程引擎实例，会自动读取activiti.cfg.xml文件
         */
        private ProcessEngine processEngine=ProcessEngines.getDefaultProcessEngine();
         
        /**
         * 部署流程定义
         */
        @Test
        public void deploy(){
            Deployment deployment=processEngine.getRepositoryService() // 获取部署相关Service
                    .createDeployment() // 创建部署
                    .addClasspathResource("diagrams/multiUserProcess2.bpmn") // 加载资源文件
                    .addClasspathResource("diagrams/multiUserProcess2.png") // 加载资源文件
                    .name("学生请假流程5") // 流程名称
                    .deploy(); // 部署
            System.out.println("流程部署ID:"+deployment.getId()); 
            System.out.println("流程部署Name:"+deployment.getName());
        }
         
        /**
         * 启动流程实例
         */
        @Test
        public void start(){
            Map<String,Object> variables=new HashMap<String,Object>();
            variables.put("userIds", "张三,李四,王五");
            ProcessInstance pi=processEngine.getRuntimeService() // 运行时Service
                .startProcessInstanceByKey("multiUserProcess2",variables); // 流程定义表的KEY字段值
            System.out.println("流程实例ID:"+pi.getId());
            System.out.println("流程定义ID:"+pi.getProcessDefinitionId()); 
        }
         
         
        /**
         * 查看任务
         */
        @Test
        public void findTask(){
            List<Task> taskList=processEngine.getTaskService() // 任务相关Service
                .createTaskQuery() // 创建任务查询
                //.taskAssignee("李四") // 指定某个人
                .taskCandidateUser("张三") // 候选人查询
                .list();
            for(Task task:taskList){
                System.out.println("任务ID:"+task.getId()); 
                System.out.println("任务名称:"+task.getName());
                System.out.println("任务创建时间:"+task.getCreateTime());
                System.out.println("任务委派人:"+task.getAssignee());
                System.out.println("流程实例ID:"+task.getProcessInstanceId());
            }
        }
        /**
         * 完成任务
         */
        @Test
        public void completeTask(){
            processEngine.getTaskService() // 任务相关Service
                .complete("317505");
        }
    }
    ```

## 分配方式三 TaskListener监听实现

* 我们定义一个监听类 MyTaskListener 实现 TaskListener接口：

```
import org.activiti.engine.delegate.DelegateTask;
import org.activiti.engine.delegate.TaskListener;
 
public class MyTaskListener implements TaskListener{
 
    /**
     * 
     */
    private static final long serialVersionUID = 1L;
 
    public void notify(DelegateTask delegateTask) {
        // TODO Auto-generated method stub
        delegateTask.addCandidateUser("张三");
        delegateTask.addCandidateUser("李四");
        delegateTask.addCandidateUser("王五");
    }
 
}
```

![](/images/activiti/activiti5/user/7.jpg)

* 这边指定下 定义的类

    ```
    import java.util.List;
     
    import org.activiti.engine.ProcessEngine;
    import org.activiti.engine.ProcessEngines;
    import org.activiti.engine.repository.Deployment;
    import org.activiti.engine.runtime.ProcessInstance;
    import org.activiti.engine.task.Task;
    import org.junit.Test;
     
    public class AssignTest3 {
     
        /**
         * 获取默认流程引擎实例，会自动读取activiti.cfg.xml文件
         */
        private ProcessEngine processEngine=ProcessEngines.getDefaultProcessEngine();
         
        /**
         * 部署流程定义
         */
        @Test
        public void deploy(){
            Deployment deployment=processEngine.getRepositoryService() // 获取部署相关Service
                    .createDeployment() // 创建部署
                    .addClasspathResource("diagrams/multiUserProcess3.bpmn") // 加载资源文件
                    .addClasspathResource("diagrams/multiUserProcess3.png") // 加载资源文件
                    .name("学生请假流程5") // 流程名称
                    .deploy(); // 部署
            System.out.println("流程部署ID:"+deployment.getId()); 
            System.out.println("流程部署Name:"+deployment.getName());
        }
         
        /**
         * 启动流程实例
         */
        @Test
        public void start(){
            ProcessInstance pi=processEngine.getRuntimeService() // 运行时Service
                .startProcessInstanceByKey("multiUserProcess3"); // 流程定义表的KEY字段值
            System.out.println("流程实例ID:"+pi.getId());
            System.out.println("流程定义ID:"+pi.getProcessDefinitionId()); 
        }
         
         
        /**
         * 查看任务
         */
        @Test
        public void findTask(){
            List<Task> taskList=processEngine.getTaskService() // 任务相关Service
                .createTaskQuery() // 创建任务查询
                //.taskAssignee("李四") // 指定某个人
                .taskCandidateUser("张三") // 候选人查询
                .list();
            for(Task task:taskList){
                System.out.println("任务ID:"+task.getId()); 
                System.out.println("任务名称:"+task.getName());
                System.out.println("任务创建时间:"+task.getCreateTime());
                System.out.println("任务委派人:"+task.getAssignee());
                System.out.println("流程实例ID:"+task.getProcessInstanceId());
            }
        }
         
         
        /**
         * 完成任务
         */
        @Test
        public void completeTask(){
            processEngine.getTaskService() // 任务相关Service
                .complete("325004");
        }
    }
    ```

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/84.html)