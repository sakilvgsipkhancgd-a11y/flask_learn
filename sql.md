sql是一种数据化查询语言
数据库常用名词：
database：数据库
table：表
COLUMN：列
row：行
record：记录
primary key:主键（非空且唯一的列或组合）
sql和其他语言一样，应该不使用关键字作为一些变量名，数据库名称，列名称，避免冲突
启动服务命令：sudo service mysql start
停止服务命令：sudo service mysql stop
查看服务状态命令：sudo service mysql status
登录mysql命令：mysql -u root -p
创建数据库：CREATE DATABASE 数据库名称;
一.查询语句
1.检索单个列：SELECT 列名 FROM 表名;--这句话表示查询某一列从某个表中
官方解释为利用select语句从Products表中检索一个名为prod_name的列，所需的列名写在select关键字之后，from关键字指出从那个表中检索数据
SELECT vend_id FROM Products;检索表Products中的vend_id列
SELECT DISTINCT vend_id FROM Products;表示检索表Products中的vend_id列，但不包含重复的项
SELECT vend_id FROM Products LIMIT 5;表示检索表Products中的vend_id列，并只显示前5条记录
SELECT prod_name FROM Products LIMIT 5 OFFSET 5;表示检索表Products中的prod_name列，并跳过前5条记录，显示接下来的5条记录
需要注意，第一个检索的行是第0行，而不是第一行，所以OFFSET 5表示跳过前5行，从第6行开始显示
SELECT prod_name FROM Products LIMIT 3,4;表示跳过前三行，从第四行开始显示4条记录
sql语句有两种注释方式：这是第一种，前面加上两条杠，如：--注释
还有一种是多行注释，是由/*和*/包围的注释，可以跨多行，如：
/*这样
还有这样*/
SELECT prod_name FROM Products ORDER BY prod_name;--表示检索某种的某个列，并将结果按照一定的规则排序，此句表示按照字母顺序对产品名称进行排序。并且在SELECT语句中ORDER BY必须为最后一个子句。否则会报错
SELECT prod_id,prod_name,prod_price FROM Products ORDER BY prod_price,prod_name;
/*注意此时后面列的顺序会影响排序规则，因此务必按照需要排序
的顺序来进行写语句，在本句中会先根据price列进行排序，然后基于排序后的值，再根据price列相
同的行进行name列的排序，这个子句要求price列需要有重复的值，这样才能再排序后再次进行排序。
除了直接使用列名，还支持使用相对位置，例如在表中id列的位置为1，name列的位置为2，price列的位置为3，则可以写成*/
SELECT prod_id,prod_name,prod_price FROM Products ORDER BY 3,2;
/*这种方式一般适用于列名较长的情况，一般
不使用,注意这个3和2是相对于检索的列的位置，而不是在表中的位置。*/
SELECT prod_id,prod_name,prod_price FROM Products ORDER BY 3 DESC;--DESC关键字表示降序排列
