def decorated_function(*args,**kwargs):#这个是原函数，包括两个参数,这两个参数作用分别有各自的作用如下：
    print("args:",args)
    print("kwargs:",kwargs)


decorated_function(1,2,3,name="liubei",age=25)

