# Qushi
# 项目效果预览
![首页.png](https://upload-images.jianshu.io/upload_images/4908477-265c787aa2af852a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 功能点：
- 登录，注册功能。保存数据到数据库中
- 上传趣事，保存内容到数据库
- 详情中，能添加评论
待优化：对登录，注册，上传信息的验证
![发布.png](https://upload-images.jianshu.io/upload_images/4908477-c22d88bfb62162ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![详情.png](https://upload-images.jianshu.io/upload_images/4908477-9e14fbe2d397281e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 知识点
- 表单提交，get,post请求处理
- 数据库迁移
- 数据的查询过滤
- 装饰器，限制登录
- html 排版布局
- 上下文处理钩子函数
- jinji2模板基本使用
- flask-scripts  命令管理
...
#  使用方式
- git  clone 当前项目
- 虚拟环境下 pip install -r requirements.txt
- 在本地创建自己的数据库qushi
- 在config.py中更改数据库密码
- 执行 python manage.py db upgrade ,就能生成表了
- 运行 flaskdemo.py  (pychorm下直接点运行)
-------------------------------------

