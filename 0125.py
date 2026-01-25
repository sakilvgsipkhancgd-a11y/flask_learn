import pymysql
from dotenv import load_dotenv
import os

load_dotenv()
#数据库配置参数
DB_CONFIG={
    'host':os.getenv('DB_HOST'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD'),
    'port':3306,
    'charset':'utf8mb4',
    'db':os.getenv('DB_NAME')
}

def connect_mysql():
    conn = pymysql.Connection(**DB_CONFIG)#创建连接对象

    return conn#返回连接对象

def select_data():
    with connect_mysql() as conn:#创建连接对象
        print('Connected to MySQL database')
        cur = conn.cursor()#创建游标对象
        cur.execute("SELECT * FROM Products")
        rows = cur.fetchall()#获取所有数据
        return rows


my_conn = select_data()
print(my_conn)
