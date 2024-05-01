title: Maven相关

date: 2021/5/26 11:44

tags: [Maven]

categories: Maven

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/3.jpg)

</span>

<!--more-->

### maven安装

>   <a href="https://archive.apache.org/dist/maven/maven-3/">maven下载</a>
>
>   >  解压到指定目录即可

### 修改仓库地址

    <localRepository>D:\JJDK\repository</localRepository>

### 修改阿里云镜像

    <mirror>
        <id>central</id>
        <name>central</name>                                                                                                              
        <url>http://maven.aliyun.com/nexus/content/groups/public</url>
        <mirrorOf>*</mirrorOf>
    </mirror>
    
    仓库网址： https://maven.aliyun.com/mvn/search

### 查看版本

    mvn -v 

### 配置windows环境变量

    MAVEN_HOME D:\JJDK\maven

### 配置PATH

    %MAVEN_HOME%\bin

### 本地仓库强制更新

    mvn dependency:purge-local-repository
    mvn -Dmaven.test.skip=true clean install -U
    mvn spotless:apply
    mvn dependency:purge-local-repository
    mvn dependency:purge-local-repository -DactTransitively=false -DreResolve=false --fail-at-end
### 跳过热检查
```
-Dspotless.check.skip
mvn -DskipTests=true -Dspotless.check.skip clean package -P flink-1.18,flink-1.17,prod,jdk11,flink-single-version,scala-2.12,aliyun,!dev,!jdk-1.8
```
### 本地跳过test打包

    mvn -Dmaven.test.skip=true clean install

### 基于脚手架创建项目

    ---java项目的
    mvn archetype:generate -DgroupId=com.seckill -DartifactId=FirstApp or -DarchetypeArtifactId=maven -archetype-quickstart -DinteractiveMode=false
    
    在上述情况下，一个新的Java项目命名 FourApp 而整个项目的目录结构会自动创建。
    
    --java web项目
    mvn archetype:generate -DgroupId=com.seckill -DartifactId=seckillApp -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false

### 其余命令
```
#基于tomcat启动
mvn tomcat7:run
#基于spring启动
mvn spring-boot:run
#批量设置版本
mvn versions:set -DnewVersion = 6.0.0-boot2
#批量install
mvn clean install source:jar -Dmaven.test.skip=true
```
### 打包
```
mvn -pl copm-oc/copm-oc-start -am -P dev clean package -Dmaven.test.skip
```
