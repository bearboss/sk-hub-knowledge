title: 搭建ftp

date: 2021-05-29 15:20:36

tags: ftp

categories: ftp

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/25.jpg)

</span>

<!--more-->

# Windows 

## apache-ftpserver-1.1.1

 [下载](http://mina.apache.org/ftpserver-project/download_1.1.1.html)

## 配置

### 配置用户

*  users.properties 创建两个访问账户

    ```
    # Password is "admin"
    ftpserver.user.admin.userpassword=admin
    ftpserver.user.admin.homedirectory=E:/organic-ftp/
    ftpserver.user.admin.enableflag=true
    ftpserver.user.admin.writepermission=true
    ftpserver.user.admin.maxloginnumber=0
    ftpserver.user.admin.maxloginperip=0
    ftpserver.user.admin.idletime=0
    ftpserver.user.admin.uploadrate=0
    ftpserver.user.admin.downloadrate=0
    
    # ftpserver.user.anonymous.userpassword=root
    # ftpserver.user.anonymous.homedirectory=E:/Jproject/spring-organic-food/organic-file/ftp/
    # ftpserver.user.anonymous.enableflag=true
    # ftpserver.user.anonymous.writepermission=false
    # ftpserver.user.anonymous.maxloginnumber=20
    # ftpserver.user.anonymous.maxloginperip=2
    # ftpserver.user.anonymous.idletime=300
    # ftpserver.user.anonymous.uploadrate=4800
    # ftpserver.user.anonymous.downloadrate=4800
    #密码 配置新的用户(用户名:hlf 密码:hlf)
    
    ftpserver.user.hlf.userpassword=hlf
    #主目录
    ftpserver.user.hlf.homedirectory=E:/Jproject/spring-organic-food/organic-file/
    #当前用户可用
    ftpserver.user.hlf.enableflag=true
    #具有上传权限
    ftpserver.user.hlf.writepermission=true
    #最大登陆用户数为20
    ftpserver.user.hlf.maxloginnumber=20
    #同IP登陆用户数为2
    ftpserver.user.hlf.maxloginperip=2
    #空闲时间为300秒
    ftpserver.user.hlf.idletime=300
    #上传速率限制为480000字节每秒
    ftpserver.user.hlf.uploadrate=48000000
    #下载速率限制为480000字节每秒
    ftpserver.user.hlf.downloadrate=48000000
    
    ```

* ftpd-typical.xml

    ```
    <server xmlns="http://mina.apache.org/ftpserver/spring/v1"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="
           http://mina.apache.org/ftpserver/spring/v1 http://mina.apache.org/ftpserver/ftpserver-1.0.xsd	
           "
        id="myServer">
        <listeners>
            <nio-listener name="default" port="2121">
                <ssl>
                    <keystore file="./res/ftpserver.jks" password="password" />
                </ssl>
                <data-connection idle-timeout="60">
                    <active local-port="8901" /><!--主动端口-->
                    <passive ports="8901" /><!--被动端口-->
                </data-connection>
            </nio-listener>
        </listeners>
        <file-user-manager file="./res/conf/users.properties" encrypt-passwords="clear"/>
    </server>
    ```
## 启动
    ```
    E:
    cd JJDK/apache-ftpserver-1.1.1/bin
    ftpd.bat ./res/conf/ftpd-typical.xml
    cmd
    ```
    
# Linux

## 卸载vsftpd

    sudo yum remove vsftpd 

## 安装vsftpd

    sudo yum -y install vsftpd

## 创建一个文件夹用来当作ftp得仓库
    cd /
    sudo mkdir ftpfile
    
## 创建一个用户,仅对文件夹有上传权限,又没有登陆权限

    sudo useradd ftpuser -d /ftpfile/ -s /sbin/nologin
    //赋值权限
    sudo chown -R ftpuser.ftpuser /ftpfile/
    //重置改用户的密码
    sudo passwd ftpuser
    
## 配置ftp服务器

### 配置ftp服务器器指向文件夹,以及配置用户
> sudo vim /etc/vsftpd/vsftpd.conf
    
    //放开  连接成功时的欢迎信息
    ftpd_banner=Welcome to blah FTP service.
    //新增仓库地址
    local_root=/ftpfile
    anon_root=/ftpfile
    //新增行 设置使用时间
    use_localtime=yes
    //新增行 设置被动传输接口的范围
    pasv_min_port=61000
    pasv_max_port=62000
    //修改行 匿名访问为NO
    anonymous_enable=NO
    //放开 
    chroot_list_enable=YES
    //放开
    chroot_list_file=/etc/vsftpd/chroot_list

### 创建配置用户的chroot_list文件

    cd /etc/vsftpd/
    sudo vim chroot_list
    //增加内容  上面配置的用户的用户名
    ftpuser
    
### 重启vsftpd

    sudo service vsftpd restart
    
### 编辑防火墙
> sudo vim /etc/sysconfig/iptables

    //新增行
    #vsftpd
    -A INPUT -p TCP --dport 61001:62000 -j ACCEPT
    -A OUTPUT -p TCP --sport 61001:62000 -j ACCEPT
    -A INPUT -p TCP --dport 20 -j ACCEPT
    -A OUTPUT -p TCP --sport 20 -j ACCEPT
    -A INPUT -p TCP --dport 21 -j ACCEPT
    -A OUTPUT -p TCP --sport 21 -j ACCEPT

### 重启防火墙

    sudo service iptables restart
    
### 重启vsftpd

    sudo service vsftpd restart

### 修改系统文件  以防匿名用户无法创建文件

    sudo vim /etc/selinux/config 
    //修改
    SELINUX=disable
    //刷新生效
    sudo setenforce 0