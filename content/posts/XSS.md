+++
title = "XSS"
date = 2022-09-21T10:00:00+08:00
draft = false
description = "XSS 漏洞的利用方式、平台使用和常见思路整理。"
tags = []
+++
利用XSS平台进行获取cookie 等一系列操作

![](images/posts/XSS/1659256378269-9691c227-75e9-417f-ab83-2bd56f17d401-933d517bd1.png)

与管理员交互的页面  XSS 的作用才能发挥到最大

![](images/posts/XSS/1659439538981-a636136b-4e65-4013-8005-fc274488c447-fb4e41d2a0.png)

![](images/posts/XSS/1659439985145-c9011ca9-2ee9-4af4-9ea0-7f43eb550677-91b4051482.png)

## XSS原理和危害
#创建一个回显传参的脚本

![](images/posts/XSS/1659256467367-3a488f74-0d8c-433b-86d3-d3137dae25d4-4795a58996.webp)

#浏览器访问

![](images/posts/XSS/1659256640122-d99b4b71-1538-41fb-a591-b4f745000cf5-4ea0b8e495.png)

---传参：`&lt;script&gt;alert("你好")&lt;/script&gt;`，发现产生弹窗。这里就是XSS的本质：如果对方对参数进行回显，传递的参数代码会被回显者的浏览器执行。即对文件显示过程出现了问题。

---本质为前端漏洞，一般执行为js代码，因此危害不大。

## XSS 跨站漏洞分类

![](images/posts/XSS/1659257846819-02f9fb00-e28c-404f-a862-9dec4ba01df7-afdf17783c.png)

### 反射型

![](images/posts/XSS/1659257338557-8d25a32a-ef6d-47c7-9c4e-824a951e4dd2-1571a21961.png)

### 存储型
＃写入XSS

---和反射型的区别：反射型回显参数，每次传递的参数不一样，XSS效果也就不一样（如果不构造，不会触发漏洞）。但是存储型不一样，写入了之后，每次访问留言板，都会触发XSS（相当于存储到了网站的数据库，攻击会持续到数据在数据库中被删除，危害性更大）

### DOM型 前端处理 反射型的一种

![](images/posts/XSS/1659257512828-0fd23978-64bc-4920-8167-3f4e06d927b5-d096d560e6.png)

#这种网址没有改变  通过html代码实现

![](images/posts/XSS/1659257716959-a0b04aff-98a9-49da-93ba-8b6d82f1fd51-6511967172.png)

![](images/posts/XSS/1659257468135-7f492592-a425-43f8-b2b8-faf3bfa17d69-2498ce23b9.png)

## HTTP only
http only只是无法读取到cookie 但是脚本语句还是可以执行

![](images/posts/XSS/1659598417938-8cba06c1-4f3a-41f0-8c4c-886f133b4c78-3e64af8915.png)

## 表单劫持 登录框
#未保存密码读取

利用XSS 登陆时传数据包一份传到服务器 一份传到XSS平台 获取账号密码

#保存密码读取 （存在再浏览器中）

输入对应的字段名 （在已经执行XSS攻击的情况下）

![](images/posts/XSS/1659603560250-01c6382a-1191-476a-a0ad-08220de766c0-51db7a589e.png)

### XSS 绕过
[XSS.pdf](https://www.yuque.com/attachments/yuque/0/2022/pdf/26686608/1659601034355-08effcab-28a4-4cae-9572-cd64c6af3605.pdf)

### CSRF referer

![](images/posts/XSS/1659602285684-8c446275-6f9a-4248-85a7-b2903c290732-224412b106.png)

## XSS WAF拦截和修复

![](images/posts/XSS/1659697678244-fc57a4f2-d8dc-4b36-a85d-c29aacdaf8f9-ea2995f694.png)

### WAF拦截 使用特殊符号 或者 垃圾数据

![](images/posts/XSS/1659698073283-3b885bba-670b-4198-aeb6-5a4a98c212ad-acd636c33d.png)

Post 提交 前提是支持post提交

![](images/posts/XSS/1659699001388-a3776f59-a5b3-4c94-a70b-824d7a3c98a3-bc48e875cb.png)。

![](images/posts/XSS/1659699417552-619dac53-81c5-4089-9b96-48e79c11136b-ba2ed803fd.png)

### XSS修复
Java

![](images/posts/XSS/1659700366725-0482417b-39cc-45cc-9b4f-25e0edfd5879-181fe63ce8.png)
![](images/posts/XSS/1659700395821-ea2f827d-8556-414b-847e-ad802ff9bd7b-309ef75aa7.png)

PHP 等其他

![](images/posts/XSS/1659700445545-974f4a13-efee-4016-a845-99a45962356f-ca542ff1fc.png)
![](images/posts/XSS/1659700499930-26147b9a-66c9-421c-b3a0-8523cf50e5d1-c45e0d2877.png)
