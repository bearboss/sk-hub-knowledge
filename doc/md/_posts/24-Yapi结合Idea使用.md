title: Yapi结合Idea使用

date: 2021-05-29 15:20:36

tags: Yapi

categories: Yapi

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/24.jpg)

</span>

<!--more-->
# Yapi 与 swagger

![](/images/yapi/1.png)

# 服务器安装部署Yapi

> 省略...

# IDEA安装YapiUpload插件

* 在idea中安装YapiUpload插件，在marketplace中搜索YapiUpload

* ![](/images/yapi/2.png)

* 确认安装成功

* ![](/images/yapi/3.png)

# 配置Yapi地址信息

* 在项目中的.idea文件中，找到misc.xml文件

* ![](/images/yapi/4.png)

* 将项目在Yapi中的信息填写到其中

* ![](/images/yapi/5.png)

# 浏览器安装cross-request插件

* [本地下载](/images/yapi/cross-request.zip)

* cross-request 插件，赋予一个 html 页面跨域请求能力，浏览器必须安装该插件才可在yapi中调用各应用接口。（有提供安装包）
* *  解压
* *  进入到Chrome的【扩展程序】页面，首先开启【开发者模式】，一定要先开启开发者模式
* * “加载已解压的扩展程序”，选择步骤1解压的文件夹，即可

# 上传接口

> 结合注释，请配置注释模板

1.	选中单个方法，上传，则是单个接口上传至平台，多次上传同一个接口，只要接口全类名未做更改，则会更新平台已有接口信息
2.	Controller层中直接右键上传，则是将该类下所有接口上传，平台中已有接口走更新逻辑
3.	关于代码风格，请务必按标准编码风格进行，入参出参需把注释标全了，保证上传的接口可读性，互惠互利
4.	[IDE配置参考链接](https://www.liangzl.com/get-article-detail-146070.html)
5. 样例
* 控制层
* * ![](/images/yapi/6.png)
* 实体类
* * ![](/images/yapi/7.png)
* 结果
* * ![](/images/yapi/8.png)


