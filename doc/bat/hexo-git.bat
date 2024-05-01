chcp 65001

@echo off
setlocal enabledelayedexpansion
 
REM 设置要提交的文件路径
E:

cd E:/Jgit-project/hexo-site

git add .

git commit -m"新增知识"


git push


cmd