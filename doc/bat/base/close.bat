@echo off
TASKKILL /F /IM cmd.exe /T
cmd
TASKKILL /F /FI "WINDOWTITLE eq abc"
taskkill /f /FI "WINDOWPATH eq C:\Windows\System32\cmd.exe"
cmd