#!/bin/bash

pids=`ps -ef | grep  litemall-wx-api-0.1.0.jar | grep -v grep | awk '{print $2}'`

echo "当前进程号[]: " $pids

if [ ! -z "$pids" ]; then
  for id in $pids
  do
    kill -9 $id
    echo "killed $id"
  done
fi

nohup java -jar  /data/app/xqmall-wx/litemall-wx-api-0.1.0.jar &

echo "启动完成"

