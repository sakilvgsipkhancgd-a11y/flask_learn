import pymysql
from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
# 导入模块
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
        host=DB_HOST,
        port=3306,
        user=DB_USER,
        password=DB_PASSWORD,
        database='finance_db',
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




