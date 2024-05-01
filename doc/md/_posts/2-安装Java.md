title: 安装Java

date: 2021/5/26 11:44

tags: [Java]

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/2.jpg)

</span>

<!--more-->

# 安装java 
```
yum install java-1.8.0-openjdk-devel.x86_64
```

## Windows安装

### 下载Jdk8

-   选择对应jdk版本下载（Tips：可在Windows下载完成后，通过FTP或者SSH到发送到Linux上）
-   <a href="https://repo.huaweicloud.com/java/jdk/">JDK下载</a>

### 指定目录

    D:\JJDK\java\

### 安装jre

    创建目录安装：D:\JJDK\java\jre1.8.0_281  

### 配置环境变量
    JAVA_HOME： D:\JJDK\java 
    PATH:  %JAVA_HOME%\bin
    CLASSPATH: .;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar;

### 检查

    java -version

## Linux安装

### 下载Jdk8

- 选择对应jdk版本下载（Tips：可在Windows下载完成后，通过FTP或者SSH到发送到Linux上）
- <a href="https://repo.huaweicloud.com/java/jdk/">JDK下载</a>
        

### 登录Linux，切换到root用户

    su root 获取root用户权限，当前工作目录不变(需要root密码)
       
    sudo -i 不需要root密码直接切换成root（需要当前用户密码）

### 在usr目录下建立java安装目录

    cd /usr/local
    
    mkdir java

### 将jdk-8u60-linux-x64.tar.gz拷贝到java目录下

    cp /mnt/hgfs/linux/jdk-8u60-linux-x64.tar.gz /usr/local/java/

### 解压jdk到当前目录

    得到文件夹 jdk1.8.0_*　　(注意：下载不同版本的JDK目录名不同！)
    tar -zxvf jdk-8u60-linux-x64.tar.gz

### 安装完毕为他建立一个链接以节省目录长度

    ln -s /usr/local/java/jdk1.8.0_60/ /usr/local/jdk

### 编辑配置文件，配置环境变量

    vim /etc/profile
    
        JAVA_HOME=/usr/local/jdk
        CLASSPATH=$JAVA_HOME/lib/
        PATH=$PATH:$JAVA_HOME/bin
        export PATH JAVA_HOME CLASSPATH
### jps
```
sudo yum install -y java-1.8.0-openjdk-devel.x86_64
```
### 重启机器或执行命令 

    source /etc/profile
    
    sudo shutdown -r now

### 查看安装情况

    java -version
    
    java version "1.8.0_60"
    Java(TM) SE Runtime Environment (build 1.8.0_60-b27)
    Java HotSpot(TM) Client VM (build 25.60-b23, mixed mode)

### 可能出现的错误信息

    bash: ./java: cannot execute binary file
    
    出现这个错误的原因可能是在32位的操作系统上安装了64位的jdk，
    1、查看jdk版本和Linux版本位数是否一致。
    2、查看你安装的Ubuntu是32位还是64位系统
   <a href="http://www.cnblogs.com/zeze/p/5902124.html" title="点击此处">来源博客</a>

### 杀掉进程的shell脚本

```
#!/bin/bash

if [ -f /home/szhpt/magic-0.0.1-SNAPSHOT.jar ]; then

  cd /data/magic/

  rm -rf /data/magic/magic-0.0.1-SNAPSHOT.jar

  cp -f /home/szhpt/magic-0.0.1-SNAPSHOT.jar /data/magic/

  pids=`ps -ef | grep magic-0.0.1-SNAPSHOT.jar | grep -v grep | awk '{print $2}'`

  echo "当前进程号[]: " $pids

  if [ ! -z "$pids" ]; then
    for id in $pids
    do
      kill -9 $id
      echo "killed $id"
    done
  fi

  nohup java -jar magic-0.0.1-SNAPSHOT.jar &

  rm -rf /home/szhpt/magic-0.0.1-SNAPSHOT.jar

  echo "启动完成"
else
  echo "先在/home/szhpt/上传jar包"    
fi



[ -a FILE ] 如果 FILE 存在则为真。

[ -b FILE ] 如果 FILE 存在且是一个块特殊文件则为真。

[ -c FILE ] 如果 FILE 存在且是一个字特殊文件则为真。

[ -d FILE ] 如果 FILE 存在且是一个目录则为真。

[ -e FILE ] 如果 FILE 存在则为真。

[ -f FILE ] 如果 FILE 存在且是一个普通文件则为真。

[ -g FILE ] 如果 FILE 存在且已经设置了SGID则为真。

[ -h FILE ] 如果 FILE 存在且是一个符号连接则为真。

[ -k FILE ] 如果 FILE 存在且已经设置了粘制位则为真。

[ -p FILE ] 如果 FILE 存在且是一个名字管道(F如果O)则为真。

[ -r FILE ] 如果 FILE 存在且是可读的则为真。

[ -s FILE ] 如果 FILE 存在且大小不为0则为真。

[ -t FD ] 如果文件描述符 FD 打开且指向一个终端则为真。

[ -u FILE ] 如果 FILE 存在且设置了SUID (set user ID)则为真。

[ -w FILE ] 如果 FILE 如果 FILE 存在且是可写的则为真。

[ -x FILE ] 如果 FILE 存在且是可执行的则为真。

[ -O FILE ] 如果 FILE 存在且属有效用户ID则为真。

[ -G FILE ] 如果 FILE 存在且属有效用户组则为真。

[ -L FILE ] 如果 FILE 存在且是一个符号连接则为真。

[ -N FILE ] 如果 FILE 存在 and has been mod如果ied since it was last read则为真。

[ -S FILE ] 如果 FILE 存在且是一个套接字则为真。

[ -o OPTIONNAME ] 如果 shell选项 “OPTIONNAME” 开启则为真。

[ -z STRING ] “STRING” 的长度为零则为真。
```

# 第二种脚本

```
rm -rf ~/app/copm-oc/copm-oc-start.jar 

mv /home/cwbb/copm-oc-start.jar  ~/app/copm-oc/

pid=`ps -ef|grep copm-oc-start.jar|grep -v grep|awk '{print $2}'`

#存在杀掉进程
if [ -n "$pid" ]; then
   kill -9 $pid 
fi

nohup java -jar ~/app/copm-oc/copm-oc-start.jar &

#tail -200f ~/app/copm-oc/nohup.out

```



## 寻找JAVA安装位置

```
which java
	-- /usr/bin/java
ls -lrt /usr/bin/java
	-- /usr/bin/java -> /etc/alternatives/java
ls -lrt /etc/alternatives/java
	--  /etc/alternatives/java -> /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.362.b08-1.el7_9.x86_64/jre/bin/java
vi /etc/profile
	JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.362.b08-1.el7_9.x86_64/jre
    CLASSPATH=$JAVA_HOME/lib/
    PATH=$PATH:$JAVA_HOME/bin
    export PATH JAVA_HOME CLASSPATH
source /etc/profile    
```
# jar 替换文件
```
# 解压
jar -xvf spring-security-web-6.0.3.jar org/springframework/security/web/server/ui/LoginPageGeneratingWebFilter.class
# 修改class
https://hexed.it/
# 替换或者压缩
cp -f ./new/LoginPageGeneratingWebFilter.class org/springframework/security/web/server/ui/LoginPageGeneratingWebFilter.class
||
jar -uvf ./new/LoginPageGeneratingWebFilter.class org/springframework/security/web/server/ui/LoginPageGeneratingWebFilter.class
# 打进jar包
jar -uvf spring-security-web-6.0.3.jar org/springframework/security/web/server/ui/LoginPageGeneratingWebFilter.class
```

# jar替换文件2
```
# 看一下在哪里
jar -tvf kafka-ui-api.jar | grep spring-security-web-6.0.3.jar

# 解压
jar -xvf kafka-ui-api.jar

# 替换新包
mv spring-security-web-6.0.3.jar BOOT-INF/lib/spring-security-web-6.0.3.jar

# 重新封成新Jar包
jar -cfM0 kafka-ui-api.jar BOOT-INF/ META-INF/ org/

```
# 指定dump日志
```
java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/dump.hprof -Xmx2048m -DNACOS_CONFIG_SERVER_ADDR=10.51.144.170:8848 -jar your_application.jar

然后通过MAP分析工具进行分析. 百度网盘上存在
```
