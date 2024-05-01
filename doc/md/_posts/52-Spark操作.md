title: Spark操作

date: 2021-05-25 15:20:36

tags: Hadoop

categories: Hadoop

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/52.jpg)

</span>

<!--more-->

# Sprak

* sprak命令
```
spark shell
```

* 特点
```
轻
核心代码只有3万行
快
对小数据集可达到亚秒级
```

* 核心概念RDD
```
Resilient Distributed Datasets 即弹性分布式数据集,是一个只读的,可分区的分布式数据集
RDD 默认存储在内存,当内存不足时,溢写到磁盘
RDD数据以分区形式在集群中存储
RDD具有血统机制(Lineage),发生数据丢失时,可快速进行数据恢复
```

```
shuffle:把相同数字放在一台服务器上

窄依赖和宽依赖

窄依赖: 子分区和父分区 1对1
宽依赖: 子分区来自于多个父分区

创建 - 创建数据
转换 - 分区
控制 - 缓存
行动 - reduce等操作
```
* 数据格式

![](/images/big/data.jpg)

* RDD操作
```
#spark-shell

#从本地文件创建
val line  = sc.textFile("file:///user/gg.txt")
#从hdfs创建
val line = sc.textFile("hdfs://hacluster/user/gg/tt.txt")
#集合创建
val array = Array(1,2,3,4,5)
val list = List(1,2,3,4,5)
#转换成rdd数据
val rdd1 = sc.parallelize(array)
#对rdd1每一个元素乘以2排序
val rdd2 = rdd1.map(_ * 2).sortBy(x=>x,true)
#过滤出大于等于5的元素
val rdd3 = rdd2.filter(_ >= 5)
#显示
rdd3.collect

#flatMap
rdd1里面的每一个元素先切分在压平
val rdd1 = sc.parallelize(Array("a b c","d e f","h i j"))
val rrd2 = rdd1.flatMap(_.split(" "))
rrd2.collect

#交集 并集
val rdd1 = sc.parallelize(Array(1,2,3,4,5))
val rdd2 = sc.parallelize(Array(1,3,4,5))

#并集
val rdd3 = rdd1.union(rdd2)
rdd3.collect

#交集
val rdd3 = rdd1.intersection(rdd2)
rdd3.collect

#去重
val rdd3 = rdd3.distinct.collect
rdd3.collect

#join
val rdd1 = sc.parallelize(Array({"tom",1},{"li",3},{"wang",5}))
val rdd2 = sc.parallelize(Array({"tom2",2},{"tom",1},{"li2",4},{"wang2",56}))
val rdd3 =  rdd1.join(rdd2)
rdd3.collect

#并集
val rdd3 =  rdd1.union(rdd2)
rdd3.collect

#按key进行分组
val rdd4 =  rdd3.groupByKey
rdd4.collect

#cogroup
多个迭代器
val rdd4 =  rdd1.cogroup(rdd2)
rdd4.collect

#reduce
val rdd1 = sc.parallelize(Array(1,2,3,4,5))
val rdd2 = rdd1.reduce(_ + _)
rdd2

#reduceByKey sortByKey
rdd1.reduceByKey(_ + _)

val rdd5 = rdd3.map(t=>(t._2,t._1)).sortByKey(false).map(t=>(t._2,t._1))
rdd5.collect


#惰性机制 
加载不存在的文件  只有collect真正执行才会报错

```
* dataFrame操作
```
linux本地创建文件gg.txt
1 zhangsan 20
2 lsi 28
3 wangwu 44
4 sh 22
5 dd 44
6 kobe 22
#上传
hdfs dfs -put gg.txt /user/gg/
#加载文件
val lineRDD = sc.textFile("/user/gg/gg.txt").map(_.split(" "))
#创建表
case class Person(id:Int,name:String,age:Int)
#转换关联RDD
val personRDD = lineRDD.map(x=>Person(x(0).toInt,x(1),x(2).toInt))
#rdd转换成dataframe
val personDF = personRDD.toDF
#查看结果
personDF.show

```

* spark.sql

```
#注册临时表才能使用sparkSQL
personDF.registerTempTable("Person")
#查询
spark.sql("desc Person").show
spark.sql("select * from Person").show
```

* dataSQL
```
#加载数据
val ds1 = spark.createDataset(1 to 5)
ds1.show

val ds1 = spark.createDataset(sc.textFile("/user/gg.txt"))
ds1.show

case class Person2(id:Int,name:String,age:Int)
val data = List(Person2(10001,"a",20),Person2(10003,"b",30))
val ds3 = data.toDS
ds3.show

通过dataFrame生成的数据,通过as转换dataSet
val ds4 personDF.as[Person2]

查询
ds4.filter(col("age")>=25).show

```
* 小结
```

dataFrame 加载 .toDF

dataFrame 通过 as 变成dataSet

dataFrame 通过 registerTempTable  变成 sparkSQL

```

* 传输组件 
```
flume 采集日志
loader 数据库传输
kafka 消息队列

```



