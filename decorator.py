from functools import wraps
from  flask import session ,url_for,redirect

"""
很多地方会验证登录状态，每个地方在html中去判断很麻烦，所有用装饰器来实现登录的验证
"""
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)  # 需要返回
        else:
            return redirect(url_for('login'))
    return wrapper
"""
index =login_required(index)=wrapper
index()=wrapper()
print('hello')

"""