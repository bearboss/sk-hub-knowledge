title: Activiti5之排它网关

date: 2021-06-04 19:40:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/38.jpg)

</span>

<!--more-->

# Activiti之排他网关

* 所谓排他网关 顾名思义 执行到该网关，根据条件只能走一条执行线路；
* 在右侧 palette中 的Gateway 有个 ExclusiveGateway 即为默认网关；
![](/images/activiti/activiti5/1.jpg)
* 我们绘制新的流程定义图标：
![](/images/activiti/activiti5/2.jpg)

* 这里我们规定  根据请假天数，来具体让谁来审批

    ```
    请假天数小于3天，班长审批；
    请假天数小于7天，大于等于3天，班主任审批；
    请假天数大于等于7天，校长审批；
    ```

* 这里我们依然用表达式来实现；
![](/images/activiti/activiti5/3.jpg)
* 班长审批连线表达式；
![](/images/activiti/activiti5/4.jpg)
* 班主任审批连线表达式；
* 至于校长审批，我们不需要再设置表达式了，排他网关可以指定默认的执行线路；
* 我们找到校长审批的id；
![](/images/activiti/activiti5/5.jpg)
* 是flow11；
* 然后我们选中 排他网关，设置默认执行的线路；
![](/images/activiti/activiti5/6.jpg)
* 我们给下执行代码：

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
     
    public class ExclusiveGatewayTest {
     
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
                    .addClasspathResource("diagrams/StudentLeaveProcess3.bpmn") // 加载资源文件
                    .addClasspathResource("diagrams/StudentLeaveProcess3.png") // 加载资源文件
                    .name("学生请假流程3") // 流程名称
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
                .startProcessInstanceByKey("studentLevaeProcess3"); // 流程定义表的KEY字段值
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
                .taskAssignee("赵六") // 指定某个人
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
                .complete("237504");
        }
         
        @Test
        public void completeTask2(){
     
            Map<String, Object> variables=new HashMap<String,Object>();
            variables.put("days", 8);
            processEngine.getTaskService() // 任务相关Service
                .complete("235004", variables); //完成任务的时候，设置流程变量
        }
    }
    ```

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/84.html)