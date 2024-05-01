#!bin/bash

mysql -h${dorisHost} -P${dorisPort} -u${dorisUser} -p${dorisPwd} <<EOF
        
    DROP database IF EXISTS ${database};
    CREATE database IF NOT EXISTS ${database};
    
    DROP USER IF EXISTS '${user}'@'${domain}';
    CREATE USER '${user}'@'${domain}' IDENTIFIED BY '${pwd}';
    
    GRANT SELECT_PRIV,LOAD_PRIV,ALTER_PRIV,CREATE_PRIV,DROP_PRIV ON *.${database}.* TO '${user}'@'${domain}';
    
    use ${database};
    
    drop table if exists ${table};
    CREATE TABLE IF NOT EXISTS ${table}(
        stats_date INT(10)   COMMENT '统计时间Y-M' ,
        org_id varchar(256) DEFAULT NULL COMMENT "组织ID",
        org_level int(10) DEFAULT NULL COMMENT "组织层级",
        project_id VARCHAR(256)    COMMENT '项目ID' ,
        project_code VARCHAR(256)    COMMENT '项目code' ,
        city_id VARCHAR(256)    COMMENT '城市公司ID' ,
        city_code VARCHAR(256)    COMMENT '城市公司code' ,
        company_id VARCHAR(256)    COMMENT '平台公司ID' ,
        company_code VARCHAR(256)    COMMENT '平台公司code' ,
        group_id VARCHAR(256)    COMMENT '集团ID' ,
        group_code VARCHAR(256)    COMMENT '集团code' ,
        total_num BIGINT(20)    COMMENT '本月项目工单的总数量' ,
        receive_num BIGINT(20)    COMMENT '本月项目接单的总数量' ,
        receive_ratio DECIMAL(10,4)   COMMENT '接单及时率' ,
        average_receive_ratio DECIMAL(10,4)   COMMENT '平均接单及时率' ,
        dw_process_dt DATETIME    COMMENT '处理时间'
    )
    UNIQUE KEY(stats_date, org_id)
    DISTRIBUTED BY HASH(stats_date, org_id) BUCKETS 1
    PROPERTIES(
        "replication_num" = "${replicationNum}"
    );
EOF

#CREATE ROLE mx_role;
#CREATE USER 'mx'@'%' IDENTIFIED BY '123456' DEFAULT ROLE 'mx_role';
#GRANT SELECT_PRIV,LOAD_PRIV,ALTER_PRIV,CREATE_PRIV,DROP_PRIV ON *.ads_eesd.* TO ROLE 'my_role';