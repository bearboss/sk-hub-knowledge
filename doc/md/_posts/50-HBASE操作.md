title: HBASE操作

date: 2021-05-25 15:20:36

tags: Hadoop

categories: Hadoop

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/50.jpg)

</span>

<!--more-->

# hbase操作

* 进入hbase
```
hbase shell
```
* hbase创建表
```
表名 - 列族名
create 'gg_table','stu'
```

* 增加数据
```
表名 - 主键-列族-列-值
put 'gg_table','001','stu:name','tom'
put 'gg_table','001','stu:gender','male'
put 'gg_table','001','stu:age','20'
put 'gg_table','002','stu:name','lilei'
put 'gg_table','002','stu:gender','female'
put 'gg_table','002','stu:age','19'
put 'gg_table','003','stu:name','zhangsan'
put 'gg_table','003','stu:gender','male'
put 'gg_table','003','stu:age','22'
```

* 查看
```
scan 'gg_table'
```

* scan 查询表
```
查询所有
scan 'gg_table'

查询列族为stu的数据
scan 'gg_table',{COLUMNS=>'stu'}

查询列族为stu-列为name的数据
scan 'gg_table',{COLUMNS=>'stu:name'}
```

* get 查询表
```
查询行键为001
get 'gg_table','001'

查询行键为001 列族为stu 列名为name
get 'gg_table','001','stu:name'
```

* 指定条件查询数据
```
起始行键001 ,最多两个行键 结束是002 ,前面包含后面不包含
scan 'gg_table',{STARTROW=>'001','LIMIT'=>2,STOPROW=>'004'}
scan 'gg_table',{STARTROW=>'001','LIMIT'=>2,STOPROW=>'004',COLUMNS=>'stu:name'}
```

* 解释
```
除了列(COLUMNS)修饰词,Hbase还支持LIMIT(限制查询结果行键数)
STARTROW(ROWKEY起始行.会根据这个key定位到region,再向后扫描),
STOPROW(结束行) TIMERANGE(限定时间戳范围)
VERSION(版本数)
FILTER(按条件过滤行)等
```

* 查询多版本数据
```
查询到最新的数据
put 'gg_table','001','stu:name','mm'
put 'gg_table','001','stu:name','mm1'
put 'gg_table','001','stu:name','mm2'
#多版本查询
get 'gg_table','001',{COLUMNS=>'stu',VERSIONS=>5}
#查询系统版本信息
desc 'gg_table'
#修改版本
alter 'gg_table',{NAME=>'stu',VERSION=>5}
#插入数据查询  会看见多版本的数据
#scan只会显示最新的数据,所以需要用get查询
```

* 删除
```
put 'gg_table','004','stu:name','jk4'
delete 'gg_table','004','stu:name'
delete 'gg_table','004'
```

* 删除表
```
disable 'gg_table'
drop 'gg_table'
```


* 创建预分region表
```
Hbase默认建表时只有一个region,这个region的rowkey是没有边界的,即没有startKey和endKey
在数据写入时,所有的数据都会写入这个默认的region,随着数量的增加,此region不能承受数量(10G)会进行split,
分成2个region,在此过程中会产生两个问题:
1.数据往一个region写,会有写热点问题
2.region split会消耗I/0资源
由此,我们可以创建表时,创建多个空的region,并确定每个region的起始和终止rowkey
这样rowkey设计能均匀命中region,split的概率也会降低
hbase提供了两种pre-split算法,HEXStringSplit和UniformSplit 
前者适用于十六进制的rowkey,后者适用于随机字节数组的rowkey
```

```
以rowKey切分,随机分为4个region
UniformSplit 适用于十六进制字符的rowKey

create 'gg_table_2','stu2',{NUMREGION=>4,SPLITALGO=>'UniformSplit'}

```

* 指定startKey和endKey
```
create 'gg_table_3','stu3',SPLITS=>['001','002'.'003']
```


* Filter过滤器
```
scan 'gg_table',{FILTER=>"ValueFilter(=,'binary:20')"}
scan 'gg_table',{FILTER=>"ValueFilter(=,'binary:lilei')"}

scan 'gg_table',FILTER=>"ColumnPrefixFilter('name') AND ValueFilter(=,'binary:lilei')"
```






