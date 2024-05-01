title: Jenkins部署Git服务

date: 2021-05-29 15:20:36

tags: Jenkins

categories: Jenkins

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/23.jpg)

</span>

<!--more-->

# 安装jenkins

## 下载

* [jenkins](https://www.jenkins.io/zh/download/)

## 安装

* 输入密码，创建用户，按照社区插件安装

## 下载插件

* Publish Over Ssh 
* git 
* Localization: Chinese (Simplified)  - 汉化软件
* PostBuildScript – 打包完成后执行ssh
* Pipeline Maven Integration   - 创建maven项目
* Ssh 

# 配置

## Global Tool Configuration

* 配置Jdk

* * ![](/images/jenkins/1.png)

* 配置git

* * ![](/images/jenkins/2.png)

* 配置maven

* * ![](/images/jenkins/3.png)

## Security - 凭据

> 添加服务器账号信息、git账号地址

* * ![](/images/jenkins/4.png)

## 系统配置 - 配置ssh

* ![](/images/jenkins/6.png)

## 系统配置 - 上传文件路径

* ![](/images/jenkins/5.png)

# 执行

## 创建

* ![](/images/jenkins/7.png)

## 指定git

* ![](/images/jenkins/8.png)

## 打包命令

> 如果需要增加本地jar包，
```
mvn install:install-file -Dfile=alipay-sdk-java-3.0.0.jar -DgroupId=com.aliyun -DartifactId=alipay-sdk-java -Dversion=3.0.0 -Dpackaging=jar
```
* ![](/images/jenkins/10.png)

## 上传到服务器

> 根据实际情况删减，这里做了配置外移打包

```
target/lib/**,target/resources/**,target/*.jar
```

* ![](/images/jenkins/15.png)

## 上传之后执行脚本

* ![](/images/jenkins/12.png)

```
jenkens 执行SSH脚本错误 #加上source /etc/profile
source /etc/profile
BUILD_ID=DONTKILLME 
kill -9 $(ps -ef|grep cent-order|grep -v grep|awk '{print $2}') 
nohup java -jar /home/user/xx-0.0.1-SNAPSHOT.jar >  /home/user/nohup.out 2>&1 &
```

* jenkens  编码GBK的不可映射字符
> pom.xml
```
<!-- 文件拷贝时的编码 -->
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
<!-- 编译时的编码 -->
<maven.compiler.encoding>UTF-8</maven.compiler.encoding>
```

* 程序包org.apache.commons.collections不存在
> pom.xml 去掉
```
<scope>provided</scope>
```

# 最后删除空间打包内容

* ![](/images/jenkins/13.png)  