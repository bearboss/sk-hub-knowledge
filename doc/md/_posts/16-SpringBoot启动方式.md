title: SpringBoot启动方式

date: 2021-05-28 15:20:36

tags: SpringBoot

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/16.jpg)

</span>

<!--more-->

# 手动打包  

> jar包默认

	mvn clean package -Dmaven.test.skip=true


> 运行war包
	
- 运行命令 
- - mvn clean package -Dmaven.test.skip=true
- 拷贝war包至web服务器tomcat的webapps中
- 将war包名称修改为ROOT.war
- 启动tomcat 
- - %TOMCAT_HOME%/bin/startup.bat


# idea 启动

* idea 直接启动入口文件

* 进入目录，输出mvn spring-boot:run

* 进入目录:mvn -install 

* * 进入 target 执行 java -jar xxx.jar -spring.profiles.active=dev;


# LINUX上tomcat启动

## jar

* [以正常项目启动](https://www.cnblogs.com/ysocean/p/6893446.html )

* java -jar XXX.jar

* * 这是最基本的jar包执行方式，但是当我们用ctrl+c中断或者关闭窗口时，程序也会中断执行。

## &

* java -jar XXX.jar &

* &代表在后台运行，使用ctrl+c不会中断程序的运行，但是关闭窗口会中断程序的运行。

## nohup

* nohup java -jar XXX.jar &

* 使用这种方式运行的程序日志会输出到当前目录下的nohup.out文件，使用ctrl+c中断或者关闭窗口都不会中断程序的执行。

## >

* nohup java -jar XXX.jar >temp.out &

* temp.out的意思是将日志输出重定向到temp.out文件，使用ctrl+c中断或者关闭窗口都不会中断程序的执行。

## 增加外部配置

```
--spring.config.location=E:\config\application-order.yml
```







