title: BPMN

date: 2021-06-02 15:20:36

tags: BPMN

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/29.jpg)

</span>

<!--more-->

# UserTask

![](/images/activiti/activiti7/userTask.jpg)

# bpmn元素

![](/images/activiti/activiti7/1.jpg)

# 流程组织元素图

![](/images/activiti/activiti7/2.jpg)

# UEL

![](/images/activiti/activiti7/UEL.jpg)

![](/images/activiti/activiti7/UEL2.jpg)

# 网关

![](/images/activiti/activiti7/3.jpg)

## 并行网关

> 全部通过之后进行后续流程

![](/images/activiti/activiti7/5.jpg)

## 排它网关

> 仅满足一个条件进入，未写条件默认走新建bpmn文件顺序执行

> 条件进入

![](/images/activiti/activiti7/6.jpg)

> 审批不通过退回

![](/images/activiti/activiti7/7.jpg)

## 包容网关

> 满足条件的审批人执行完毕流程就结束

![](/images/activiti/activiti7/8.jpg)

# 动态表单

![](/images/activiti/activiti7/check.jpg)
![](/images/activiti/activiti7/check_save.jpg)
![](/images/activiti/activiti7/动态用户.jpg)

    ```
    FormProperty_0nsq3on-_!string-_!姓名-_!请填写姓名-_!f
    FormProperty_3elor37-_!long-_!年龄-_!无-_!s
    
    FormProperty_0nsq3on-_!我是八戒-_!f!_!FormProperty_3elor37-_!男-_!f
    
    FormProperty_3ei84q8-_!string-_!悟空写死姓名-_!悟空写死姓名-_!f
    FormProperty_21nbr6a-_!string-_!性别A-_!FormProperty_3elor37-_!f
    ```

# 高级事件

![](/images/activiti/activiti7/事件.jpg)

![](/images/activiti/activiti7/事件2.jpg)

![](/images/activiti/activiti7/任务.jpg)

## 任务监听器和执行监听器

> 任务监听器能拿到任务相关的属性

> > 可以动态修改任务执行人,候选人等

```
public class TKlistener implements TaskListener {
    @Override
    public void notify(DelegateTask delegateTask) {
        delegateTask.setAssignee("xxx");
    }
}
```

> 执行监听器能拿到流程实例相关的属性

> > 常用于统计任务耗时

```
public class PiListener implements ExecutionListener {
    @Override
    public void notify(DelegateExecution delegateExecution) {
        delegateExecution.getProcessInstanceId();
        delegateExecution.getProcessDefinitionId();
    }
}
```
![](/images/activiti/activiti7/执行监听器.jpg)

![](/images/activiti/activiti7/前端参数.jpg)

## 定时事件

> 指定日期开启流程实例

> 24小时任务未办理短信提醒

> 3天未审核则主管领导介入
### 类型

![](/images/activiti/activiti7/定时事件类型.jpg)

#### 定时
    ```
    2020-02-03 01:22:22
    ```
#### 持续规则

![](/images/activiti/activiti7/持续.jpg)

#### 循环规则

![](/images/activiti/activiti7/循环.jpg)

### 场景

![](/images/activiti/activiti7/场景.jpg)

## 信号事件的捕获与抛出

![](/images/activiti/activiti7/抛出.jpg)

![](/images/activiti/activiti7/信号事件.jpg)

![](/images/activiti/activiti7/配置信号.jpg)

![](/images/activiti/activiti7/代码触发.jpg)

### 总结

* 边界事件: 触发边界的流向

* 中间事件: 阻塞之后触发下一个任务

* 边界非阻塞: 既触发下一个,还是保留原来的待办任务




## 消息事件

> 跨实例触发

> 跨任务触发

![](/images/activiti/activiti7/取回流程图.jpg)

![](/images/activiti/activiti7/退回.jpg)


## 错误事件

![](/images/activiti/activiti7/错误事件.jpg)

## 补偿事件

![](/images/activiti/activiti7/补偿事件.jpg)
![](/images/activiti/activiti7/补偿事件特点.jpg)

## 取消事件

![](/images/activiti/activiti7/取消事件.jpg)

## 额外事件

![](/images/activiti/activiti7/额外事件.jpg)

# 任务

## 手工任务

![](/images/activiti/activiti7/手工任务.jpg)

## 脚本任务

![](/images/activiti/activiti7/脚本任务.jpg)

## 业务规则任务

![](/images/activiti/activiti7/业务规则任务.jpg)

## 接收任务

![](/images/activiti/activiti7/接收任务.jpg)

## 发送任务

![](/images/activiti/activiti7/发送任务.jpg)

## 服务任务

![](/images/activiti/activiti7/服务任务.jpg)

### 服务任务使用

![](/images/activiti/activiti7/服务任务使用.jpg)
![](/images/activiti/activiti7/服务任务注意.jpg)

# 子流程

## 嵌入子流程[同bpmn文件]

## 调用子流程[不同bpmn文件]

## 流程图 

![](/images/activiti/activiti7/嵌套子任务.jpg)

# 多实例任务 - 会签

![](/images/activiti/activiti7/多实例任务.jpg)

![](/images/activiti/activiti7/多实例完成条件.jpg)

```
实例总数: nrOfInstances
当前还没有完成的实例: nrOfActiveInstances
已经完成的实例数:nrOfCompletedInstances
```

# 总结

![](/images/activiti/activiti7/总结-覆盖.jpg)

![](/images/activiti/activiti7/总结-密码.jpg)

![](/images/activiti/activiti7/总结-组.jpg)
