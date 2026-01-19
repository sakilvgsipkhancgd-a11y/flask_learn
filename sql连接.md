import pymysql# 导入模块
"""
pymysql是python常用的链接数据库的第三方库，其中包含了众多类和方法，例如
connect和connection，下面将挑选一些常用的方法和类进行说明
1.pymysql.connect()创建数据库连接，返回一个connection对象
参数常常包括主机名host，端口port，用户名user，密码password，数据库名database以及字符编码类型charset，utf8mb4支持emoji
本函数为数据库操作入口，一切操作需建立在链接成功的基础上，如果未连接成功，会抛出pymysql.mysqlerror异常
2.connection对象，此对象代表一个数据库连接，常用方法有
.cursor()创建游标对象，用以执行语句connection.cursor()
创建了游标对象之后就可以用cursor.来执行任务，例如cursor.execute(...)表示执行一条sql语句，括号内部填写SQL语句
游标对象用来处理数据库内部事务，connect对象用来管理数据库，例如
connection.commit()提交方法，对于增删改查等，想要改变数据库内部必须要提交，否则不会真正写入数据库
connection.rollback()出错之后回滚
connection.close()关闭连接
3.cursor游标对象，如2中提到创建方法，此对象创建之后即可执行任务，方法为cursor.方法
务必使用参数化查询防止SQL注入，例如：
name = "'; DROP TABLE users; --"
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
这句代码在变量被代入执行时，sql语句默认分号作为结束符号，后面的不会执行，正确做法应该为：
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
# 或
cursor.execute("SELECT * FROM users WHERE name = %(name)s", {"name": name})
将变量通过占位符传入
4.上下文管理器
connection对象和cursor都可以通过上下文管理器关闭，代码示例如下文中代码


"""
#链接数据库
"""try:
    connection = pymysql.connect(
        host="localhost",#主机名
        port=3306,#端口号，默认3306
        user="root",#用户名
        password="cwbhyd",#密码
        database="myblog",#数据库名称
        charset='utf8mb4'#字符编码，utf8mb4可支持emoji字符
    )
    print("数据库连接成功")
    #2.创建游标对象
    cursor = connection.cursor()
    #3.执行查询
    cursor.execute("select * from poems;")
    results = cursor.fetchall()
    #打印结果
    for row in results:
        print(row)

except Exception as e:
    print("查询出错或者未查询到",e)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
        print("已关闭连接")"""
#用with上下文管理器更方便易用
try:
    with pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='cwbhyd',
        database='myblog',
        charset='utf8mb4'

    ) as connection:
        print("数据库连接成功")
        with connection.cursor() as cursor:
            cursor.execute("select * from poems;")
            results = cursor.fetchall()
            for row in results:
                print(row)

except Exception as e:
    print("无法连接或未查询到",e)
请帮我看一下本章数据库连接对其理解是否透彻
