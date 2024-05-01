title: 安装Mysql

date: 2021/5/26 11:44

tags: [Mysql]

categories: Mysql

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/11.jpg)

</span>

<!--more-->

## Windows下安装Mysql

### 下载

*   选择对应mysql版本下载[Mysql](http://mirrors.sohu.com/mysql/)

*   搜索zip 64位的版本进行下载      

### 配置环境变量

    MYSQL_HOME D:\JJDK\mysql

### 配置PATH

    PATH %MYSQL_HOME%\bin

### 初始化data

*   以管理员身份运行cmd 进入D:\JJDK\mysql\bin下

*   执行命令

    ``` 
    mysqld --initialize-insecure --user=mysql
    ```

*   在D:\JJDK\mysql的bin同级目录生成data目录

### 启动MySQL

    mysqld

### 登录MySQL

    mysql -u root -p

### 查询密码

    use mysql;
    select host,user,authentication_string from mysql.user;

### 修改密码

    alter user 'root'@'localhost' identified by 'root'; #5.6
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'; #8.0
    flush privileges; 

### 添加用户

```
CREATE USER 'nacos'@'%' IDENTIFIED BY 'nacos';
GRANT ALL PRIVILEGES ON *.* TO 'nacos'@'%';
FLUSH PRIVILEGES;



mysql5.x

#登录mysql
mysql -uroot -p
#创建数据库
mysql>
create database dinky;
#授权
mysql>
grant all privileges on dinky.* to 'dinky'@'%' identified by 'dinky' with grant option;
mysql>
flush privileges;
#此处用 dinky 用户登录
mysql -h fdw1 -udinky -pdinky



mysql8.x

#登录mysql
mysql -uroot -p
#创建数据库
mysql>
CREATE DATABASE dinky;
#创建用户并允许远程登录
mysql>
create user 'dinky'@'%' IDENTIFIED WITH mysql_native_password by 'dinky';
#授权
mysql>
grant ALL PRIVILEGES ON dinky.* to 'dinky'@'%';
mysql>
flush privileges;

```



### 配置权限允许访问

    1. update user set user.Host='%' where user.User='root';
    2. grant all privileges on *.* to root@'%'  identified by '123456'; 任意ip访问数据库 

### 增加my.ini配置文件

>  放在mysql安装目录下

    [mysqld] 
    # 设置mysql的安装目录，也就是刚才我们解压的目录
    basedir=D:/JJDK/mysql
    # 设置mysql数据库的数据的存放目录
    # datadir=D:/JJDK/mysql/data
    # 设置默认使用的端口
    port=3306
    # 允许最大连接数
    max_connections=200
    # 允许连接失败的次数。这是为了防止有人试图攻击数据库
    max_connect_errors=10
    # 服务端使用的字符集
    character-set-server=utf8mb4
    # 数据库字符集对应一些排序等规则使用的字符集
    collation-server=utf8mb4_general_ci
    # 创建新表时将使用的默认存储引擎
    default-storage-engine=INNODB
    # 默认使用“mysql_native_password”插件作为认证加密方式
    # MySQL8.0默认认证加密方式为caching_sha2_password
    default_authentication_plugin=mysql_native_password
    #大小写不敏感
    lower_case_table_names = 1
    
    [mysql]
    # 设置mysql客户端默认字符集
    default-character-set=utf8mb4
    
    [client]
    default-character-set=utf8mb4
    port=3306

### 后台进程启动

    D:/JJDK/mysql/bin/mysqld.exe --install Mysql --defaults-file=D:/JJDK/mysql/my.ini #新增进程
    sc delete Mysql #删除进程


## Linux下安装Mysql


### 下载

*   选择对应mysql版本下载[Mysql](https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.15-linux-glibc2.12-i686.tar)

### 安装依赖

    yum -y search libaio
    yum -y install libaio
    yum -y install numactl
    yum -y install libnuma
    yum -y install ld-linux.so.2
    yum -y install libaio.so.1
    yum -y install libnuma.so.1
    yum -y install libstdc++.so.6
    yum -y install libtinfo.so.5

### 创建mysql用户

    groupadd mysql
    useradd -r -g mysql -s /usr/local/mysql mysql

### 解压

    tar zxvf /root/mysql/mysql-8.0.15-linux-glibc2.12-i686.tar.gz
    或者
    tar -xvf /root/mysql/mysql-8.0.15-linux-glibc2.12-i686.tar
    或者
    tar -xvJf /root/mysql/mysql-8.0.15-linux-glibc2.12-i686.tar.xz

### 移动

    mv mysql-8.0.15-linux-glibc2.12-i686 mysql 
    cp mysql-8.0.15-linux-glibc2.12-i686.tar.xz /usr/local/

### 修改目录用户

    cd /usr/local/mysql #进入/usr/local/mysql 目录
    chown -R mysql:mysql ./

### 初始化
>   记住初始化密码，后面用于修改

    ./bin/mysqld  --initialize  --user=mysql  --basedir=/usr/local/mysql  --datadir=/usr/local/mysql/data --defaults-file=/etc/my.cnf

### 启动服务

    cd support-files
    ./mysql.server start

### 配置mysql环境

    vi /etc/profile
        export MYSQL_HOME=/usr/local/mysql
        export MYSQL_PATH=${MYSQL_HOME}/bin:${MYSQL_HOME}/lib
        export PATH=$PATH:/usr/local/mysql/bin
    shutdown -r now 重启下服务器或者 source /etc/profile 均可使环境变量生效

### 配置开机自启动

    cp /usr/local/mysql/support-files/mysql.server  /etc/init.d/mysql       #拷贝mysql.server 
    chmod +x  /etc/init.d/mysql                                             #添加可执行权限。
    chkconfig  --add mysql                                                  #注册启动服务
    chkconfig  --list                                                       #查看是否添加成功

### 修改密码

    按照上面windows操作就行

### 配置/etc/my.cnf

    类似 my.ini
    启动 ./bin/mysqld --user=mysql  --basedir=/usr/local/mysql  --datadir=/usr/local/mysql/data --defaults-file=/etc/my.cnf

# Docker启动

    docker run --name mysql1 --env MYSQL_ROOT_HOST=172.17.%.% 
    --env MYSQL_ROOT_PASSWORD=root -v $PWD/mysql_data:/var/lib/mysql -p 3333:3306 -d mysql/mysql-server:5.7

# mysql 8 不支持大小写
```
find / -iname php.ini -type f


java -jar dbapi-standalone-3.2.1.jar


rm -rf /var/lib/mysql

mkdir -p /var/lib/mysql


chown mysql:mysql /var/lib/mysql


/usr/sbin/mysqld --initialize --user=root --lower-case-table-names=1


systemctl stop mysql.service

service mysql restart



grep "A temporary password" /var/log/mysql/error.log


mysql -p -uroot

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';


use mysql 

update user set host = '%' where user = 'root';

flush privileges;



create user 'user'@'%' identified by 'user@123';


GRANT ALL PRIVILEGES ON *.* TO 'user'@'%'  WITH GRANT OPTION;


ALTER USER 'user'@'%' IDENTIFIED WITH mysql_native_password BY 'user@123';

flush privileges;


unset PYTHONPATH
unset PYTHONHOME

```
# 用户
```
ALTER user root@'localhost' identified by '8a2e81e474acd549'; 8a2e81e474acd549

create user 'user'@'%' identified with mysql_native_password by 'user@123';

grant all on *.* to 'user'@'%' with grant option;

flush privileges;
```
# dump
```
source xx.sql

mysqldump -uroot -p8a2e81e474acd549  --add-drop-table --all-databases > /root/all.sql

mysqldump -uroot -p8a2e81e474acd549  --add-drop-table xqmall > /root/xqmall.sql

mysqldump -uroot -p8a2e81e474acd549  --add-drop-table nacos > /root/nacos.sql
```
