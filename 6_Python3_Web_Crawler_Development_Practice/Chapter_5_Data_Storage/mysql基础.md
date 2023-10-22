# mysql基础

## 进入mysql

MySQL -u root -p 之后输入命令即可

## 查询现存的数据库命令

进入MySQL后输入

show databases;

分号不要忘了

## 创建一个数据库

进入MySQL后输入

create database 数据库名 DEFAULT CHARSET 编码集 COLLATE  排序规则;

create database 数据库名 DEFAULT CHARSET utf8 COLLATE  utf8_general_ci

分号不要忘了

## 删除数据库

进入MySQL后输入

drop database 数据库名 ;

分号不要忘了

## 进入数据库

进入MySQL后输入

use 数据库名 ;

分号不要忘了

### 查看该数据库下的表

show tables;

## 通过python使用mysql

所有的查询都要加一句cursor.fetchall()以获取查询结果

所有的新增，修改，删除命令都有加一句cursor.commit()以将修改提交到终端

## 在一个数据库中创建表

进入MySQL后输入

先输入 use 数据库名 ; 进入数据库

之后输入 create table 表名(

列名 类型，

列名 类型，

列名 类型，

.....

)default charset=utf8;

分号不要忘了

eg：

use db1;

create table tb1(

id int not null auto-increment primary key，--primary key 不允许为空&自增&主键 且不能重复，类似于索引

name  varchar(16) not null， -- 长度最大为16，不允许为空

email varchar(32) null, --允许为空

age int default 3， -- 如果此行不赋值则默认为3

)default charset=utf8;

### 查看表

desc 表名;

### 一个表只能有一个自增列

### 删除一个表

进入数据库后输入

drop table 表名;

### 清空表中的数据

delete from 表名;

#### 添加列，前提是先进去到目标数据库中的目标表格

alter table 表名 add 列名 类型;

alter table 表名 add 列名 类型 DEFAULT 默认值;

alter table 表名 add 列名 类型 NOT NULL  DEFAULT 默认值;

alter table 表名 add 列名 类型 NOT NULL primary key  auto-increment;

#### 删除列

alter table 表名 drop column 列名;

#### 修改列 类型

alter table 表名 modify column 列名 类型;

#### 修改列 类型 + 名称

alter table 表名 change column 原列名 新列名 新类型;

#### 修改列 默认值

alter table 表名 alter 列名 SET DEFAULT 1000;

#### 删除列 默认值

alter table 表名 alter 列名 DROP DEFAULT ;

#### 添加主键

alter table 表名 add primary key(列名) ;

#### 删除主键

alter table 表名 drop primary key;

### 数据表的增删改查

#### 插入数据

insert into 表名(列名, 列名, 列名,) value(对应列的值, 对应列的值, 对应列的值,);

eg:

insert into tb1(name, password) values('沙丁鱼', '12138');

insert into tb1(name, password) values('沙丁鱼', '12138'),('罗非鱼', '21138'); -- 一次插入两行，多行就是依次往后面加

#### 删除数据

delete from 表名;

delete from 表名 where 条件;

eg:

delete from table1;

delete from table1 where name='沙丁鱼';

delete from table1 where name='沙丁鱼' and password='12138'; --这个where类似于if

delete from table1 where id > 9;

#### 修改数据

update 表名 set 列名= 值;

update 表名 set 列名= 值 where 条件;

eg:

update tb1 set name = '沙丁鱼';

update tb1 set name = '沙丁鱼' where id = 1;

update tb1 set age = age+1  where id = 2;

update users set name = concat(name,'123')  where id = 2; --concat一个拼接字符串的函数

#### 查询数据

select * from 表名;

select 列名,列名,列名, from 表名,表名,表名,;

select 列名,列名,as 别名，别名 from 表名,表名,;-- 别名相当于重命名

select * from 表名 where 条件;

eg:

select * from tb1;

select id, name, age from tb1;

select id, name ad n, age, from tb1;

select id, name ad n, age,111, from tb1;


select * from tb1 where id = 1;

select * from tb1 where id > 1;

select * from tb1 where id != 1;

select * from tb1 where name = '沙丁鱼' and password='123';
