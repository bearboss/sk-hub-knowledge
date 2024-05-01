title: Hadoop搭建

date: 2021-08-11 15:20:36

tags: Hadoop

categories: Hadoop

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/54.jpg)

</span>

<!--more-->

# Hadoop搭建

### 单机部署

* 配置IP地址
```
    vi /etc/sysconfig/network-scripts/ifcfg-eth0
    #修改
    BOOTPROTO="static"
    #新增
    IPADDR=192.168.182.100 
    GATEWAY=192.168.182.2 
    DNS1=192.168.182.2
    #重启
    service network restart
```
* 修改主机名
```
    hostname bigdata01
    vi /etc/hostname
    #主机名
    bigdata01
```
* 关闭防火墙
```
    systemctl stop firewalld
    systemctl disable firewalld
```
* ssh免登录
```
   ssh-keygen -t rsa
   公钥拷贝到需要免密码登录的机器
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
* 安装jdk
```
    mkdir -p /data/soft
    vi /etc/profile
        export JAVA_HOME=/data/soft/jdk1.8.0_151
        export CLASSPATH=$JAVA_HOME/lib/
        export PATH=.:$JAVA_HOME/bin:$PATH
    source /etc/profile    
```
* 安装hadoop
```
    vi /etc/profile
       export HADOOP_NAME=/data/soft/hadoop-3.2.0
       export PATH= $HADOOP_HOME/sbin:$HADOOP_HOME/bin:$PATH
    source /etc/profile
    
```
* 修改hadoop配置文件
```
    cd /data/soft/hadoop-3.2.0/etc/hadoop/
    主要修改这几个文件:
    hadoop-env.sh
    core-site.xml
    hdfs-site.xml
    mapred-site.xml
    yarn-site.xml
    workers
    
    ## JAVA_HOME：指定java的安装位置
    ## HADOOP_LOG_DIR：hadoop的日志的存放目录  
    vi hadoop-env.sh
        export JAVA_HOME=/data/soft/jdk1.8.0_151
        export HADOOP_LOG_DIR=/data/hadoop_repo/logs/hadoop
        
    ## fs.defaultFS 属性中的主机名需要和你配置的主机名保持一致
    vi core-site.xml
        <property> 
            <name>fs.defaultFS</name> 
            <value>hdfs://bigdata01:9000</value> 
        </property> 
        <property> 
            <name>hadoop.tmp.dir</name> 
            <value>/data/hadoop_repo</value> 
        </property>
        
    #把hdfs中文件副本的数量 
    vi hdfs-site.xml
        <property> 
            <name>dfs.replication</name>
            <value>1</value> 
        </property>
        
    #设置mapreduce使用的资源调度框架   
    vi mapred-site.xml    
        <property>
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
         </property>
         
    #设置yarn上支持运行的服务和环境变量白名单
    vi yarn-site.xml
        <property> 
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
         </property>
         <property>
            <name>yarn.nodemanager.env-whitelist</name> 
            <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value> 
        </property>
        
    #设置集群中从节点的主机名信息 
    vi workers
        bigdata01
```
* 格式化hdfs
* * Hadoop中的HDFS是一个分布式的文件系统，文件系统在使用之前是需要先格式化的，就类似我们买一块新的磁盘，在安装系统之前需要先格式化才可以使用
```
    bin/hdfs namenode -format
    #如果能看到successfully formatted这条信息就说明格式化成功了
    #如果需要重复执行，那么需要把/data/hadoop_repo目录中的内容全部删除，再执行格式化
```
* 增加启动用户
```
    vi start-dfs.sh
        HDFS_DATANODE_USER=root 
        HDFS_DATANODE_SECURE_USER=hdfs 
        HDFS_NAMENODE_USER=root 
        HDFS_SECONDARYNAMENODE_USER=root
        
    vi stop-dfs.sh
        HDFS_DATANODE_USER=root 
        HDFS_DATANODE_SECURE_USER=hdfs 
        HDFS_NAMENODE_USER=root 
        HDFS_SECONDARYNAMENODE_USER=root 
          
    vi start-yarn.sh
        YARN_RESOURCEMANAGER_USER=root 
        HADOOP_SECURE_DN_USER=yarn 
        YARN_NODEMANAGER_USER=root
        
    vi stop-yarn.sh
        YARN_RESOURCEMANAGER_USER=root 
        HADOOP_SECURE_DN_USER=yarn 
        YARN_NODEMANAGER_USER=root
```
* 启动加验证
```
    sbin/start-all.sh
    jps
    
    HDFS webui界面：http://bigdata01:9870
    YARN webui界面：http://bigdata01:8088
    
```

### 分布式集群安装
    
* 先创建三台机器 bigdata01 bigdata02 bigdata03

```
    1.设置固定IP
        window hosts
            172.22.134.11 bigdata01
            172.22.133.135 bigdata02
            172.22.141.116 bigdata03
        linux hosts
            vi /etc/hosts
            172.22.134.11 bigdata01
            172.22.133.135 bigdata02
            172.22.141.116 bigdata03
        
    2.关闭防火墙
        systemctl stop firewalld
        systemctl disable firewalld
    
    3.同步时间 
        #01,02,03节点上配置时间同步
        yum install -y ntpdate
        ntpdate -u ntp.sjtu.edu.cn
        vi /etc/crontab
        * * * * * root /usr/sbin/ntpdate -u ntp.sjtu.edu.cn
        
    3.在每台机器上执行免登录
        #01,02,03都执行
        ssh-keygen -t rsa
        #01,02,03本机免密码登录
        cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
        #将bigdata01作为主节点 然后将01的公钥拷到其他机器上
        scp ~/.ssh/authorized_keys bigdata02:~/
        scp ~/.ssh/authorized_keys bigdata03:~/
        在02 03上分别执行
        cat ~/authorized_keys >> ~/.ssh/authorized_keys
        ##有没有必要实现从节点之间互相免密码登录呢？
            这个就没有必要了，因为在启动集群的时候只有主节点需要远程连接其它节点。
```

* 安装hadoop
```
    #这里只需要从bigdata01上修改配置文件 然后将整个hadoop包复制到02,03
    #在01上执行启动命令即可
    ## JAVA_HOME：指定java的安装位置
    ## HADOOP_LOG_DIR：hadoop的日志的存放目录  
    vi hadoop-env.sh
        export JAVA_HOME=/data/soft/jdk1.8.0_151
        export HADOOP_LOG_DIR=/data/hadoop_repo/logs/hadoop
        
    ## fs.defaultFS 属性中的主机名需要和你配置的主机名保持一致
    vi core-site.xml
        <property>
            <name>fs.defaultFS</name>
            <value>hdfs://bigdata01:9000</value>
        </property>
        <property>
            <name>hadoop.tmp.dir</name>
            <value>/data/hadoop_repo</value>
        </property>
        
        <property>
             #开启垃圾桶
            <name>fs.trash.interval</name>
            <value>1440</value>
        </property>
        
    #把hdfs中文件副本的数量 
    vi hdfs-site.xml
        <property>
            <name>dfs.replication</name>
            <value>2</value> </property>
        <property>
            <name>dfs.namenode.secondary.http-address</name>
            <value>bigdata01:50090</value>
        </property>
        <property>
            <name>dfs.permissions.enabled</name>
            <value>false</value>
        </property>

        
    #设置mapreduce使用的资源调度框架   
    vi mapred-site.xml    
        <property>
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>
        <property>
            <name>yarn.app.mapreduce.am.env</name>
            <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
        </property>
        <property>
            <name>mapreduce.map.env</name>
            <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
        </property>
        <property>
            <name>mapreduce.reduce.env</name>
            <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
        </property>
        <property>
            <name>mapreduce.application.classpath</name>
            <value>/data/soft/hadoop-3.2.0/share/hadoop/mapreduce/*,/data/soft/hadoop-3.2.0/share/hadoop/mapreduce/lib/*</value>
        </property>
         
    #设置yarn上支持运行的服务和环境变量白名单
    vi yarn-site.xml
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>
        <property>
            <name>yarn.nodemanager.env-whitelist</name>
            <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
        </property>
        <property>
            <name>yarn.resourcemanager.hostname</name>
            <value>bigdata01</value>
        </property>
        <property>
            <name>yarn.resourcemanager.hostname</name>
            <value>bigdata01</value>
        </property>
        <property>
            <name>yarn.log.server.url</name>
            <value>http://bigdata01:19888/jobhistory/logs/</value>
        </property>
        <property>
            <name>yarn.application.classpath</name>
            <value>/data/soft/hadoop-3.2.0/etc/hadoop:/data/soft/hadoop-3.2.0/share/hadoop/common/lib/*:/data/soft/hadoop-3.2.0/share/hadoop/common/*:/data/soft/hadoop-3.2.0/share/hadoop/hdfs:/data/soft/hadoop-3.2.0/share/hadoop/hdfs/lib/*:/data/soft/hadoop-3.2.0/share/hadoop/hdfs/*:/data/soft/hadoop-3.2.0/share/hadoop/mapreduce/lib/*:/data/soft/hadoop-3.2.0/share/hadoop/mapreduce/*:/data/soft/hadoop-3.2.0/share/hadoop/yarn:/data/soft/hadoop-3.2.0/share/hadoop/yarn/lib/*:/data/soft/hadoop-3.2.0/share/hadoop/yarn/*</value>
        </property>
        <property>
            <name>yarn.log-aggregation-enable</name>
            <value>true</value>
            <description>
             开启日志聚集功能，任务执行完之后，将日志文件自动上传到文件系统（如HDFS文件系统），
             否则通过namenode1:8088页面查看日志文件的时候，会报错
             "Aggregation is not enabled. Try the nodemanager at namenode1:54951"
            </description>
        </property>
        <property>
            <name>yarn.log-aggregation.retain-seconds</name>
            <value>302400</value>
            <description>
             日志文件保存在文件系统（如HDFS文件系统）的最长时间，默认值是-1，即永久有效。
             这里配置的值是：7天 = 3600 * 24 * 7 = 302400
            </description>
        </property>
             
    #设置集群中从节点的主机名信息 
    vi workers
       bigdata02
       bigdata03
```
* 设置启动用户
```
    vi start-dfs.sh 
        HDFS_DATANODE_USER=root 
        HDFS_DATANODE_SECURE_USER=hdfs 
        HDFS_NAMENODE_USER=root 
        HDFS_SECONDARYNAMENODE_USER=root 
    vi stop-dfs.sh 
        HDFS_DATANODE_USER=root 
        HDFS_DATANODE_SECURE_USER=hdfs 
        HDFS_NAMENODE_USER=root 
        HDFS_SECONDARYNAMENODE_USER=root
    vi start-yarn.sh 
        YARN_RESOURCEMANAGER_USER=root 
        HADOOP_SECURE_DN_USER=yarn 
        YARN_NODEMANAGER_USER=root
    vi stop-yarn.sh 
        YARN_RESOURCEMANAGER_USER=root 
        HADOOP_SECURE_DN_USER=yarn 
        YARN_NODEMANAGER_USER=root
```
* 拷贝到从节点
```
    scp -rq hadoop-3.2.0 bigdata02:/data/soft/
    scp -rq hadoop-3.2.0 bigdata03:/data/soft/
```
* hdfs初始化
```
    bin/hdfs namenode -format
```
* 启动
```
    sbin/start-all.sh
    sbin/stop-all.sh
```

### window连接Hadoop异常问题
* 安装[HADOOP](https://github.com/steveloughran/winutils)
```
    HADOOP_HOME D:\JJDK\hadoop-3.0.0
    Path: %HADOOP_HOME%\bin
```