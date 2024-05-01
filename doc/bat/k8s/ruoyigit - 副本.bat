@echo off
setlocal enabledelayedexpansion
 
REM 设置要提交的文件路径
E:

cd E:/Jgit-project/ruoyi

git add .

git commit -m"auto commit"


git push