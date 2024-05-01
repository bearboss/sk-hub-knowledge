#@echo off 
#if "%1" == "h" goto begin 
#mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
#:begin 

tasklist|findstr /i "nginx.exe"
taskkill /f /t /im nginx.exe

d:
cd JJDK/nginx
nginx.exe -c D:\JJDK\nginx\conf\nginx.conf
cmd
pause
exit
/b