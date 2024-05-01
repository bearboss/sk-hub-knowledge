title: Activiti6.0.0安装脚手架

date: 2021-05-31 15:20:36

tags: Activiti

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/27.jpg)

</span>

<!--more-->

# 下载activiti源码

* [git](https://github.com/Activiti/Activiti)


# 介绍

* 脚手架就相当于是一个模板，若我们采用脚手架，则可以重用之前的代码快速开发。

* 在Activiti的目录结构（见下图）中，原本就是带有脚手架的，但默认不能使用，需要我们手动安装。



# 一、创建默认脚手架


1. 切换分支

* 我们打开一个终端，然后切换新建的分支，若没有，则自己创建
* 切换分支：git checkout -b study6 activiti-6.0.0
* ![](/images/activiti/archetype/2.png)

2. 安装脚手架

    1. 切换好分支后，进入tooling/archetypes目录，进行安装，提示安装成功。
    
    2. mvn clean install
    
    3. ![](/images/activiti/archetype/3.png)

3. 以上已经成功安装了默认的脚手架

# 二、创建自定义脚手架

1. 拷贝脚手架
* 拷贝activiti-archetype-unittest目录，重命名为 activiti-archetype-unittest2，<br/>并修改pom.xml中的内容为activiti-archetype-unittest2
* ![](/images/activiti/archetype/4.png)


2. 修改 ACTIVITI-ARCHETYPE-UNITTEST2内容

    1. 在archetype-resources/src目录下<br/>创建目录man/java和main/resources（默认只有test/java和test/resources目录）  
    * ![](/images/activiti/archetype/5.png)

    2. 将Helloworld项目中的内容拷贝过来
    * [源码下载](/images/activiti/archetype/archetype.zip)
    * java中的DemoMain.java，并修改文件中的包名为package ${package};并添加其他三个文件
    * ![](/images/activiti/archetype/6.png)
   
    3. 修改 META-INF/maven/archetype-metadata.xml文件的内容如下：
    * filetered是否过滤，packaged是否经过包结构过滤，两个都是true;之前的包结构占位符能够替换
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <archetype-descriptor name="activiti-archetype-unittest2">
    <fileSets>
    <fileSet filtered="true" packaged="true">
      <directory>src/main/java</directory>
      <includes>
        <include>**/*.java</include>
      </includes>
    </fileSet>
    <fileSet filtered="false" packaged="false">
      <directory>src/main/resources</directory>
      <includes>
        <include>activiti.cfg.xml</include>
        <include>logback.xml</include>
        <include>second_approve.bpmn20.xml</include>
      </includes>
    </fileSet>
    <fileSet filtered="true" packaged="true">
      <directory>src/test/java</directory>
      <includes>
        <include>**/*.java</include>
      </includes>
    </fileSet>
    <fileSet filtered="true" packaged="true">
      <directory>src/test/resources</directory>
      <includes>
        <include>my-process.bpmn20.xml</include>
      </includes>
    </fileSet>
    </fileSets>
    </archetype-descriptor>
    ```
    4. 删除不用的文件
    * 删除掉test/resource下的activiti.cfg.xml和log4j.properties，因为我们采用logback.xml。
    * 删除时把search in comments and strings前面的钩去掉。

    5. 安装自定义脚手架
    * 进入到本地的activiti-archetype-unittest2目录中进行安装
    ```
    cd activiti-archetype-unittest2
    mvn clean install
    ```
    * ![](/images/activiti/archetype/7.png)
    
    6. 添加脚手架

    * ![](/images/activiti/archetype/8.png)

    7. 显示添加成功
    
    * ![](/images/activiti/archetype/10.png)

# 三、使用脚手架

1. 创建项目

* 重新建一个maven项目（建项目不用脚手架），
* 可以取名为activiti6-samples，GroupId可取com.syc.activiti，ArtifactId可取activiti6-samples。
* 然后新建module模型，选择Maven，并且从archetype创建，选择我们建好的unittest2，模块名可取config。

2. 导入依赖

> 在项目的pom.xml中修改parent为springboot，因为helloword程序依赖的是springboot。

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.syc.activiti</groupId>
    <artifactId>activiti6-samples</artifactId>
    <packaging>pom</packaging>
    <version>1.0-SNAPSHOT</version>
    <modules>
        <module>config</module>
    </modules>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.0.RELEASE</version>
        <relativePath></relativePath>
    </parent>
</project>
```
> 在config的pom.xml中添加guava依赖，不添加该依赖会报错，最好将原先的依赖全部导入

```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>com.syc.activiti</groupId>
	<artifactId>config</artifactId>
	<version>1.0-SNAPSHOT</version>
 
	<dependencies>
		<dependency>
			<groupId>org.activiti</groupId>
			<artifactId>activiti-engine</artifactId>
			<version>6.0.0</version>
			<exclusions>
				<exclusion>
					<artifactId>activation</artifactId>
					<groupId>javax.activation</groupId>
				</exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>4.11</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
			<version>1.1.11</version>
		</dependency>
		<dependency>
			<groupId>com.google.guava</groupId>
			<artifactId>guava</artifactId>
			<version>23.0</version>
		</dependency>
		<dependency>
			<groupId>com.h2database</groupId>
			<artifactId>h2</artifactId>
			<version>1.3.176</version>
		</dependency>
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<version>5.1.22</version>
		</dependency>
		<dependency>
			<groupId>com.alibaba</groupId>
			<artifactId>druid</artifactId>
			<version>1.0.9</version>
		</dependency>
	</dependencies>
 
</project>
```
3. maven项目不能忽略

* Unignore Projects后点击刷新
* ![](/images/activiti/archetype/9.png)

4. 刷新项目后就是可运行状态

5. 运行项目后提示警告：

* WARNING: Illegal reflective access by org.apache.ibatis.reflection.Reflector (file:/D:/maven_repository/org/mybatis/mybatis/3.4.2/mybatis-3.4.2.jar) to method java.lang.Object.finalize() 
* 该问题是jdk的版本过高，我们将project structure中的jdk设置回1.8即可。

# 本文源地址来源

* [灰信网](https://www.freesion.com/article/9811943567/)

