title: jeecg接口文档

date: 2021-06-11 15:20:36

tags: Java

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/47.jpg)

</span>

<!--more-->

# Jeecg-Boot 后台服务API接口文档


**简介**:Jeecg-Boot 后台服务API接口文档


**HOST**:192.168.100.165:8088


**联系人**:JEECG团队


**Version**:1.0


**接口路径**:/v2/api-docs


[TOC]






# 单表DEMO


## 添加DEMO


**接口地址**:`/fastrun/test/jeecgDemo/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:添加DEMO


**请求示例**:


```javascript
{
	"age": 0,
	"birthday": "",
	"bonusMoney": 0,
	"content": "",
	"createBy": "",
	"createTime": "",
	"email": "",
	"id": "",
	"keyWord": "",
	"name": "",
	"punchTime": "",
	"salaryMoney": 0,
	"sex": "",
	"sysOrgCode": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|jeecgDemo|测试DEMO|body|true|测试DEMO对象|测试DEMO对象|
|&emsp;&emsp;age|年龄||false|integer(int32)||
|&emsp;&emsp;birthday|生日||false|string(date-time)||
|&emsp;&emsp;bonusMoney|奖金||false|number(double)||
|&emsp;&emsp;content|个人简介||false|string||
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;email|邮箱||false|string||
|&emsp;&emsp;id|ID||false|string||
|&emsp;&emsp;keyWord|关键词||false|string||
|&emsp;&emsp;name|姓名||false|string||
|&emsp;&emsp;punchTime|打卡时间||false|string(date-time)||
|&emsp;&emsp;salaryMoney|工资||false|number||
|&emsp;&emsp;sex|性别||false|string||
|&emsp;&emsp;sysOrgCode|部门编码||false|string||
|&emsp;&emsp;updateBy|更新人||false|string||
|&emsp;&emsp;updateTime|更新时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 通过ID删除DEMO


**接口地址**:`/fastrun/test/jeecgDemo/delete`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:通过ID删除DEMO


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 批量删除DEMO


**接口地址**:`/fastrun/test/jeecgDemo/deleteBatch`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:批量删除DEMO


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 编辑DEMO


**接口地址**:`/fastrun/test/jeecgDemo/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:编辑DEMO


**请求示例**:


```javascript
{
	"age": 0,
	"birthday": "",
	"bonusMoney": 0,
	"content": "",
	"createBy": "",
	"createTime": "",
	"email": "",
	"id": "",
	"keyWord": "",
	"name": "",
	"punchTime": "",
	"salaryMoney": 0,
	"sex": "",
	"sysOrgCode": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|jeecgDemo|测试DEMO|body|true|测试DEMO对象|测试DEMO对象|
|&emsp;&emsp;age|年龄||false|integer(int32)||
|&emsp;&emsp;birthday|生日||false|string(date-time)||
|&emsp;&emsp;bonusMoney|奖金||false|number(double)||
|&emsp;&emsp;content|个人简介||false|string||
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;email|邮箱||false|string||
|&emsp;&emsp;id|ID||false|string||
|&emsp;&emsp;keyWord|关键词||false|string||
|&emsp;&emsp;name|姓名||false|string||
|&emsp;&emsp;punchTime|打卡时间||false|string(date-time)||
|&emsp;&emsp;salaryMoney|工资||false|number||
|&emsp;&emsp;sex|性别||false|string||
|&emsp;&emsp;sysOrgCode|部门编码||false|string||
|&emsp;&emsp;updateBy|更新人||false|string||
|&emsp;&emsp;updateTime|更新时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 获取Demo数据列表


**接口地址**:`/fastrun/test/jeecgDemo/list`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:获取所有Demo数据列表


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|age|年龄|query|false|integer(int32)||
|birthday|生日|query|false|string(date-time)||
|bonusMoney|奖金|query|false|number(double)||
|content|个人简介|query|false|string||
|createBy|创建人|query|false|string||
|createTime|创建时间|query|false|string(date-time)||
|email|邮箱|query|false|string||
|id|ID|query|false|string||
|keyWord|关键词|query|false|string||
|name|姓名|query|false|string||
|pageNo|pageNo|query|false|integer(int32)||
|pageSize|pageSize|query|false|integer(int32)||
|punchTime|打卡时间|query|false|string(date-time)||
|salaryMoney|工资|query|false|number||
|sex|性别|query|false|string||
|sysOrgCode|部门编码|query|false|string||
|updateBy|更新人|query|false|string||
|updateTime|更新时间|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 通过ID查询DEMO


**接口地址**:`/fastrun/test/jeecgDemo/queryById`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:通过ID查询DEMO


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|示例id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 填值规则


## 填值规则-添加


**接口地址**:`/fastrun/sys/fillRule/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:填值规则-添加


**请求示例**:


```javascript
{
	"createBy": "",
	"createTime": "",
	"id": "",
	"ruleClass": "",
	"ruleCode": "",
	"ruleName": "",
	"ruleParams": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysFillRule|填值规则|body|true|sys_fill_rule对象|sys_fill_rule对象|
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;id|主键ID||false|string||
|&emsp;&emsp;ruleClass|规则实现类||false|string||
|&emsp;&emsp;ruleCode|规则Code||false|string||
|&emsp;&emsp;ruleName|规则名称||false|string||
|&emsp;&emsp;ruleParams|规则参数||false|string||
|&emsp;&emsp;updateBy|修改人||false|string||
|&emsp;&emsp;updateTime|修改时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 填值规则-通过id删除


**接口地址**:`/fastrun/sys/fillRule/delete`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:填值规则-通过id删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 填值规则-批量删除


**接口地址**:`/fastrun/sys/fillRule/deleteBatch`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:填值规则-批量删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 填值规则-编辑


**接口地址**:`/fastrun/sys/fillRule/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:填值规则-编辑


**请求示例**:


```javascript
{
	"createBy": "",
	"createTime": "",
	"id": "",
	"ruleClass": "",
	"ruleCode": "",
	"ruleName": "",
	"ruleParams": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysFillRule|填值规则|body|true|sys_fill_rule对象|sys_fill_rule对象|
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;id|主键ID||false|string||
|&emsp;&emsp;ruleClass|规则实现类||false|string||
|&emsp;&emsp;ruleCode|规则Code||false|string||
|&emsp;&emsp;ruleName|规则名称||false|string||
|&emsp;&emsp;ruleParams|规则参数||false|string||
|&emsp;&emsp;updateBy|修改人||false|string||
|&emsp;&emsp;updateTime|修改时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 填值规则-分页列表查询


**接口地址**:`/fastrun/sys/fillRule/list`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:填值规则-分页列表查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy|创建人|query|false|string||
|createTime|创建时间|query|false|string(date-time)||
|id|主键ID|query|false|string||
|pageNo|pageNo|query|false|integer(int32)||
|pageSize|pageSize|query|false|integer(int32)||
|ruleClass|规则实现类|query|false|string||
|ruleCode|规则Code|query|false|string||
|ruleName|规则名称|query|false|string||
|ruleParams|规则参数|query|false|string||
|updateBy|修改人|query|false|string||
|updateTime|修改时间|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 填值规则-通过id查询


**接口地址**:`/fastrun/sys/fillRule/queryById`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:填值规则-通过id查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 多数据源管理


## 多数据源管理-添加


**接口地址**:`/fastrun/sys/dataSource/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:多数据源管理-添加


**请求示例**:


```javascript
{
	"code": "",
	"createBy": "",
	"createTime": "",
	"dbDriver": "",
	"dbName": "",
	"dbPassword": "",
	"dbType": "",
	"dbUrl": "",
	"dbUsername": "",
	"id": "",
	"name": "",
	"remark": "",
	"sysOrgCode": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysDataSource|多数据源管理|body|true|sys_data_source对象|sys_data_source对象|
|&emsp;&emsp;code|数据源编码||false|string||
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建日期||false|string(date-time)||
|&emsp;&emsp;dbDriver|驱动类||false|string||
|&emsp;&emsp;dbName|数据库名称||false|string||
|&emsp;&emsp;dbPassword|密码||false|string||
|&emsp;&emsp;dbType|数据库类型||false|string||
|&emsp;&emsp;dbUrl|数据源地址||false|string||
|&emsp;&emsp;dbUsername|用户名||false|string||
|&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;name|数据源名称||false|string||
|&emsp;&emsp;remark|备注||false|string||
|&emsp;&emsp;sysOrgCode|所属部门||false|string||
|&emsp;&emsp;updateBy|更新人||false|string||
|&emsp;&emsp;updateTime|更新日期||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 多数据源管理-通过id删除


**接口地址**:`/fastrun/sys/dataSource/delete`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:多数据源管理-通过id删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 多数据源管理-批量删除


**接口地址**:`/fastrun/sys/dataSource/deleteBatch`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:多数据源管理-批量删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 多数据源管理-编辑


**接口地址**:`/fastrun/sys/dataSource/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:多数据源管理-编辑


**请求示例**:


```javascript
{
	"code": "",
	"createBy": "",
	"createTime": "",
	"dbDriver": "",
	"dbName": "",
	"dbPassword": "",
	"dbType": "",
	"dbUrl": "",
	"dbUsername": "",
	"id": "",
	"name": "",
	"remark": "",
	"sysOrgCode": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysDataSource|多数据源管理|body|true|sys_data_source对象|sys_data_source对象|
|&emsp;&emsp;code|数据源编码||false|string||
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建日期||false|string(date-time)||
|&emsp;&emsp;dbDriver|驱动类||false|string||
|&emsp;&emsp;dbName|数据库名称||false|string||
|&emsp;&emsp;dbPassword|密码||false|string||
|&emsp;&emsp;dbType|数据库类型||false|string||
|&emsp;&emsp;dbUrl|数据源地址||false|string||
|&emsp;&emsp;dbUsername|用户名||false|string||
|&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;name|数据源名称||false|string||
|&emsp;&emsp;remark|备注||false|string||
|&emsp;&emsp;sysOrgCode|所属部门||false|string||
|&emsp;&emsp;updateBy|更新人||false|string||
|&emsp;&emsp;updateTime|更新日期||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 多数据源管理-分页列表查询


**接口地址**:`/fastrun/sys/dataSource/list`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:多数据源管理-分页列表查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|code|数据源编码|query|false|string||
|createBy|创建人|query|false|string||
|createTime|创建日期|query|false|string(date-time)||
|dbDriver|驱动类|query|false|string||
|dbName|数据库名称|query|false|string||
|dbPassword|密码|query|false|string||
|dbType|数据库类型|query|false|string||
|dbUrl|数据源地址|query|false|string||
|dbUsername|用户名|query|false|string||
|id|id|query|false|string||
|name|数据源名称|query|false|string||
|pageNo|pageNo|query|false|integer(int32)||
|pageSize|pageSize|query|false|integer(int32)||
|remark|备注|query|false|string||
|sysOrgCode|所属部门|query|false|string||
|updateBy|更新人|query|false|string||
|updateTime|更新日期|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 多数据源管理-通过id查询


**接口地址**:`/fastrun/sys/dataSource/queryById`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:多数据源管理-通过id查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 定时任务接口


## 暂停定时任务


**接口地址**:`/fastrun/sys/quartzJob/pause`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|jobClassName|jobClassName|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 恢复定时任务


**接口地址**:`/fastrun/sys/quartzJob/resume`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|jobClassName|jobClassName|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 文件管理


## 文件管理-添加


**接口地址**:`/fastrun/system/sysFile/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:文件管理-添加


**请求示例**:


```javascript
{
	"businessId": "",
	"createBy": "",
	"createTime": "",
	"delFlag": 0,
	"fileLength": 0,
	"fileName": "",
	"filePath": "",
	"fileType": "",
	"id": "",
	"moduleCode": "",
	"projectId": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysFile|文件管理|body|true|sys_file对象|sys_file对象|
|&emsp;&emsp;businessId|业务ID||false|string||
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;delFlag|删除标识0-正常,1-已删除||false|integer(int32)||
|&emsp;&emsp;fileLength|文件大小||false|integer(int64)||
|&emsp;&emsp;fileName|文件名称||false|string||
|&emsp;&emsp;filePath|文件路径||false|string||
|&emsp;&emsp;fileType|文件类型||false|string||
|&emsp;&emsp;id|ID||false|string||
|&emsp;&emsp;moduleCode|模块名称||false|string||
|&emsp;&emsp;projectId|项目ID||false|string||
|&emsp;&emsp;updateBy|修改人||false|string||
|&emsp;&emsp;updateTime|修改时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 文件管理-通过id删除


**接口地址**:`/fastrun/system/sysFile/delete`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:文件管理-通过id删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 文件管理-批量删除


**接口地址**:`/fastrun/system/sysFile/deleteBatch`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:文件管理-批量删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 下载附件


**接口地址**:`/fastrun/system/sysFile/downLoadStatic`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:download attachment 


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 下载附件


**接口地址**:`/fastrun/system/sysFile/download`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:download attachment 


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 文件管理-编辑


**接口地址**:`/fastrun/system/sysFile/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:文件管理-编辑


**请求示例**:


```javascript
{
	"businessId": "",
	"createBy": "",
	"createTime": "",
	"delFlag": 0,
	"fileLength": 0,
	"fileName": "",
	"filePath": "",
	"fileType": "",
	"id": "",
	"moduleCode": "",
	"projectId": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysFile|文件管理|body|true|sys_file对象|sys_file对象|
|&emsp;&emsp;businessId|业务ID||false|string||
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;delFlag|删除标识0-正常,1-已删除||false|integer(int32)||
|&emsp;&emsp;fileLength|文件大小||false|integer(int64)||
|&emsp;&emsp;fileName|文件名称||false|string||
|&emsp;&emsp;filePath|文件路径||false|string||
|&emsp;&emsp;fileType|文件类型||false|string||
|&emsp;&emsp;id|ID||false|string||
|&emsp;&emsp;moduleCode|模块名称||false|string||
|&emsp;&emsp;projectId|项目ID||false|string||
|&emsp;&emsp;updateBy|修改人||false|string||
|&emsp;&emsp;updateTime|修改时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 文件管理-分页列表查询


**接口地址**:`/fastrun/system/sysFile/list`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:文件管理-分页列表查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|businessId|业务ID|query|false|string||
|createBy|创建人|query|false|string||
|createTime|创建时间|query|false|string(date-time)||
|delFlag|删除标识0-正常,1-已删除|query|false|integer(int32)||
|fileLength|文件大小|query|false|integer(int64)||
|fileName|文件名称|query|false|string||
|filePath|文件路径|query|false|string||
|fileType|文件类型|query|false|string||
|id|ID|query|false|string||
|moduleCode|模块名称|query|false|string||
|pageNo|pageNo|query|false|integer(int32)||
|pageSize|pageSize|query|false|integer(int32)||
|projectId|项目ID|query|false|string||
|updateBy|修改人|query|false|string||
|updateTime|修改时间|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 下载附件


**接口地址**:`/fastrun/system/sysFile/opendownload`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:download attachment 


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 文件管理-通过businessId查询


**接口地址**:`/fastrun/system/sysFile/queryByBusinessId`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:文件管理-通过businessId查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|businessId|businessId|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 文件管理-通过id查询


**接口地址**:`/fastrun/system/sysFile/queryById`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:文件管理-通过id查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 上传附件


**接口地址**:`/fastrun/system/sysFile/upload`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:upload attachment 


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|businessId|businessId|query|false|string||
|fileType|fileType|query|false|string||
|moduleCode|moduleCode|query|false|string||
|projectId|projectId|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 流程


## 流程-查询流程类型


**接口地址**:`/fastrun/actBusiness/actZProcess`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:流程类型


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-添加申请草稿状态


**接口地址**:`/fastrun/actBusiness/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:业务表单参数数据一并传过来！


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|procDeTitle|申请标题|body|true|string||
|procDefId|流程定义Id|body|true|string||
|tableName|数据表名|body|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-提交申请 启动流程


**接口地址**:`/fastrun/actBusiness/apply`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:提交申请 启动流程。


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|applyTime||query|false|string(date-time)||
|assignees|审批人（用户名），多个,号相连|query|false|string||
|createBy||query|false|string||
|createTime||query|false|string(date-time)||
|currTaskName||query|false|string||
|dataMap||query|false|object||
|delFlag||query|false|integer(int32)||
|firstGateway|第一个节点是否为网关|query|false|boolean||
|id|id|query|false|string||
|isHistory||query|false|boolean||
|params|流程设置参数|query|false|object||
|priority|任务优先级 默认0 0普通1重要2紧急|query|false|integer(int32)||
|procDefId|流程定义id|query|false|string||
|procInstId|流程实例id|query|false|string||
|procInstStatus||query|false|integer(int32)||
|processName||query|false|string||
|result||query|false|integer(int32)||
|routeName||query|false|string||
|sendEmail|是否发送邮件通知-暂无用|query|false|boolean||
|sendMessage|是否发送站内消息|query|false|boolean||
|sendSms|是否发送短信通知-暂无用|query|false|boolean||
|status||query|false|integer(int32)||
|tableId||query|false|string||
|tableName||query|false|string||
|title||query|false|string||
|updateBy||query|false|string||
|updateTime||query|false|string(date-time)||
|userId||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-撤回申请


**接口地址**:`/fastrun/actBusiness/cancel`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:撤回申请


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|流程扩展表id|query|true|string||
|procInstId|流程实例id|query|true|string||
|reason|撤销理由原因说明|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-通过id删除草稿状态申请


**接口地址**:`/fastrun/actBusiness/delByIds`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:通过id删除草稿状态申请


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|流程扩展表id，多个,号相连|body|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-查询申请列表 与 已办列表的合集


**接口地址**:`/fastrun/actBusiness/doAndApplyList`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:查询申请列表 与 已办列表的合集


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|applyTime||query|false|string(date-time)||
|assignees|审批人（用户名），多个,号相连|query|false|string||
|categoryId|categoryId|query|false|string||
|createBy||query|false|string||
|createTime||query|false|string(date-time)||
|currTaskName||query|false|string||
|dataMap||query|false|object||
|delFlag||query|false|integer(int32)||
|firstGateway|第一个节点是否为网关|query|false|boolean||
|id|id|query|false|string||
|isHistory||query|false|boolean||
|name|name|query|false|string||
|params|流程设置参数|query|false|object||
|priority|任务优先级 默认0 0普通1重要2紧急|query|false|integer(int32)||
|procDefId|流程定义id|query|false|string||
|procInstId|流程实例id|query|false|string||
|procInstStatus||query|false|integer(int32)||
|processName||query|false|string||
|result||query|false|integer(int32)||
|routeName||query|false|string||
|sendEmail|是否发送邮件通知-暂无用|query|false|boolean||
|sendMessage|是否发送站内消息|query|false|boolean||
|sendSms|是否发送短信通知-暂无用|query|false|boolean||
|status||query|false|integer(int32)||
|tableId||query|false|string||
|tableName||query|false|string||
|title||query|false|string||
|updateBy||query|false|string||
|updateTime||query|false|string(date-time)||
|userId||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-修改业务表单信息


**接口地址**:`/fastrun/actBusiness/editForm`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:业务表单参数数据一并传过来!


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|业务表数据id|body|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-获取业务表单信息


**接口地址**:`/fastrun/actBusiness/getForm`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:获取业务表单信息


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tableId|业务表数据id|body|true|string||
|tableName|业务表名|body|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-流程列表


**接口地址**:`/fastrun/actBusiness/listData`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:流程列表，登录用户的流程列表


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|applyTime||query|false|string(date-time)||
|assignees|审批人（用户名），多个,号相连|query|false|string||
|createBy||query|false|string||
|createTime||query|false|string(date-time)||
|currTaskName||query|false|string||
|dataMap||query|false|object||
|delFlag||query|false|integer(int32)||
|firstGateway|第一个节点是否为网关|query|false|boolean||
|id|id|query|false|string||
|isHistory||query|false|boolean||
|params|流程设置参数|query|false|object||
|priority|任务优先级 默认0 0普通1重要2紧急|query|false|integer(int32)||
|procDefId|流程定义id|query|false|string||
|procInstId|流程实例id|query|false|string||
|procInstStatus||query|false|integer(int32)||
|processName||query|false|string||
|result||query|false|integer(int32)||
|routeName||query|false|string||
|sendEmail|是否发送邮件通知-暂无用|query|false|boolean||
|sendMessage|是否发送站内消息|query|false|boolean||
|sendSms|是否发送短信通知-暂无用|query|false|boolean||
|status||query|false|integer(int32)||
|tableId||query|false|string||
|tableName||query|false|string||
|title||query|false|string||
|updateBy||query|false|string||
|updateTime||query|false|string(date-time)||
|userId||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-通过流程定义id获取第一个任务节点


**接口地址**:`/fastrun/actProcessIns/getFirstNode`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:通过流程定义id获取第一个任务节点，包含可供选择的审批人、网关信息等


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|procDefId|流程定义Id|body|true|string||
|tableId|表id|body|true|string||
|tableName|表名|body|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-任务节点审批 驳回至发起人


**接口地址**:`/fastrun/actTask/back`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:任务节点审批 驳回至发起人


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|comment|意见评论|query|false|string||
|id|任务id|query|false|string||
|procInstId|流程实例id|query|false|string||
|sendEmail|是否发送邮件通知|query|false|boolean||
|sendMessage|是否发送站内消息|query|false|boolean||
|sendSms|是否发送短信通知|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 任务节点审批驳回至指定历史节点


**接口地址**:`/fastrun/actTask/backToTask`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|assignees|原节点审批人|query|false|string||
|backTaskKey|驳回指定节点key|query|false|string||
|comment|意见评论|query|false|string||
|id|任务id|query|false|string||
|priority|优先级|query|false|integer(int32)||
|procDefId|流程定义id|query|false|string||
|procInstId|流程实例id|query|false|string||
|sendEmail|是否发送邮件通知|query|false|boolean||
|sendMessage|是否发送站内消息|query|false|boolean||
|sendSms|是否发送短信通知|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 委托他人代办


**接口地址**:`/fastrun/actTask/delegate`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|comment|意见评论|query|false|string||
|id|任务id|query|false|string||
|procInstId|流程实例id|query|false|string||
|sendEmail|是否发送邮件通知|query|false|boolean||
|sendMessage|是否发送站内消息|query|false|boolean||
|sendSms|是否发送短信通知|query|false|boolean||
|userId|委托用户id|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-删除任务历史


**接口地址**:`/fastrun/actTask/deleteHistoric/{ids}`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:删除任务历史


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-已办列表


**接口地址**:`/fastrun/actTask/doneList`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:已办列表


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|categoryId|categoryId|query|false|string||
|name|name|query|false|string||
|priority|priority|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-获取可返回的节点


**接口地址**:`/fastrun/actTask/getBackList/{procInstId}`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:获取可返回的节点


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|procInstId|procInstId|path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-流程流转历史


**接口地址**:`/fastrun/actTask/historicFlow/{id}`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:流程流转历史


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|实例Id|path|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 任务节点审批通过


**接口地址**:`/fastrun/actTask/pass`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|assignees|下个节点审批人|query|false|string||
|comment|意见评论|query|false|string||
|id|任务id|query|false|string||
|priority|优先级|query|false|integer(int32)||
|procInstId|流程实例id|query|false|string||
|sendEmail|是否发送邮件通知|query|false|boolean||
|sendMessage|是否发送站内消息|query|false|boolean||
|sendSms|是否发送短信通知|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-待办条数


**接口地址**:`/fastrun/actTask/todoCounts`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:待办列表


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|procDefIds|流程定义key|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-代办列表


**接口地址**:`/fastrun/actTask/todoList`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:代办列表


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|categoryId|任务分类|body|false|string||
|createTime_begin|创建开始时间|body|false|string||
|createTime_end|创建结束时间|body|false|string||
|name|任务名称|body|false|string||
|priority|优先级|body|false|integer||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 通过当前节点定义id获取下一个节点


**接口地址**:`/fastrun/activiti_process/getNextNode`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|currActId|当前节点定义id|body|false|string||
|procDefId|流程定义id|body|false|string||
|procInstId|当前节点定义id|body|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 通过节点nodeId获取审批人


**接口地址**:`/fastrun/activiti_process/getNode`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|nodeId|节点nodeId|query|false|string||
|tableId|表单id|query|false|string||
|tableName|表单名称|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 流程-获取可用流程


**接口地址**:`/fastrun/activiti_process/listData`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:获取可用流程


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|lckey|流程key|body|false|string||
|lcmc|流程名称|body|false|string||
|roles|如果此项不为空，则会过滤当前用户的角色权限|body|false|boolean||
|status|流程状态 部署后默认1激活|body|false|string||
|zx|是否最新|body|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 获取最新部署的流程定义


**接口地址**:`/fastrun/activiti_process/queryNewestProcess`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|processKey|流程定义key|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 用户登录


## 登录接口


**接口地址**:`/fastrun/sys/login`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
	"captcha": "",
	"checkKey": "",
	"password": "",
	"username": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysLoginModel|登录对象|body|true|登录对象|登录对象|
|&emsp;&emsp;captcha|验证码||false|string||
|&emsp;&emsp;checkKey|验证码key||false|string||
|&emsp;&emsp;password|密码||false|string||
|&emsp;&emsp;username|账号||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«JSONObject»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 手机号登录接口


**接口地址**:`/fastrun/sys/phoneLogin`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|jsonObject|jsonObject|body|true|||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«JSONObject»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 获取验证码


**接口地址**:`/fastrun/sys/randomImage/{key}`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|key|key|path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«string»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|string||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": "",
	"success": true,
	"timestamp": 0
}
```


# 编码校验规则


## 编码校验规则-添加


**接口地址**:`/fastrun/sys/checkRule/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:编码校验规则-添加


**请求示例**:


```javascript
{
	"createBy": "",
	"createTime": "",
	"id": "",
	"ruleCode": "",
	"ruleDescription": "",
	"ruleJson": "",
	"ruleName": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysCheckRule|编码校验规则|body|true|sys_check_rule对象|sys_check_rule对象|
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;id|主键id||false|string||
|&emsp;&emsp;ruleCode|规则Code||false|string||
|&emsp;&emsp;ruleDescription|规则描述||false|string||
|&emsp;&emsp;ruleJson|规则JSON||false|string||
|&emsp;&emsp;ruleName|规则名称||false|string||
|&emsp;&emsp;updateBy|更新人||false|string||
|&emsp;&emsp;updateTime|更新时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 编码校验规则-通过Code校验传入的值


**接口地址**:`/fastrun/sys/checkRule/checkByCode`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:编码校验规则-通过Code校验传入的值


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ruleCode|ruleCode|query|true|string||
|value|value|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 编码校验规则-通过id删除


**接口地址**:`/fastrun/sys/checkRule/delete`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:编码校验规则-通过id删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 编码校验规则-批量删除


**接口地址**:`/fastrun/sys/checkRule/deleteBatch`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:编码校验规则-批量删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 编码校验规则-编辑


**接口地址**:`/fastrun/sys/checkRule/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:编码校验规则-编辑


**请求示例**:


```javascript
{
	"createBy": "",
	"createTime": "",
	"id": "",
	"ruleCode": "",
	"ruleDescription": "",
	"ruleJson": "",
	"ruleName": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysCheckRule|编码校验规则|body|true|sys_check_rule对象|sys_check_rule对象|
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;id|主键id||false|string||
|&emsp;&emsp;ruleCode|规则Code||false|string||
|&emsp;&emsp;ruleDescription|规则描述||false|string||
|&emsp;&emsp;ruleJson|规则JSON||false|string||
|&emsp;&emsp;ruleName|规则名称||false|string||
|&emsp;&emsp;updateBy|更新人||false|string||
|&emsp;&emsp;updateTime|更新时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 编码校验规则-分页列表查询


**接口地址**:`/fastrun/sys/checkRule/list`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:编码校验规则-分页列表查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy|创建人|query|false|string||
|createTime|创建时间|query|false|string(date-time)||
|id|主键id|query|false|string||
|pageNo|pageNo|query|false|integer(int32)||
|pageSize|pageSize|query|false|integer(int32)||
|ruleCode|规则Code|query|false|string||
|ruleDescription|规则描述|query|false|string||
|ruleJson|规则JSON|query|false|string||
|ruleName|规则名称|query|false|string||
|updateBy|更新人|query|false|string||
|updateTime|更新时间|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 编码校验规则-通过id查询


**接口地址**:`/fastrun/sys/checkRule/queryById`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:编码校验规则-通过id查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 职务表


## 职务表-添加


**接口地址**:`/fastrun/sys/position/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:职务表-添加


**请求示例**:


```javascript
{
	"code": "",
	"companyId": "",
	"createBy": "",
	"createTime": "",
	"id": "",
	"name": "",
	"postRank": "",
	"sysOrgCode": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysPosition|职务表|body|true|sys_position对象|sys_position对象|
|&emsp;&emsp;code|职务编码||false|string||
|&emsp;&emsp;companyId|公司id||false|string||
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;name|职务名称||false|string||
|&emsp;&emsp;postRank|职级||false|string||
|&emsp;&emsp;sysOrgCode|组织机构编码||false|string||
|&emsp;&emsp;updateBy|修改人||false|string||
|&emsp;&emsp;updateTime|修改时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«sys_position对象»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|sys_position对象|sys_position对象|
|&emsp;&emsp;code|职务编码|string||
|&emsp;&emsp;companyId|公司id|string||
|&emsp;&emsp;createBy|创建人|string||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;id|id|string||
|&emsp;&emsp;name|职务名称|string||
|&emsp;&emsp;postRank|职级|string||
|&emsp;&emsp;sysOrgCode|组织机构编码|string||
|&emsp;&emsp;updateBy|修改人|string||
|&emsp;&emsp;updateTime|修改时间|string(date-time)||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {
		"code": "",
		"companyId": "",
		"createBy": "",
		"createTime": "",
		"id": "",
		"name": "",
		"postRank": "",
		"sysOrgCode": "",
		"updateBy": "",
		"updateTime": ""
	},
	"success": true,
	"timestamp": 0
}
```


## 职务表-通过id删除


**接口地址**:`/fastrun/sys/position/delete`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:职务表-通过id删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 职务表-批量删除


**接口地址**:`/fastrun/sys/position/deleteBatch`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:职务表-批量删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«sys_position对象»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|sys_position对象|sys_position对象|
|&emsp;&emsp;code|职务编码|string||
|&emsp;&emsp;companyId|公司id|string||
|&emsp;&emsp;createBy|创建人|string||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;id|id|string||
|&emsp;&emsp;name|职务名称|string||
|&emsp;&emsp;postRank|职级|string||
|&emsp;&emsp;sysOrgCode|组织机构编码|string||
|&emsp;&emsp;updateBy|修改人|string||
|&emsp;&emsp;updateTime|修改时间|string(date-time)||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {
		"code": "",
		"companyId": "",
		"createBy": "",
		"createTime": "",
		"id": "",
		"name": "",
		"postRank": "",
		"sysOrgCode": "",
		"updateBy": "",
		"updateTime": ""
	},
	"success": true,
	"timestamp": 0
}
```


## 职务表-编辑


**接口地址**:`/fastrun/sys/position/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:职务表-编辑


**请求示例**:


```javascript
{
	"code": "",
	"companyId": "",
	"createBy": "",
	"createTime": "",
	"id": "",
	"name": "",
	"postRank": "",
	"sysOrgCode": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysPosition|职务表|body|true|sys_position对象|sys_position对象|
|&emsp;&emsp;code|职务编码||false|string||
|&emsp;&emsp;companyId|公司id||false|string||
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;name|职务名称||false|string||
|&emsp;&emsp;postRank|职级||false|string||
|&emsp;&emsp;sysOrgCode|组织机构编码||false|string||
|&emsp;&emsp;updateBy|修改人||false|string||
|&emsp;&emsp;updateTime|修改时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«sys_position对象»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|sys_position对象|sys_position对象|
|&emsp;&emsp;code|职务编码|string||
|&emsp;&emsp;companyId|公司id|string||
|&emsp;&emsp;createBy|创建人|string||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;id|id|string||
|&emsp;&emsp;name|职务名称|string||
|&emsp;&emsp;postRank|职级|string||
|&emsp;&emsp;sysOrgCode|组织机构编码|string||
|&emsp;&emsp;updateBy|修改人|string||
|&emsp;&emsp;updateTime|修改时间|string(date-time)||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {
		"code": "",
		"companyId": "",
		"createBy": "",
		"createTime": "",
		"id": "",
		"name": "",
		"postRank": "",
		"sysOrgCode": "",
		"updateBy": "",
		"updateTime": ""
	},
	"success": true,
	"timestamp": 0
}
```


## 职务表-分页列表查询


**接口地址**:`/fastrun/sys/position/list`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:职务表-分页列表查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|code|职务编码|query|false|string||
|companyId|公司id|query|false|string||
|createBy|创建人|query|false|string||
|createTime|创建时间|query|false|string(date-time)||
|id|id|query|false|string||
|name|职务名称|query|false|string||
|pageNo|pageNo|query|false|integer(int32)||
|pageSize|pageSize|query|false|integer(int32)||
|postRank|职级|query|false|string||
|sysOrgCode|组织机构编码|query|false|string||
|updateBy|修改人|query|false|string||
|updateTime|修改时间|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«IPage«sys_position对象»»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|IPage«sys_position对象»|IPage«sys_position对象»|
|&emsp;&emsp;current||integer(int64)||
|&emsp;&emsp;hitCount||boolean||
|&emsp;&emsp;pages||integer(int64)||
|&emsp;&emsp;records||array|sys_position对象|
|&emsp;&emsp;&emsp;&emsp;code|职务编码|string||
|&emsp;&emsp;&emsp;&emsp;companyId|公司id|string||
|&emsp;&emsp;&emsp;&emsp;createBy|创建人|string||
|&emsp;&emsp;&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;id|id|string||
|&emsp;&emsp;&emsp;&emsp;name|职务名称|string||
|&emsp;&emsp;&emsp;&emsp;postRank|职级|string||
|&emsp;&emsp;&emsp;&emsp;sysOrgCode|组织机构编码|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|修改人|string||
|&emsp;&emsp;&emsp;&emsp;updateTime|修改时间|string(date-time)||
|&emsp;&emsp;searchCount||boolean||
|&emsp;&emsp;size||integer(int64)||
|&emsp;&emsp;total||integer(int64)||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {
		"current": 0,
		"hitCount": true,
		"pages": 0,
		"records": [
			{
				"code": "",
				"companyId": "",
				"createBy": "",
				"createTime": "",
				"id": "",
				"name": "",
				"postRank": "",
				"sysOrgCode": "",
				"updateBy": "",
				"updateTime": ""
			}
		],
		"searchCount": true,
		"size": 0,
		"total": 0
	},
	"success": true,
	"timestamp": 0
}
```


## 职务表-通过code查询


**接口地址**:`/fastrun/sys/position/queryByCode`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:职务表-通过code查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|code|code|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«sys_position对象»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|sys_position对象|sys_position对象|
|&emsp;&emsp;code|职务编码|string||
|&emsp;&emsp;companyId|公司id|string||
|&emsp;&emsp;createBy|创建人|string||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;id|id|string||
|&emsp;&emsp;name|职务名称|string||
|&emsp;&emsp;postRank|职级|string||
|&emsp;&emsp;sysOrgCode|组织机构编码|string||
|&emsp;&emsp;updateBy|修改人|string||
|&emsp;&emsp;updateTime|修改时间|string(date-time)||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {
		"code": "",
		"companyId": "",
		"createBy": "",
		"createTime": "",
		"id": "",
		"name": "",
		"postRank": "",
		"sysOrgCode": "",
		"updateBy": "",
		"updateTime": ""
	},
	"success": true,
	"timestamp": 0
}
```


## 职务表-通过id查询


**接口地址**:`/fastrun/sys/position/queryById`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:职务表-通过id查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«sys_position对象»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|sys_position对象|sys_position对象|
|&emsp;&emsp;code|职务编码|string||
|&emsp;&emsp;companyId|公司id|string||
|&emsp;&emsp;createBy|创建人|string||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;id|id|string||
|&emsp;&emsp;name|职务名称|string||
|&emsp;&emsp;postRank|职级|string||
|&emsp;&emsp;sysOrgCode|组织机构编码|string||
|&emsp;&emsp;updateBy|修改人|string||
|&emsp;&emsp;updateTime|修改时间|string(date-time)||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {
		"code": "",
		"companyId": "",
		"createBy": "",
		"createTime": "",
		"id": "",
		"name": "",
		"postRank": "",
		"sysOrgCode": "",
		"updateBy": "",
		"updateTime": ""
	},
	"success": true,
	"timestamp": 0
}
```


# 部门权限表


## 部门权限表-添加


**接口地址**:`/fastrun/sys/sysDepartPermission/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:部门权限表-添加


**请求示例**:


```javascript
{
	"dataRuleIds": "",
	"departId": "",
	"id": "",
	"permissionId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysDepartPermission|部门权限表|body|true|sys_depart_permission对象|sys_depart_permission对象|
|&emsp;&emsp;dataRuleIds|数据规则id||false|string||
|&emsp;&emsp;departId|部门id||false|string||
|&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;permissionId|权限id||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门权限表-通过id删除


**接口地址**:`/fastrun/sys/sysDepartPermission/delete`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:部门权限表-通过id删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门权限表-批量删除


**接口地址**:`/fastrun/sys/sysDepartPermission/deleteBatch`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:部门权限表-批量删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门权限表-编辑


**接口地址**:`/fastrun/sys/sysDepartPermission/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:部门权限表-编辑


**请求示例**:


```javascript
{
	"dataRuleIds": "",
	"departId": "",
	"id": "",
	"permissionId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysDepartPermission|部门权限表|body|true|sys_depart_permission对象|sys_depart_permission对象|
|&emsp;&emsp;dataRuleIds|数据规则id||false|string||
|&emsp;&emsp;departId|部门id||false|string||
|&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;permissionId|权限id||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门权限表-分页列表查询


**接口地址**:`/fastrun/sys/sysDepartPermission/list`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:部门权限表-分页列表查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|dataRuleIds|数据规则id|query|false|string||
|departId|部门id|query|false|string||
|id|id|query|false|string||
|pageNo|pageNo|query|false|integer(int32)||
|pageSize|pageSize|query|false|integer(int32)||
|permissionId|权限id|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门权限表-通过id查询


**接口地址**:`/fastrun/sys/sysDepartPermission/queryById`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:部门权限表-通过id查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 部门角色


## 部门角色-添加


**接口地址**:`/fastrun/sys/sysDepartRole/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:部门角色-添加


**请求示例**:


```javascript
{
	"createBy": "",
	"createTime": "",
	"departId": "",
	"description": "",
	"id": "",
	"roleCode": "",
	"roleName": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysDepartRole|部门角色|body|true|sys_depart_role对象|sys_depart_role对象|
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;departId|部门id||false|string||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;roleCode|部门角色编码||false|string||
|&emsp;&emsp;roleName|部门角色名称||false|string||
|&emsp;&emsp;updateBy|更新人||false|string||
|&emsp;&emsp;updateTime|更新时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门角色-通过id删除


**接口地址**:`/fastrun/sys/sysDepartRole/delete`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:部门角色-通过id删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门角色-批量删除


**接口地址**:`/fastrun/sys/sysDepartRole/deleteBatch`


**请求方式**:`DELETE`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:部门角色-批量删除


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|204|No Content||
|401|Unauthorized||
|403|Forbidden||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门角色-编辑


**接口地址**:`/fastrun/sys/sysDepartRole/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:部门角色-编辑


**请求示例**:


```javascript
{
	"createBy": "",
	"createTime": "",
	"departId": "",
	"description": "",
	"id": "",
	"roleCode": "",
	"roleName": "",
	"updateBy": "",
	"updateTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|sysDepartRole|部门角色|body|true|sys_depart_role对象|sys_depart_role对象|
|&emsp;&emsp;createBy|创建人||false|string||
|&emsp;&emsp;createTime|创建时间||false|string(date-time)||
|&emsp;&emsp;departId|部门id||false|string||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;roleCode|部门角色编码||false|string||
|&emsp;&emsp;roleName|部门角色名称||false|string||
|&emsp;&emsp;updateBy|更新人||false|string||
|&emsp;&emsp;updateTime|更新时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门角色-分页列表查询


**接口地址**:`/fastrun/sys/sysDepartRole/list`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:部门角色-分页列表查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy|创建人|query|false|string||
|createTime|创建时间|query|false|string(date-time)||
|departId|部门id|query|false|string||
|deptId|deptId|query|false|string||
|description|描述|query|false|string||
|id|id|query|false|string||
|pageNo|pageNo|query|false|integer(int32)||
|pageSize|pageSize|query|false|integer(int32)||
|roleCode|部门角色编码|query|false|string||
|roleName|部门角色名称|query|false|string||
|updateBy|更新人|query|false|string||
|updateTime|更新时间|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


## 部门角色-通过id查询


**接口地址**:`/fastrun/sys/sysDepartRole/queryById`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:部门角色-通过id查询


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```


# 重复校验


## 重复校验接口


**接口地址**:`/fastrun/sys/duplicate/check`


**请求方式**:`GET`


**请求数据类型**:`*`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | in    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|dataId|数据ID|query|false|string||
|fieldName|字段名|query|false|string||
|fieldVal|字段值|query|false|string||
|tableName|表名|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|接口返回对象«object»|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|返回代码|integer(int32)|integer(int32)|
|message|返回处理消息|string||
|result|返回数据对象|object||
|success|成功标志|boolean||
|timestamp|时间戳|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"code": 0,
	"message": "",
	"result": {},
	"success": true,
	"timestamp": 0
}
```