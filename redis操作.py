import redis
#像连接数据库一样链接redis服务器
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
    )
try:
    r.lpush('list1','123')#lpush是从左边插入数据
    r.lpush('list2','456')
    print("连接成功，已插入数据")
    print(r.rpop('list1'))#rpop是从右边取出数据
    print(r.rpop('list2'))
except redis.ConnectionError:
    print("连接失败，请检查Redis服务器是否运行")
#此场景可以模拟一个任务队列的简单实现，先插入的数据先处理，实现左进右出
