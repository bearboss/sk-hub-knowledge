#!bin/bash

mysql -h${dorisHost} -P${dorisPort} -u${dorisUser} -p${dorisPwd} <<EOF
   
    DROP USER IF EXISTS '${user}'@'${domain}';
    CREATE USER '${user}'@'${domain}' IDENTIFIED BY '${pwd}';
    
    GRANT SELECT_PRIV,LOAD_PRIV,ALTER_PRIV,CREATE_PRIV,DROP_PRIV ON *.* TO '${user}'@'${domain}';
    
EOF