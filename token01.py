#本代码用以生成随机token
import secrets
import string

def generate_password(length=32):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))


token = generate_password()
print(token)
