### MySQL学习

#### 一、关系数据库

* 【目的】用于数据的持久化

* 【发展过程】：网状数据库 -> 层次数据库 -> 关系数据库 -> NoSQl数据库

* 【关系数据库特点】：
    1. 理论基础：集合论和关系代数
    2. 具体表象：二维表（行和列）
    3. 编程语言：结构化查询语言（SQL语言）     

* 【ER模型】：实体关系模型:  
    1. 实体
    2. 属性 
    3. 关系
    4. 重数

* 【关系数据库产品】
    1. Oracle
    2. DB2
    3. SQL Server
    4. MySQL
    5. PostgreSQL
    
#### 二、MySQL

* 【安装MySQL】：前往[MySQL官网](https://www.mysql.com/)下载安装文件，选择系统，版本，找到对应的下载链接

```bash
# linux
wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.26-1.el7.x86_64.rpm-bundle.tar
tar -xvf mysql-5.7.26-1.el7.x86_64.rpm-bundle.tar
# mac
# 略
# windows
# 略
```

* 【配置MySQL】：完成安装后，会生成配置文件：/etc/my.cnf

* 【启动MySQL】：通过用户+密码完成用户的登录，连接数据库

```bash
# 启动服务
service mysqld start
# 检查进程
pgrep mysqld
```
* 【使用MySQL客户端连接服务器】

```bash
# 初次连接，需找到默认密码
cat /var/log/mysqld.log | grep password
# 连接服务器：以root用户为例
mysql -u root -p
# 输入密码进行验证，完成对服务器的连接
```

* 【常用命令】
|命令|功能|备注|
|---|---|---|
|select version();|查看服务器版本||
|show databases;|查看所有数据库||
|use mysql|切换到指定数据库||
|show tabels;|查看数据库下的所有表|需要先进入数据库|
|quit;|退出数据库||

三、SQL
* 【基本操作】：DDL(数据定义语言)、DML(数据操作语言)、DCL(数据控制语言)
1. DDL：数据定义语言
