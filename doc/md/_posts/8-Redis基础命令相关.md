title: Redis基础命令相关

date: 2021/5/28 11:44

tags: Redis

categories: Redis

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/8.jpg)

</span>

<!--more-->

# Redis基本操作

## 基本数据结构

### KV

	set         #设置
	get         #获取
	del         #删除
	incr        #+1 
	decr        #-1
	incrby 5    #+5
	decrby 5    #-5
	append      #追加
	            #eg:如果 key 已经存在并且是一个字符串，
	                APPEND 命令将 value 追加到 key 原来的值的末尾。
                    如果 key 不存在， 
                    APPEND 就简单地将给定 key 设为 value ，
                    就像执行 SET key value 一样。]
	
### Hash

	hset myhash name mx             #单个设置
	hget myhash name                #单个获取
	hmset myhash2 name mx age 18    #多个设置
	hmget myhash2 name age          #多个获取
	hgetall myhash2                 #全部获取
    hdel                            #删除 
    hdel myhash2 name age           #指定删除
    del myhash2                     #删除
	hincrby myhash2 age 5           #+5
	hdecrby myhash2 age 5           #-5
	hexists myhash2 name            #判断存在 返回0或者1
	hlen myhash                     #数量
	hkeys myhash                    #获取keys
	hvalues myhash                  #获取values
	
### List

	lpush                       #左边推入  lpush mylist 1 2 3
	rpush                       #右边推入  rpush mylist a b c
	lrange                      #查看内容  lrange mylist 0 -1
	lpop myliist                #左边弹出
	rpop mylist                 #右边弹出
	llen mylist                 #查看长度
	lpushx                      #存在的list才插入，不存在就返回0
	rpushx                      #同上
	lrem mylist 2 3             #从头到尾删除2个3
	lrem mylist -2 1            #从尾到头删除2个1
	lrem mylist 0 2             #删除全部2
	lset mylist 3 mm            #第三个脚表设置mm
	linsert mylist before b 11  #第一个b之前插入11 
	linsert mylist after b 22   #第一个b之后插入22
	rpoplpush mylist5 mylist6   #将list5弹出压入list6
	
### Set
>不允许出现重复的数据，只保留一份

    sadd myset abc              #添加
    srem myset a b              #删除
    smembers myset              #查看
    sismember myset a           #a是否在集合中 返回0或者1
    sdiff mya1 myb1             #差集运算
    sinter  mya1 myb1           #交集运算
    sunion  mya1 myb1           #并集运算
    scard myset                 #得到set中的数量
    srandmember myset           #随机获取集合中数量
    sdiffstore  my1  mya1 myb1  #将mya1 myb1 不同的存在my1中
    sinterstore my2  mya1 myb1  #将mya1 myb1 相同的存在my2中
    sunionstore my3  mya1 myb1  #将mya1 myb1 并集的存在my3中

### SortedSet
>不允许出现重复的数据，只保留一份
		
    zadd mysort 70 zs 80 li 90 ww                   #添加
    zadd 100 zs                                     #覆盖之前的zs 
    zscore mysort zs                                #获取分数
    zcard mysort                                    #数量
    zrem mysort tom ww                              #删除
    zrange mysort 0 -1                              #从小到大查看元素
    zrange mysort 0 -1 withscores                   #查看分数
    zrevrange mysort 0 -1                           #从大到小
    zrevrange mysort 0 -1 withscores                #从大到小分数排序
    zremrangebyrank mysort 0 4                      #按照排名范围来删除
    zremrangebyscore mysort 80                      #100 按照分数删除
    zrangbyscore myscore 0 100 withscore            #返回分数范围的成员并排序返回
    zrangbyscore myscore 0 100 withscore limit 0 2  #返回分数范围的成员并排序返回限制
    zincrby myscore 3 ls                            #增加分数
    zsscore mysorr ls                               #显示李四的分数
    zcount mysort  80 90                            #获取分数范围的个数
		
## Keys

	keys *                      #所有keys
	keys my?                    #查看所有my的key
	exists my1                  #key是否存在
	rename company new company  #更改键
	expire company 1000         #设置1000秒过时
	ttl company                 #剩余时间
	type company                #获取类型
	
## Redis新特性
	
    select 1        #选择1号数据库
	move myset 1    #移动myset这个key 到1号库
	multi           #开启事务
	exec            #提交
	discard         #回滚

## Redis 持久化

	#RDB方式（100多行左右--）
        save 900 1
        save 300 10
        ...
        dbfilename dump.rdb #保存文件名
        ..
        优势：只会保留一个文件，容易备份，性能最大化
        劣势：容易丢失数据（每过几十秒才保存数据）
	#AOF方式（appendonly yes 开启）
        策略： appendfsync always(每次修改都保存)
        ..
        优势：append的形式，不易毁坏之前的数据
        劣势：AOF要大，运行效率比RDB低
        把aof打开的最后的flushall删除，重新开启reids即可还原数据
        
	#无持久化

	#同时使用RDB和AOF


# Protostuff序列化

## Jar

    <!--依赖jar包-->
    <dependency>
       <groupId>redis.clients</groupId>
       <artifactId>jedis</artifactId>
       <version> 2.9.0 </version>
    </dependency>
    <dependency>
       <groupId>com.dyuproject.protostuff</groupId>
       <artifactId>protostuff-core</artifactId>
       <version>1.1.3</version>
    </dependency>
    <dependency>
       <groupId>com.dyuproject.protostuff</groupId>
       <artifactId>protostuff-runtime</artifactId>
       <version>1.1.3</version>
    </dependency>

## Test

    public class jedis {

        private static final String ip = "127.0.0.1";
        private static final int port = 6379;
    
        private static JedisPool jedisPool;
        private static RuntimeSchema<Page> schema = RuntimeSchema.createFrom(Page.class);
        public jedis() {
            jedisPool = new JedisPool(ip, port);
        }
    
        //设置数据进入redis
        public  String setRedis( Page page ){
            Jedis jedis  = jedisPool.getResource();
            String key = "key:" + page.getId();
            int timeout = 60 * 60; // 1小时
            //把对象实例化
            byte[] bytes = ProtostuffIOUtil.toByteArray( page,schema, 
            LinkedBuffer.allocate(LinkedBuffer.DEFAULT_BUFFER_SIZE));
            //设置redis
            String result = jedis.setex(key.getBytes(),timeout,bytes);
            jedis.close();
            return result;
        }
        /**
         * 从redis取数据
         */
        public  Page getRedis(String id){
            Jedis jedis  = jedisPool.getResource();
            String key = "key:" +id;
            byte[]  bytes = jedis.get(key.getBytes());
            //把字节数组序列化返回成实体
            if (bytes != null) {
                Page page = schema.newMessage();
                ProtostuffIOUtil.mergeFrom(bytes, page, schema);
                return page;
            }
            jedis.close();
            return null;
        }
    
        public static void main(String[] args){
            jedis j = new jedis();
            Page m = j .getRedis("1");
            if(m!=null){
                System.out.println(m);
            }else{
                Page p = new Page();
                p.setId(1);
                p.setName("小明");
                p.setDetail("小明今天去爬山");
                p.setTime(String.valueOf(new Date()));
                j.setRedis(p);
            }
        }
    }
