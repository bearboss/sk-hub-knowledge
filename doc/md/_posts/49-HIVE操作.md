title: HIVE操作

date: 2021-05-25 15:20:36

tags: Hadoop

categories: Hadoop

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/49.jpg)

</span>

<!--more-->

# HIVE操作

* 进入HVIE
```
beeline
```
* HIVE创建托管(内部)表
```
create table myhive(name string,gender string,age int) row format delimited fields terminated by ',' stored as textfile;
```

* HIVE创建外部表
```
create external table myhive2(name string,gender string,age int) row format delimited fields terminated by ',' stored as textfile;
```

* 载入hdfs数据
```
vi vi.txt

tom,male,10
jack,female,22


hdfs dfs -put vi.txt /user/gg/

在hive-beeline里面

load data inpath '/user/gg/vi.txt' into table myhive02;

查看
select * from myhive2;
```

* 模糊查询表
```
show tables like 'myhive*';
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






