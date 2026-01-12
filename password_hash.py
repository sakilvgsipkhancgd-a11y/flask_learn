import hashlib
def hash_string(text:str,algorithm='sha256') -> str:
    #对字符串编码
    encoded_text = text.encode('utf-8')
    #创建哈希对象
    data = hashlib.new(algorithm)
    #更新哈希对象
    data.update(encoded_text)
    #返回十六进制哈希值
    return data.hexdigest()

password1 = input("请输入您的密码：")
password2 = input("请再次输入您的密码：")
hashed_password1 = hash_string(password1)
hashed_password2 = hash_string(password2)
if hashed_password1 == hashed_password2:
    print("密码匹配！")
else:
    print("密码不匹配，请重试。")

