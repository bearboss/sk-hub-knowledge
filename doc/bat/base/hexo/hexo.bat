@echo off 
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin
E:
cd E:\Jgit-project\hexo-site
call hexo clean
call hexo g
call hexo s
