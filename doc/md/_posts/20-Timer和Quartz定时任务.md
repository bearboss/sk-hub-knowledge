title: Timer和Quartz定时任务

date: 2021-05-29 15:20:36

tags: Quartz

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/20.jpg)

</span>

<!--more-->

# Timer

## TimerTask

* 1.创建myTimerTask 类 继承 TimerTask

* * 实现run方法（具体要实现的逻辑类）


* 2.新建文件-创建主函数 实现定时定频率调用myTimerTask
    ```
    main{
        Timer timer = new Timer();
        myTimerTask tak = new myTimerTask();
        //第一次执行时在2s后，之后每秒过一次
        timer.schedule(tak ,2000L,1000L);
    }
    ```
* 取消定时任务(放在myTimerTask类里面取消,比如执行2次就取消，针对单体)
* * Timer.cancel()
* 方法用于删除计时器中已取消的任务;返回移除的任务数
* *	Timer.purge() 
* 方法用于返回任务最近实际已安排执行时间，返回值long
* * *  TimerTask中的scheduledExecutionTime()

## schedule

* schedule 的四种用法
* * 时间等于或者超过时执行仅执行一次
* * * schedule(task ,time);
* * 时间等于或者超过时执行一次，然后每过period再重复执行
* * * schedule(task ,time，period);
* * 等待delay毫秒之后执行仅执行一次
* * * schedule(task ,delay);
* * 等待delay毫秒之后执行一次，然后每过period再重复执行
* * * schedule(task ,delay，period);

## scheduleAtFixedRate 的两种用法

* *时间等于或者超过时执行一次，然后每过period再重复执行
* * * scheduleAtFixedRate(task ,time，period);
* *等待delay毫秒之后执行一次，然后每过period再重复执行
* * * scheduleAtFixedRate(task ,delay，period);

## schedule 和 scheduleAtFixedRate的区别

* 执行时间早于任务时间
* * scheduleAtFixedRate 会执行多次追赶任务进度
* * schedule 到点执行
* 执行时间超过任务时间
* * schedule 要执行完了才去执行
* * scheduleAtFixedRate 按照时间执行，会存在并发

## Timer缺陷

* 管理并发任务不行（只有一个进程，不能并发）
* 抛异常时缺陷（终止所有任务）


# Quartz

>	Job 实现业务逻辑的接口类 就是定时的任务逻辑

>	属性：name group jobClass jobDataMap 

## HelloJob.java - implements Job 

    public class HelloJob implements Job {
        public void execute(JobExecutionContext context)
                throws JobExecutionException {
            // 打印当前的执行时间，格式为2017-01-01 00:00:00
            Date date = new Date();
            SimpleDateFormat sf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
            System.out.println("Current Exec Time Is : " + sf.format(date));
            System.out.println("Hello World");
        }
    }
## HelloScheduler.java

    public class HelloScheduler {
        public static void main(String[] args) throws SchedulerException, InterruptedException {
            // 打印当前的时间，格式为2017-01-01 00:00:00
            Date date = new Date();
            SimpleDateFormat sf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
            System.out.println("Current Time Is : " + sf.format(date));
            // 创建一个JobDetail实例，将该实例与HelloJob Class绑定
            JobDetail jobDetail = JobBuilder.newJob(HelloJob.class)
                    .withIdentity("myJob", "group1").build();
            //创建触发器
            （1）Trigger trigger =  TriggerBuilder
                    .newTrigger()
                    .withIdentity("myTrigger", "group1")
                    .startNow()
                    .withSchedule(
                            SimpleScheduleBuilder.simpleSchedule().
                                    withIntervalInSeconds(2).repeatForever()
                    )
                    .build();
        
            （2）CronTrigger trigger = CronTriggerBuilder
                    .newTrigger()
                    .withIdentity("myTrigger", "group1")
                    .withSchedule(
                            //每秒执行一次
                            CronScheduleBuilder.cronSchedule("* * * * * ? *")		
                    )
                    .build();		
            // 创建Scheduler实例
            SchedulerFactory sfact = new StdSchedulerFactory();
            Scheduler scheduler = sfact.getScheduler();
            scheduler.start();
            scheduler.scheduleJob(jobDetail, trigger);
        }
    }
    
## 通过JobExecutionContext获取传参

* jobdetail 和 trigger 传参 .usingJobData("key","value");

* 在helleoJob里面获取参数

* * 通过手动去获取

    ```
    #获取JobDetail名字，分组和自定义参数
    JobKey key = context.getJobDetail().getKey();
    key.getName();key.getGroup();
    JobDataMap datamap = context.getJobDetail().getJobDataMap();
    String jobMsg = dataMap.getString("key");
    ```

* * 获取Triiger名字，分组和自定义参数
    ```
        TriggerKey tkey = context.getTrigger.getKey();
        tkey.getName(),tkey.getGroup();
        JobDataMap tdatamap = context.getTrigger().getJobDataMap();
        String tjobMsg = tdataMap.getString("key");
        2.#通过设置同名成员变量
            设置set方法，直接就能获取传入的变量
    ```	
## 基本方法   
 				
### Trigger

    .startAt
    .endAt
    在指定时间内执行一次作业任务
    或者指定时间间隔执行多次任务
    
### scheduler

    standby 任务挂起				
    start 开启任务
    shutdown(true|false) 关闭任务-true 等待关闭在置为shutdown false先置为关闭
    isShutdown 是否被关闭
    --删除任务
    sched.pauseTrigger();// 停止触发器
    sched.unscheduleJob();// 移除触发器
    sched.deleteJob();// 删除任务


