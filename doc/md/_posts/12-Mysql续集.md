title: Mysql续集

date: 2021-05-28 15:20:36

tags: Mysql

categories: Mysql

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/12.jpg)

</span>

<!--more-->
# 删除查询数据
```
delete  from t_ds_task_definition_log where id in (
select id from (
  select min(id) as id
  from t_ds_task_definition_log group by code,version having count(*) >1
  ) as a
)


delete  from t_ds_task_definition where id in (
select id from (
  select min(id) as id
  from t_ds_task_definition group by code,version having count(*) >1
  ) as a
)

```
# 更新
```
update litemall_order as a join (select order_id as id,count(order_id) as count from litemall_order_goods group by order_id) as b set a.comments = b.count where a.id = b.id;
```
# SQL树状处理
```
JSON_ARRAY  可以换成 JSON_ARRAY_CGG试试
WITH data_ref AS (    
    SELECT 
    	a.group_name,
        a.area_name ,
        a.reach_name,     
        JSON_ARRAY(GROUP_CONCAT(JSON_OBJECT('value', a.name, 'disabled', true))) as childrens    
    FROM     
        dim_org_project_info_for_crm a  
    GROUP BY     
        a.group_name, a.area_name, a.reach_name    
),

area_ref AS (
	SELECT 
		a.group_name,
		a.area_name,
		JSON_ARRAY(GROUP_CONCAT(JSON_OBJECT('value', a.reach_name, 'childrens', a.childrens))) as childrens  
	from
	    data_ref a
	group by
	    a.group_name,area_name
),

group_ref AS (
	SELECT 
		a.group_name,
		JSON_ARRAY(GROUP_CONCAT(JSON_OBJECT('value', a.area_name, 'childrens', a.childrens))) as childrens  
	from
	    area_ref a
	group by
	    a.group_name
)
select JSON_OBJECT(     
            'value', a.group_name,    
            'childrens', a.childrens ) from group_ref a
```
# jdbc 时差问题

    jdbc:mysql://127.0.0.1:3306/order?useTimezone=true&serverTimezone=Asia/Shanghai&characterEncoding=utf8&nullCatalogMeansCurrent=true&useSSL=true

# 设置时间默认值

    ALTER TABLE `matter_public_area`
    MODIFY COLUMN `created_at`  datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
    MODIFY COLUMN `updated_at`  datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间' ,
    MODIFY COLUMN `is_deleted`  tinyint(1) NULL DEFAULT 0 COMMENT '是否删除';

# 时间格式化

    SELECT FROM_UNIXTIME(date, '%Y-%c-%d %h:%i:%s' ) as post_date ,   
    date_format(NOW(), '%Y-%c-%d %h:%i:%s' ) as post_date_gmt   
    FROM `article`  where outkey = 'Y' 

# 传入变量
```
select substring_index(substring_index(a.outIds, ',', b.id + 1) ,',', -1) as outIds
from(select "1,2,3,4,5,6,7,8,9,0,1,2,212,21,32,32,44,4" as outIds) a join matter_help_id b on b.id < LENGTH(a.outIds) - LENGTH(REPLACE(a.outIds,',','')) + 1;


CREATE TABLE cent_order.`matter_help_id` (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


TRUNCATE cent_order.matter_help_id;
DROP PROCEDURE IF EXISTS initIndex;
DELIMITER $$
create procedure initIndex(in row_num int)
begin 
	declare id varchar(32);
	declare counter int default 0;
	set @pre_sql = "insert into cent_order.matter_help_id(id) values";
	set @exec_sql = @pre_sql;
	repeat
		set @exec_sql = concat(@exec_sql,"(",counter,"),");
		set counter=counter+1;
		if counter mod 10000 = 0 or counter >= row_num then
			set @exec_sql = substring(@exec_sql, 1, char_length(@exec_sql)-1);
			prepare stmt from @exec_sql;
			execute stmt;
			deallocate prepare stmt;
			if counter < row_num then
				set @exec_sql = @pre_sql;
			end if;
		end if;
		until counter >= row_num
	end repeat;
end$$
DELIMITER ;
#先整个10万条 后面不够了再加 - 大概需要执行50秒
call initIndex(100000);
DROP PROCEDURE IF EXISTS initIndex;
```

# 锁

    乐观锁 - 使用版本号控制 update shop set count =46 where count = 47 
    悲观锁 - for update 

# 存储过程

## 查找所有存储过程

     show procedure status;

## 查看单个

    show create procedure xx;

## 删除

    drop procedure xx;

## 创建简单的储存过程

    //默认;变成$$结尾
    //in表示输入
    //out 表示输出
    //调用用call
    //变量是@开始
    delimiter $$;
    create procedure p4(in pid int,out name varchar(30))
    begin
        select * from seckill where id = pid;
    end
    //创建结束开始调用
    call p4(20009,@name);
    select @name;

## 复杂的存储过程

### 定义变量: 

     语句中定义：	
        DECLARE insert_count int DEFAULT 0;//定义一个insert_count 标量为0，相当于类的成员变量
        set r_result = -1;让输出变量等于-1；
     语句外定义：
        set @r_result=-3;

### if判断语句：	

    IF (insert_count = 0) THEN
      ROLLBACK;
      set r_result = -1;
    ELSEIF(insert_count < 0) THEN
      ROLLBACK;
      SET R_RESULT = -2;
    ELSE
    xxx
    END IF;

### 插入小技巧ignore 重复插入返回0；

     insert ignore into success_killed (seckill_id,user_phone,create_time) values (v_seckill_id,v_phone,v_kill_time);

### 统计插入正确的条数 并赋值给变量

    select row_count() into insert_count;	

### 标签对应

    begin-end
    if - endif;


​	

## 秒杀执行存储过程

    DELIMITER $$ -- console ; 转换为 $$
    -- 定义存储过程
    -- 参数: in 输入参数; out 输出参数
    -- row_count():返回上一条修改类型sql(delete,insert,update)的影响行数
    -- row_count: 0:未修改数据; >0:表示修改的行数; <0:sql错误/未执行修改sql
    --seckill表示数据库名字，execute_seckill表示存储过程名
    
    CREATE PROCEDURE `seckill`.`execute_seckill`
      (in v_seckill_id bigint,in v_phone bigint,
        in v_kill_time timestamp,out r_result int)
      BEGIN
        DECLARE insert_count int DEFAULT 0;
        START TRANSACTION;
        insert ignore into success_killed
          (seckill_id,user_phone,create_time)
          values (v_seckill_id,v_phone,v_kill_time);
        select row_count() into insert_count;
        IF (insert_count = 0) THEN
          ROLLBACK;
          set r_result = -1;
        ELSEIF(insert_count < 0) THEN
          ROLLBACK;
          SET R_RESULT = -2;
        ELSE
          update seckill
          set number = number-1
          where seckill_id = v_seckill_id
            and end_time > v_kill_time
            and start_time < v_kill_time
            and number > 0;
          select row_count() into insert_count;
          IF (insert_count = 0) THEN
            ROLLBACK;
            set r_result = 0;
          ELSEIF (insert_count < 0) THEN
            ROLLBACK;
            set r_result = -2;
          ELSE
            COMMIT;
            set r_result = 1;
          END IF;
        END IF;
      END;
    $$
    -- 存储过程定义结束
    
    DELIMITER ;
    --
    set @r_result=-3;
    -- 执行存储过程
    call execute_seckill(1003,13502178891,now(),@r_result);
    -- 获取结果
    select @r_result;

## 存储过程总结

- 存储过程优化：事务行级锁持有的时间
- 不要过度依赖存储过程
- 简单的逻辑可以应用存储过程
- QPS:一个秒杀单6000/qps

## 彩蛋

- 秒杀数据库的瓶颈主要在于，网络延迟和GC（垃圾回收机制）

  # 批量插入数据	

```
DELIMITER //

CREATE PROCEDURE insert_million_data()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE data_id INT;
    DECLARE data_name VARCHAR(10);
    DECLARE data_age INT;
    DECLARE data_email VARCHAR(20);

    WHILE i < 1000000 DO
        SET i = i + 1;
        SET data_id = i;
        SET data_name = CONCAT('Name', i);
        SET data_age = FLOOR(RAND() * 43) + 18;  -- 随机年龄范围在 18 到 60 之间
        SET data_email = CONCAT('email', i, '@example.com');

        INSERT INTO your_table (id, name, age, email)
        VALUES (data_id, data_name, data_age, data_email);

        INSERT INTO `ctt_contract` (`top_organ_id`, `organ_id`, `community_code`, `community_id`, `e_community_code`, `par_ctt_id`, `type_id`, `template_id`, `main_id`, `contract_name`, `contract_code`, `original_code`, `user_id`, `user_name`, `Sign_date`, `Sign_status`, `Exec_status`, `approval_status`, `ctt_begin_date`, `ctt_end_date`, `ctt_finish_date`, `finish_desc`, `is_auto_exec`, `buss_type_id`, `acct_code`, `acct_name`, `bank_account`, `acct_dept_id`, `dept_segment_code`, `dept_segment_name`, `create_user_id`, `create_user_name`, `create_time`, `update_user_id`, `update_user_name`, `update_time`, `link_ctt_id`, `link_ctt_name`, `source_type`, `md_req_status`, `modify_desc`, `modify_type`, `version`, `rec_pay_type`, `is_agreement`, `project_id`, `project_name`, `settle_type`, `settle_cycle`, `cycle_num`, `is_commonly`, `ctt_amount`, `is_seal`, `seal_type`, `archive_status`, `first_settle_date`, `execute_amount`, `real_fee`, `finish_type`, `submit_date`, `content_id`, `content_name`, `is_unlimited`, `win_bid_id`, `unlimit_cause`, `modify_amount`, `invalid_date`, `invalid_desc`) 
				VALUES ('12182455', '12504266', '', NULL, '', NULL, '257', '100', NULL, '物业前介品质管控工作服务委托合同', '物业前介品质管控工作服务委托合同', '物业前介品质管控工作服务委托合同', '1', '李四', '2022-05-15', '1', '2', '1', '2022-03-01', '2023-03-01', '2018-11-15', '', '1', NULL, '', '', '', '', '', '', NULL, '王五', '2021-03-01 00:00:00', '2295619', '张三', '2024-06-14 14:47:06', NULL, '', '1', '0', '', '', '1', '1', '0', '', '', '1', NULL, NULL, '1', '122.00', '0', NULL, '0', '1899-12-30', '222.00', '0.00', NULL, '2021-05-14 14:47:06', NULL, '', NULL, NULL, '', NULL, '2021-05-14', '');

        IF i % 1000 = 0 THEN
            SELECT CONCAT('Inserted ', i, ' rows');
        END IF;
    END WHILE;
END //

DELIMITER ;

-- 调用存储过程插入百万条数据
CALL insert_million_data();
```
# mysql修改json
```
#示例 
Warehouse-pyspark 单条记录的global_params字段内容如下
[
  {"prop": "bizdate", "type": "VARCHAR", "value": "$[yyyy-MM-dd -1]", "direct": "IN"},
  {"prop": "doris_hosts", "type": "VARCHAR", "value": "10.51.34.126", "direct": "IN"},
  {"prop": "doris_user", "type": "VARCHAR", "value": "user", "direct": "IN"}, 
  {"prop": "doris_passwd", "type": "VARCHAR", "value": "User@123", "direct": "IN"}, 
  {"prop": "mysql_host", "type": "VARCHAR", "value": "10.51.34.132", "direct": "IN"}, 
  {"prop": "mysql_user", "type": "VARCHAR", "value": "user", "direct": "IN"}, 
  {"prop": "mysql_passwd", "type": "VARCHAR", "value": "User@123", "direct": "IN"}, 
  {"prop": "table_name", "type": "VARCHAR", "value": "ads_mall_same_item_df", "direct": "IN"}
]

进行doris_hosts的值修改

@PGSQL

UPDATE t_ds_process_definition SET global_params = jsonb_set(global_params::jsonb, '{1, value}', '"10.51.34.1238"') WHERE name='Warehouse-pyspark';


@MYSQL

UPDATE t_ds_process_definition SET global_params = JSON_SET(global_params, '$[1].value', '10.51.34.126') WHERE name='Warehouse-pyspark';
```










