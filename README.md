#READ ME
---
*writer:houyizhong*  

##Blog  
[Blog](http://www.jianshu.com/p/a2a3cab84869)的地址是<http://www.jianshu.com/p/a2a3cab84869>  
Github地址是<https://github.com/houyizhong/Employee_manager>

##说明  
本程序实现的是对员工信息数据库的查询，更新，删除和新增操作，语法类似SQL语法，具体操作语句可以参见**操作指南**。  

##程序结构  
|  
|--bin  
|----io.py  
|--core  
|----chushihua.py  
|----sel_module.py  
|----insert_module.py  
|----update_module.py  
|----delete_module.py  
|--database  
|----staff_table

###数据库数据如下  
|staff\_id  |name  |age  |phone  |dept  |enroll\_date  |
|-|-:|-:|-:|-:|-:|
|1|Alex Li|22|13612684608|IT|2013-04-01|
|2|Jack Wang|30|18613305112|HR|2015-05-03|
|3|Nick Cave|25|18962295184|Sales|2015-04-06|  



##运行  
解压文件之后运行/bin目录下的io.py文件，按操作指南语法输入语句  

##操作指南  
* 查询语句，支持以下三种方式，用空格分开，查询条件','分开  
select * from staff_table where age > 23  
select name,age from staff_table where dept = IT  
select name,phone from staff_table where enroll_date like 2015  

* 插入语句（可小写） INTO后面是key，按','分开，一一对应VALUES后面的值，其中phone键是唯一键，id自增无需输入  
INSERT INTO staff_table name,age,phone,dept,enroll_date VALUES   root,23,18000000,IT,2017-01-01  

* 更新语句，其中dept=market是更新项，前一个是key后一个是values，中间是=，dept = IT 是筛选，用空格分开  
update staff_table set dept=market where dept = IT  

* 删除语句，输入id即可删除  
delete from staff_table id 4  

* 初始化数据库  
chushihua  

* 退出  
q
