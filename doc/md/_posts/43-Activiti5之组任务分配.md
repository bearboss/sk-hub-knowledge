title: Activiti5之组任务分配

date: 2021-06-04 21:58:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/43.jpg)

</span>

<!--more-->

# Activiti5之组任务分配

* 前面我们讲到了activiti内置的用户和组的表设计，我们现在给下数据，然后来讲解组任务分配；
* 用户表：
![](/images/activiti/activiti5/user/14.jpg)
* 角色表：
![](/images/activiti/activiti5/user/15.jpg)
* 用户和角色关系表：
![](/images/activiti/activiti5/user/16.jpg)
* 这里的话lisi,zhangli用户都是dev开发组角色；
* 接下来我们说下组任务分配的概念，我们在实际业务开发过程中，某一个审批任务节点可以分配一个角色（或者叫做组），
* 然后属于这个角色的任何一个用户都可以去完成这个任务节点的审批；


## 方式一，直接流程图配置中写死

* 首先来配置下流程图设计：
![](/images/activiti/activiti5/user/17.jpg)
* 这里我们设置dev角色或者叫做组  开发角色可以审批这个节点；
* 只要是属于dev角色的用户，都可以查询到任务；
* 这里说明一点 查询候选人 依然要用 taskCandidateUser
* 这里 zhangsan ,lisi 都属于dev角色，所以这两个人当中任何一个人都能查询到任务，任何一个人办理都行；


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
                    .addClasspathResource("diagrams/GroupProcess.bpmn") // 加载资源文件
                    .addClasspathResource("diagrams/GroupProcess.png") // 加载资源文件
                    .name("学生请假流程") // 流程名称
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
                .startProcessInstanceByKey("groupProcess"); // 流程定义表的KEY字段值
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
                .taskCandidateUser("zhangsan") // 指定候选人
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
                .complete("347504");
        }
    }
    ```

## 方式二：使用流程变量

* 我们设置下流程变量
![](/images/activiti/activiti5/user/18.jpg)
* 我们启动流程的设置具体的值：

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
                    .addClasspathResource("diagrams/GroupProcess2.bpmn") // 加载资源文件
                    .addClasspathResource("diagrams/GroupProcess2.png") // 加载资源文件
                    .name("学生请假流程") // 流程名称
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
            variables.put("groupId", "dev");
            ProcessInstance pi=processEngine.getRuntimeService() // 运行时Service
                .startProcessInstanceByKey("groupProcess2",variables); // 流程定义表的KEY字段值
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
                .taskCandidateUser("zhangsan") // 指定候选人
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
                .complete("355005");
        }
    }
    ```
# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/84.html)