title: MapReduce操作

date: 2021-05-25 15:20:36

tags: Hadoop

categories: Hadoop

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/51.jpg)

</span>

<!--more-->

# MapReduce操作计数例子

* 
```
#创建一个文件
vi tt.txt
hadoop hive hadoop hbase spark hive hadoop spark
#上传
hdfs dfs -put tt.txt /user/gg/

#执行jar包程序
yarn jar /xxx/mapreduce.jar wordcount /user/gg/tt.txt /user/gg/output
```
* 得到结果
```
hdfs dfs -cat /user/gg/output/part-r-00000

doop	1
hadoop	2
hbase	1
hive	3
spark	2

```

