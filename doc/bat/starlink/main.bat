@echo off
chcp 65001
setlocal enabledelayedexpansion
set /p port=是否需要开启zk,nacos,需要请输入yes,不需要直接回车:
    if "%port%" == "yes" (
	start  cmd  /c call E:/Jsort/文档/bat-脚本/starlink/zk.bat
	start  cmd  /c call E:\Jsort\nacos-server-2.2.3\bin\startup.cmd
       	start  cmd  /c call main-ui.bat
	start  cmd  /c call main-java.bat	
    ) else (
      	start  cmd  /c call main-ui.bat
	start  cmd  /c call main-java.bat
  )


