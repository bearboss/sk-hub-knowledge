title: Activiti5之25张表

date: 2021-06-10 09:58:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/44.jpg)

</span>

<!--more-->

# Activiti5之25张表

- <strong>act_ge_* </strong>
- - 表示通用数据，用于不同场景下，如存放资源文件。
- - - act _evt_log 事件日志表
- - - act_ge_bytearray  存放流程的信息和图片信息
- - - act_ge_property    属性数据表，存储整个流程引擎级别的数据,初始化表结构时，会默认插入三条记录(记录的是使用的流程引擎的版本)


- <b>act_re_* </b>
- - 表示流程的基本信息表：包含了流程定义信息 、流程静态资源（图片、规则等）
- - - act_re_deployment    部署信息表
- - - act_re_model            流程设计模型表
- - - act_re_procdef          流程定义数据表


- <b>act_ru_* </b>
- - 表示运行时的表，用户任务、变量、流程实例（ProcessInstance），用户的任务节点信息等运行时的数据，只有在执行中的流程才会有记录，如果该流程执行完毕后，会删除对应的数据。
- - - act_ru_event_subscr   监听信息表（几乎用不上）
- - - act_ru_execution     运行时流程执行实例表
- - - act_ru_identitylink       运行时流程人员表，主要存储任务节点与参与者相关信息
- - - act_ru_job         运行时定时任务数据表（几乎用不上）
- - - act_ru_task            运行时任务节点表
- - - act_ru_variable            运行时流程变量数据表


- <b>act_id_* </b>
- - 表示用户信息表 ,这些表包含身份信息，比如用户、组。（基本上是用不到的下边的这些表，因为每个系统都有自己对应的用户信息表）
- - - act_id_group      用户组信息表（和角色或者部门是一样的感觉）
- - - act_id_info         用户扩展信息表
- - - act_id_membership       用户与用户组关系信息表
- - - act_id_user                 用户信息表
- - - act_procdef_info         用户扩展信息表


- <b>act_hi_* 历史数据表，</b>
- - 比如历史流程实例，变量，任务等，只要流程开启了，产生节点任务就会有数据，如果某个任务节点结束了，不会删除对应的数据
- - - act_hi_actinst         历史节点表
- - - act_hi_attachment  历史附件表（几乎用不上）
- - - act_hi_comment    历史意见表（几乎用不上）
- - - act_hi_detail          历史详情表，提供历史变量的查询
- - - act_hi_identitylink  历史流程人员表
- - - act_hi_procinst      历史流程实例表  
- - - act_hi_taskinst      历史流程任务表
- - - act_hi_varinst       历史变量表

# 来源地址

> [魅魍魉](https://blog.csdn.net/qq_39188676/article/details/105346227)