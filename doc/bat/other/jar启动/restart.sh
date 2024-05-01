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

