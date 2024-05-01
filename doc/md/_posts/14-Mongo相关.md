title: Mongo相关

date: 2021-05-28 15:20:36

tags: Mongo

categories: Mongo

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/14.jpg)

</span>

<!--more-->

# Windows 安装

## 下载

*   选择对应mysql版本下载[Mysql](https://www.mongodb.com/)

*   搜索64位的版本进行下载      
    
## 解压与创建

* 随意创建自己喜欢的路径，D:\JJDK\mongo

* 在D:\JJDK\mongo下解压下载的zip文件

* 然后分别建立db,log两个文件夹，log下创建log.log

## 启动服务

* cd D:\JJDK\mongo\bin

* mongod --dbpath D:\JJDK\mongodb\data --logpath D:\JJDK\mongodb\log\log.log --logappend

## 客户端连接

*   mongo 
    ```
    use admin 
    db.createUser({ user: "root", pwd: "root", roles: [
        { role:"userAdminAnyDatabase", db: "admin" },
        { role:"dbAdminAnyDatabase", db: "admin" },
        { role:"readWriteAnyDatabase", db: "admin" }
    ] 
    })
    use juooo
    db.auth("root","root");
    db.createUser({ user: "root", pwd: "root", roles: [{ role: "dbOwner", db: "juooo" }] })
    ```
*   创建用户密码，创建admin和juooo库
				
## 以auth启动

    D:\JJDK\mongo\bin\mongod.exe --dbpath D:\JJDK\mongo\data --logpath D:\JJDK\mongo\log\log.log --logappend --auth --service

## 后台进程启动

    sc create MongoDB binPath= "D:\JJDK\mongo\bin\mongod.exe --dbpath D:\JJDK\mongo\data --logpath D:\JJDK\mongo\log\log.log --logappend --auth --service"
    sc delete MongoDB

## 修改端口

    --port=27017 --fork

# Linux安装

## 下载解压
    
    wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-4.2.5.tgz
    tar -zxvf mongodb-linux-x86_64-rhel70-4.2.5.tgz
    mv mongodb-linux-x86_64-rhel70-4.2.5/ /usr/local/mongodb
    
    mkdir  -p  /usr/local/mongodb/data
    mkdir  -p  /usr/local/mongodb/logs
    
    ln -s /usr/local/mongodb/bin/mongod mongod
    ln -s /usr/local/mongodb/bin/mongo 

## 启动并创建数据库
>   参照windows创建数据库命令

    usr/local/mongodb/bin/mongod --dbpath=/usr/local/mongodb/data --logpath=/usr/local/mongodb/logs/log.log

## 权限启动

    nohup /usr/local/mongodb/bin/mongod --dbpath=/usr/local/mongodb/data --logpath=/usr/local/mongodb/logs/log.log --auth --port=27017 --fork
    
## 开机自启动

>   新增sh脚本放在根目录的shell下面mongod_start.sh

    #!/bin/bash
    # pkill -9 mongod;
    /usr/local/mongodb/bin/mongod --shutdown --dbpath /usr/local/mongodb/data/;
    nohup /usr/local/mongodb/bin/mongod --dbpath=/usr/local/mongodb/data --logpath=/usr/local/mongodb/logs/log.log --auth --port=27017 --fork >  /tmp/mongod.log 2>&1 & 

>   设置权限

    chmod 777 mongod_start.sh
    vim /etc/rc.d/rc.local
        文件后面追加 sh /shell/mongod_start.sh
    chmod +x /etc/rc.d/rc.local        
        
# 权限介绍

- 数据库用户角色（Database User Roles）

- - read：授予User只读数据的权限
- - readWrite：授予User读写数据的权限

- 数据库管理角色（Database Administration Roles）：

- - dbAdmin：在当前dB中执行管理操作
- - dbOwner：在当前DB中执行任意操作
- - userAdmin：在当前DB中管理User

- 备份和还原角色（Backup and Restoration Roles）：

- - backup
- - restore

- 跨库角色（All-Database Roles）：

- - readAnyDatabase：授予在所有数据库上读取数据的权限
- - readWriteAnyDatabase：授予在所有数据库上读写数据的权限
- - userAdminAnyDatabase：授予在所有数据库上管理User的权限
- - dbAdminAnyDatabase：授予管理所有数据库的权限

- 集群管理角色（Cluster Administration Roles）：

- - clusterAdmin：授予管理集群的最高权限
- - clusterManager：授予管理和监控集群的权限，A user with this role can access the config and local databases, which are used in 	sharding and replication, respectively.
- - clusterMonitor：授予监控集群的权限，对监控工具具有readonly的权限
- - hostManager：管理Server

# SpringBoot整合Mongo
    
>   pom.xml

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-mongodb</artifactId>
    </dependency>
	
> application.yml

    spring.data.mongodb.uri: mongodb://root:root@localhost:27017/juooo

> 查询操作见日志

- [springboot使用mongo查询](https://blog.csdn.net/u011161786/article/details/71512952)

# 彩蛋

* 如果启动改不了就删除log文件
* 看看权限问题











