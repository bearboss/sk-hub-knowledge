title: HDFS操作

date: 2021-05-25 15:20:36

tags: Hadoop

categories: Hadoop

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/48.jpg)

</span>

<!--more-->

# HDFS 常用操作

* 使用命令操作mrs组件之前都需要设置环境
```
source /opt/client/bigdata_env
```

* help命令
```
hdfs dfs -help
```

* ls帮助命令
```
hdfs dfs -help ls
```

* ls命令
```
hdfs dfs -ls /
```

* mkdir命令
```
hdfs dfs -mkdir /user/gg 
```

* put上传命令
```
vi vi.txt
hdfs dfs -put vi.txt /user/gg 
```

* cat命令
```
hdfs dfs -cat /user/gg/vi.txt
```

* text命令
```
以字符串形式打印一个文件内容
hdfs dfs -text /user/gg/vi.txt
```

* moveFromLocal命令
```
从本地剪切文件去hdfs
vi vi2.txt
hdfs dfs -moveFromLocal vi2.txt /user/gg/
```

* appendToFile命令
```
linux追加到hdfs
vi vi3.txt
hdfs dfs -appendToFile vi3.txt /user/gg/vi2.txt
```

* cp命令
```
hdfs上拷贝
hdfs dfs -cp /user/gg/vi2.txt /user/yy/
```

* mv命令
```
hdfs上移动
hdfs dfs -mv /user/gg/vi2.txt /user/yy/
```

* copyToLocal命令
```
从hdfs下载到本地
hdfs dfs -copyToLocal /user/gg/vi.txt
```

* gitmerge命令
```
从hdfs合并多个文件下载到本地
hdfs dfs -gitmerge /user/gg/* ./abc.txt
```

* rm命令
```
hdfs删除
hdfs dfs -rm /user/gg/vi2.txt
```

* 撤销删除命令
```
hdfs dfs -mv /user/root/.Trash/Current/user/gg/vi2.txt /user/gg/
``` 

* df命令
```
统计系统可用空间信息
hdfs dfs -df -h /
``` 

* du命令
```
统计文件夹大小
hdfs dfs -du -s -h /user/gg/
``` 

* count命令
```
统计指定目录文件节点数量
hdfs dfs -count -v /user/gg/
``` 

* 回收站
```
hdfs dfs -ls -v  /user/root/.Trash/Current/user/gg/
``` 




