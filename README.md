# 爬虫分析系统——爬虫元服务
本系统由三部分组成：
- 爬虫元服务
- 分析元服务
- 告警元服务
本文将介绍爬虫元服务模块

# 简介
设计爬虫元服务,提供基础的爬虫服务，仅提供post和get功能，将页面源代码解析返回本地

url:http://10.153.115.14:7426/bug

msg:html.text
code:html
## get
```json
{
	"url": "",
	"domain": "",
	"code": 1
}
```
### demo
```json
{
	"url": "/software/25646124.html",
	"domain": "shouji.baidu.com",
	"code": 2
}
```

### 返回格式
```json
{
    "msg":"",
    "code": "",
    "status": ""
}
```


## post
```json
{
	"url":"",
	"domain":"",
	"code": ""
}
```
### demo
```json
{
	"url":"https://shouji.baidu.com/software/25646124.html",
	"domain":"shouji.baidu.com",
	"code": 1
}
```

### 返回格式
```json
{
    "msg":"",
    "code": "",
    "status": ""
}
```
