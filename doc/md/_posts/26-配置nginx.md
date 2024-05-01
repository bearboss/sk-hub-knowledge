title: 配置nginx

date: 2021-05-29 15:20:36

tags: nginx

categories: nginx

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/26.jpg)

</span>

<!--more-->

# 搭建下载

> 省略。。。

# 配置

> nginx.conf

```
#user  nobody;
worker_processes  1;

error_log   E:/config/nginx_log/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;
    
    log_format main escape=json '{"timestamp":"$time_iso8601","token":"$http_X_PD_AUTH_TOKEN","request_method":"$request_method","request_uri":"$request_uri","content_type":"$content_type","args":"$args","query_string":"$query_string","request_body":"$request_body","cookie":"$http_cookie","remote_addr":"$remote_addr","uri":"$uri","remote_user":"$remote_user","request":"$request","ups_status":"$upstream_status","http_host":"$http_host","status":"$status","request_length":"$request_length","body_bytes_sent":"$body_bytes_sent","http_referer":"$http_referer","http_user_agent":"$http_user_agent","request_time":"$request_time","http_x_forwarded_for":"$http_x_forwarded_for","upstream_addr":"$upstream_addr","upstream_response_time":"$upstream_response_time"}';

    access_log  E:/config/nginx_log/main.log;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout 120s;
    keepalive_requests 10000;

    gzip  on;

    server {
        listen       9999;
        server_name  127.0.0.1;
        charset utf-8;
        access_log  E:/config/nginx_log/static.log ;

        location / {
            alias  E:/Jproject/webfFramework/code16sss-ShangChengMoBan-master/ShangChengMoBan/;
            index  index.html index.htm;
        }

        error_page  404 403           /50x.html;
        error_page  500 502 503 504  /50x.html;
        location = /50x.html {
           alias   E:/Jproject/spring-organic-product/organic-html/organic-error/500.html;
        }
        location = /404.html {
            alias   E:/Jproject/spring-organic-product/organic-html/organic-error/404.html;
        }
    }

    upstream admin_server{
        server 127.0.0.1:8081 weight=1;
        #server 127.0.0.1:8082 weight=1;
        keepalive 500;
    }
    server {
        listen       80;
        server_name  127.0.0.1;
           
        charset utf-8;
        access_log  E:/config/nginx_log/admin.log ;

        location /system/ {
            root   html;
            proxy_pass http://admin_server;
        
            proxy_set_header Host $host:$server_port;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header REMOTE-HOST $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            client_max_body_size    2000m;

            proxy_connect_timeout 3600;
            proxy_send_timeout 3600;
            proxy_read_timeout 3600;
            index  index.html index.htm;
        }
    
        location / {
            alias  E:/Jproject/spring-organic-product/organic-html/organic-system/;
            index  index.html index.htm;
        }

        error_page  404 403           /404.html;
        error_page  500 502 503 504  /50x.html;
        location = /50x.html {
           alias   E:/Jproject/spring-organic-product/organic-html/organic-error/500.html;
        }
        location = /404.html {
            alias   E:/Jproject/spring-organic-product/organic-html/organic-error/404.html;
        }
    }

    server {
        listen       80;
        server_name  static.mx.com;
        charset utf-8;
        access_log  E:/config/nginx_log/static.log ;

        location / {
            alias  E:/organic-ftp/;
            index  index.html index.htm;
        }

        error_page  404 403           /50x.html;
        error_page  500 502 503 504  /50x.html;
        location = /50x.html {
           alias   E:/Jproject/spring-organic-product/organic-html/organic-error/500.html;
        }
        location = /404.html {
            alias   E:/Jproject/spring-organic-product/organic-html/organic-error/404.html;
        }
    }

    server {
        listen       80;
        server_name  admin.mx.com;
           
        charset utf-8;
        access_log  E:/config/nginx_log/admin.log ;

        location /system/ {
            root   html;
            proxy_pass http://admin_server;
        
            proxy_set_header Host $host:$server_port;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header REMOTE-HOST $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            client_max_body_size    2000m;

            proxy_connect_timeout 3600;
            proxy_send_timeout 3600;
            proxy_read_timeout 3600;
            index  index.html index.htm;
        }
    
        location / {
            alias  E:/Jproject/spring-organic-product/organic-html/organic-system/;
            index  index.html index.htm;
        }

        error_page  404 403           /404.html;
        error_page  500 502 503 504  /50x.html;
        location = /50x.html {
           alias   E:/Jproject/spring-organic-product/organic-html/organic-error/500.html;
        }
        location = /404.html {
            alias   E:/Jproject/spring-organic-product/organic-html/organic-error/404.html;
        }
    }

  upstream app_server{
        server 127.0.0.1:8081 weight=1;
        #server 127.0.0.1:8082 weight=1;
        keepalive 500;
    }

    server {
        listen       80;
        server_name  www.mx.com;
        charset utf-8;

        access_log  E:/config/nginx_log/www.log ;

        location /food/ {
            root   html;
           
            proxy_pass http://app_server;
        
            proxy_set_header Host $host:$server_port;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header REMOTE-HOST $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            client_max_body_size    2000m;

            proxy_connect_timeout 3600;
            proxy_send_timeout 3600;
            proxy_read_timeout 3600;
            index  index.html index.htm;
        }
         location / {
            alias  E:/Jproject/spring-organic-product/organic-html/organic-app/;
            index  index.html index.htm;
        }

        error_page  404 403           /404.html;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
           alias   E:/Jproject/spring-organic-product/organic-html/organic-error/500.html;
        }
        location = /404.html {
            alias   E:/Jproject/spring-organic-product/organic-html/organic-error/404.html;
        }
    }
}
```