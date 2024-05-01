title: Windows-Bat脚本

date: 2021-05-25 15:20:36

tags: bat

categories: bat

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/4.jpg)

</span>

<!--more-->
# 开机自启动

    将快捷方式放入 C:\Users\xxx\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup [开始菜单>程序>启动]中

# Kill端口


    @echo off
    setlocal enabledelayedexpansion
    set /p port=write port:
    for /f "tokens=1-5" %%a in ('netstat -ano ^| find ":%port%"') do (
        if "%%e%" == "" (
            set pid=%%d
        ) else (
            set pid=%%e
        )
        echo !pid!
        taskkill /f /pid !pid!
    )
    #pause
    exit



# Hexo批处理

	@echo off 
	if "%1" == "h" goto begin 
	mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
	:begin
	E:
	cd E:\Jgit-project\hexo-site
	call hexo clean
	call hexo g
	call hexo s
	eg: call命令 可以调用另外一个bat脚本


# Nginx

	tasklist|findstr /i "nginx.exe"
	d:
	cd JJDK/nginx
	nginx.exe -c D:\JJDK\nginx\conf\nginx.conf
	pause
	exit
	/b
	
	#第二种
	taskkill /f /t /im nginx.exe
	E:
	cd /JJDK/nginx-1.19.8
	nginx.exe -c E:\JJDK\nginx-1.19.8\conf\nginx.conf
	cmd
	
	#后台运行
	@echo off 
	if "%1" == "h" goto begin 
	mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
	:begin 
	
	tasklist|findstr /i "nginx.exe"
	taskkill /f /t /im nginx.exe
	d:
	cd JJDK/nginx
	nginx.exe -c D:\JJDK\nginx\conf\nginx.conf
	cmd
	pause
	exit
	/b

# Redis

    d:
    cd JJDK/redis
    eg:脚本启动
        #redis-server.exe ./redis.windows.conf
    eg：安装服务
        redis-server.exe --service-install redis.windows.conf --loglevel verbose
        #sc delete Redis

# Kafka

    @echo off
    %1(start /min cmd.exe /c %0 :$exit)
    cd E:/JJDK/kafka
    .\bin\windows\kafka-server-start.bat  .\config\server.properties
    pause


​    

# zookeeper

    @echo off
    %1(start /min cmd.exe /c %0 :$exit)
    cd E:/JJDK/zookeeper-3.3.4/bin
    zkServer.cmd
    pause

# mysql

    E:
    cd /JJDK/mysql/bin
    mysqld.exe --defaults-file=E:\JJDK\mysql\my.ini --console
    cmd
    eg：安装服务
        mysqld --install MySQL --defaults-file="D:/JJDK/mysql/my.ini"
        #sc delete Mysql

# ftp

    E:
    cd JJDK/apache-ftpserver-1.1.1/bin
    ftpd.bat ./res/conf/ftpd-typical.xml
    cmd

#  删除无效的右键

```
按下WIN+R,然后在输入框中输入regedit 找到下面的目录 删除不需要的右键菜单

HKEY_CLASSES_ROOT\*\shellex\ContextMenuHandlers
HKEY_CLASSES_ROOT\Directory\shell
HKEY_CLASSES_ROOT\Directory\shellex\ContextMenuHandlers
HKEY_CLASSES_ROOT\Folder\shell
HKEY_CLASSES_ROOT\Folder\shellex\ContextMenuHandlers
```
# move.sh
```
#!/bin/bash

rm -rf /home/cwbb/crabc-admin/*.jar

mv /home/cwbb/crabc-admin.jar /home/cwbb/crabc-admin/

echo "移动完成"

```

# restart.sh
```
#!/bin/bash

pids=`ps -ef | grep  crabc-admin.jar | grep -v grep | awk '{print $2}'`

echo "当前进程号[]: " $pids

if [ ! -z "$pids" ]; then
  for id in $pids
  do
    kill -9 $id
    echo "killed $id"
  done
fi

ehco "" >> /home/cwbb/crabc-admin/nohup.out

nohup java -jar  /home/cwbb/crabc-admin/crabc-admin.jar &

echo "启动完成"


```

# 批量执行cmd
```
::当前目录
chcp 65001
start "ui-dolphinScheduler" cmd /c call starlink/ds/ui.bat
start "ui-maxkey-web" cmd /c call starlink/maxkey/app-ui.bat
start "ui-maxkey-mgt" cmd /c call starlink/maxkey/mgt-ui.bat
start "ui-doris" cmd /c call starlink/doris/doris-ui.bat

start "java-datax" cmd /c call starlink/datax/java.bat
start "java-magic-api" cmd /c call starlink/magic-api/java.bat
start "java-dolphinScheduler" cmd /c call starlink/ds/java.bat
start "java-maxkey-web" cmd /c call starlink/maxkey/app-java.bat
start "java-maxkey-mgt" cmd /c call starlink/maxkey/mgt-java.bat
start "java-doris" cmd /c call starlink/doris/doris-java.bat

exit
```
# 关闭窗口
```
@echo off
TASKKILL /F /IM cmd.exe /T
cmd
TASKKILL /F /FI "WINDOWTITLE eq abc"
taskkill /f /FI "WINDOWPATH eq C:\Windows\System32\cmd.exe"
cmd
```

# 右键管理员菜单

```
https://blog.csdn.net/fysuccess/article/details/106091111

打开注册表
  Win + R打开运行窗口，输入 regedit 确定后打开注册表
打开注册项
  计算机\HKEY_CLASSES_ROOT\Directory\Background\shell


在shell目录右键新建一个 runas 的项
在runas目录右键新建一个 command 项


在runas上右键，新建一个DWORD32类型,数值名称ShowBasedOnVelocityId的项目，数值 639bc8的值。
点击 command 目录，双击默认值 修改为 cmd.exe /s /k pushd "%V"

```

# 浏览器多开

```
点击谷歌浏览器,复制 粘贴  然后配置在目标  最后加上这个路径
"C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir=D:\JJDK\google\google2

--user-data-dir=D:\JJDK\google\google3
```

