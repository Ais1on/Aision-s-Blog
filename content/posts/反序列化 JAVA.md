+++
title = "反序列化 JAVA"
date = 2022-01-01T10:00:00+08:00
draft = false
description = "Java 反序列化基础、识别特征与练习记录。"
tags = []
+++
![](images/posts/反序列化_JAVA/1662089253987-a96e4c33-99e1-4dbe-a13f-010c9b63e46f-9014dda688.png)WRITEOBJECT O 注:该方法对参数指定的OBJ对象进行序列化,把字节序列写到一个目标输出流中 按JAVA的标准约定是给文件一个.SER扩展名 反序列化:0BJECTINOUTSTREAM类->READOBJECT O 注:该方法从一个源输入流中读取宇节序列,再把它们反序列化为一个对象,并将其返回. 
![](images/posts/反序列化_JAVA/1662089390840-6d5f2db8-8f07-4071-965d-bb4ffe12733f-f4bc2279f1.png)
![](images/posts/反序列化_JAVA/1662090797400-aa636935-3ac1-4a72-ac41-876dd5456874-68c2dfde1c.png)TX话乱码数据序列化 WIRTEOBJECT TXT乱码数据->XIAODI 反序列化 READOBJECT 100% LROOABXQAVKIMIHINDSBKZXNICMIHBGI62SBIZSBKB3DULCBJIHNOYWXSIGJY291ZSBTB3JIHBVDZVYZNVSIHROY W4GEW911GNHBIBWB3NZAWJSESBPBWFNAW5I 两步:序列化+BASE64 我要攻击它,我该如何构造PAYLOAD  IPCONFIG对方回显要考虑 反弹SHELL IPCONFIG三>序列化->BASE64-ROOAB格式字符串最终PAYLOAD 
![](images/posts/反序列化_JAVA/1662091036342-b9b7b354-e108-4e7f-9356-15edb50894cc-1f063fdb00.png)

## 例题

![](images/posts/反序列化_JAVA/1662091798051-8c4fa322-2077-4a6f-a214-d424437c8a67-5976dc3830.png)

![](images/posts/反序列化_JAVA/1662093946255-755a4f44-27d7-47c4-a2e3-94673431da66-4767c00934.png)

## 访问链接后 题目有附件 是一些class

![](images/posts/反序列化_JAVA/1662091842210-a7a45b4d-ee93-4dd0-841e-3a03c412b504-d914913366.png)

![](images/posts/反序列化_JAVA/1662091816207-b123f732-e6e4-4826-bb9a-39b90c010cc8-b95c776e3a.png)

## 用java打开

![](images/posts/反序列化_JAVA/1662091906171-b665b2ba-ca7b-4f55-8f75-052d4b96940e-e81b425daf.png)

## Post 抓包访问/common/test/sqlDict
![](images/posts/反序列化_JAVA/1662092494930-c6ea7195-c8b2-488a-8eeb-d4c65b3bac53-2a6d757cd7.png)

![](images/posts/反序列化_JAVA/1662092573922-26518372-e8ce-47cb-bfed-a1db492b9584-74e61d6081.png)

## 数据库名词为myapp

![](images/posts/反序列化_JAVA/1662093724435-f40beaa0-23aa-4f6e-b0a5-9bef4b58f74d-5bfc5b7d91.png)

## 拼接sql语句进行注入 用户为cthhub  密码为ctfhub_30284_3312

![](images/posts/反序列化_JAVA/1662093826510-6aac9210-45c5-4c23-abbc-28e9ab9a003d-faf08b33cc.png)

## 有swagger开发接口 默认地址为如下

![](images/posts/反序列化_JAVA/1662093987038-369ebfda-14fc-482b-9d3f-fcc173ccfe10-af5049a29e.png)

![](images/posts/反序列化_JAVA/1662093962304-dccccaee-feb5-4e9c-87fe-2f9f363d177d-126e51d8fe.png)
![](images/posts/反序列化_JAVA/1662094038841-aa9256c1-ded6-415d-bc1c-0715b0edf350-2f3c69eb92.png)

## 进行登录

![](images/posts/反序列化_JAVA/1662094119641-9d8094f5-bc6a-4923-aa9e-f84328de9a4f-4378bea5a9.png)

![](images/posts/反序列化_JAVA/1662094107534-0fadcc95-f90e-4a57-959b-2ca686e1266f-d4bfc3926c.png)
![](images/posts/反序列化_JAVA/1662094181557-769ecb23-e150-443a-ae21-7a6c72dc1b17-4dfb6e0fad.png)

## 获取当前用户信息 将序列化的data写入

![](images/posts/反序列化_JAVA/1662094225068-71492be6-8dd7-4f83-82e5-d2fd6d939a1f-909001fdea.png)
![](images/posts/反序列化_JAVA/1662094322726-603f4ebe-79f1-4dc7-a8e5-684f908ef81d-0ee58245e0.png)
![](images/posts/反序列化_JAVA/1662094331928-10c87a07-ae4e-4e9e-b8d1-9403e37a549f-dbf73f0aaf.png)

## 复合序列化和反序列化过程

![](images/posts/反序列化_JAVA/1662094731971-c8b8e214-97f0-499e-84f6-edd4f17d54a7-c4149f65c0.png)

需要服务器监听端口 然后反弹shell 利用

ysoserial工具生成payload
