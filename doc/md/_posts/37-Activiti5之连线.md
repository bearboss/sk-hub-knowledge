title: Activiti5之连线

date: 2021-06-04 19:30:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/37.jpg)

</span>

<!--more-->

# 连线

![](/images/activiti/activiti5/e.jpg)
* 为了演示连线的大多数功能，我们重新绘制流程定义图，我们的业务改成，当是一般情况的请假审批，班长审批就行，假如是特殊，重要情况的请假
* 审批，我们需要让班主任也审批下。 所以在班长审批的时候，就会有分支；
* 这里连线是有名称的，即name属性；
![](/images/activiti/activiti5/f.jpg)
* 流程实例具体执行的时候 我们要通过设置流程变量的值 来具体执行某个线路，这个时候，我们还得设置连线的执行表达式：
![](/images/activiti/activiti5/g.jpg)
* 这个表达式类似el表达式；
* 我们现在新建LineTest测试类：
* 核心代码，是completeTask2 执行到班长审批的时候，我们通过设置流程变量，来执行具体的流程走向；
    
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
    public class LineTest {
     
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
                    .addClasspathResource("diagrams/StudentLeaveProcess2.bpmn") // 加载资源文件
                    .addClasspathResource("diagrams/StudentLeaveProcess2.png") // 加载资源文件
                    .name("学生请假流程2") // 流程名称
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
                .startProcessInstanceByKey("studentLevaeProcess2"); // 流程定义表的KEY字段值
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
                .taskAssignee("李四") // 指定某个人
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
                .complete("137504");
        }
         
        @Test
        public void completeTask2(){
     
            Map<String, Object> variables=new HashMap<String,Object>();
            variables.put("msg", "一般情况");
            processEngine.getTaskService() // 任务相关Service
                .complete("140002", variables); //完成任务的时候，设置流程变量
        }
         
     
    }
    ```

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/84.html)