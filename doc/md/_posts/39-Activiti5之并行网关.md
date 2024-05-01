title: Activiti5之并行网关

date: 2021-06-04 20:20:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/39.jpg)

</span>

<!--more-->

# Activiti之排他网关

* 所谓排他网关 顾名思义 执行到该网关，会有多条线路同时并行执行，当都执行完才继续执行后面的；
* 我们先上图：
![](/images/activiti/activiti5/7.jpg)
* 右侧 ParallelGateway就是并行网关；
* 我们修改后的业务是  学生请假审批提交，班长和班主任审批，当他们都审批完 才最终让校长审批。
* 测试代码：
    ```
    import java.util.List;
     
    import org.activiti.engine.ProcessEngine;
    import org.activiti.engine.ProcessEngines;
    import org.activiti.engine.repository.Deployment;
    import org.activiti.engine.runtime.ProcessInstance;
    import org.activiti.engine.task.Task;
    import org.junit.Test;
     
    public class ParallelGatewayTest {
     
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
                    .addClasspathResource("diagrams/StudentLeaveProcess4.bpmn") // 加载资源文件
                    .addClasspathResource("diagrams/StudentLeaveProcess4.png") // 加载资源文件
                    .name("学生请假流程4") // 流程名称
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
                .startProcessInstanceByKey("studentLevaeProcess4"); // 流程定义表的KEY字段值
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
                .taskAssignee("张三") // 指定某个人
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
                .complete("265003");
        }
    }
    ```

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/84.html)