from flask import Flask,render_template,request,redirect,url_for,session
from  models import User,Question
from exts import db
import config
from decorator import login_required
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app=app)




@app.route('/')
def index():
    content={
        'questions':Question.query.order_by('-create_time').all()#-create_time就是最新时间在前
    }
    # **传入关键字参数
    return render_template('home.html',**content)

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="GET":
        return  render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user=User.query.filter(User.telephone==telephone,User.password==password).first()
        if user:
            # 保存cooker,告诉客户端是谁登录，设置时间31内
            session['user_id']=user.id
            session.permanent=True#设置时间31天内
            return redirect(url_for('index'))
        else:
            return "手机号码或者密码错误"
@app.route('/logout')
def logout():
    #session.pop('user_id')
    # del session.('user_id')
    session.clear()
    return redirect(url_for('login'))





@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=="GET":
        return  render_template('register.html')
    else:
        telephone=request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #手机后面验证
        user=User.query.filter(User.telephone==telephone).first()
        if user:
            return u"改手机号码已被注册"
        else:
            if password1!=password2:
                return u"两次密码不相等，请核对"
            else:
                user=User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                #成功之后，跳转到登录界面
                return redirect(url_for('login'))

@app.context_processor
def my_content_processor():
    user_id=session.get('user_id')#session['user_id']没有会抛异常
    if user_id:
        user=User.query.filter(User.id==user_id).first()
        return {'user':user}
    else:
        #没在登录状态，不存在，也要强制返回{}
        return {}

@app.route('/question',methods=['GET',"POST"])
@login_required
def question():
    if request.method=="GET":
        return render_template('question.html')
    else:
        title=request.form.get('title')
        content=request.form.get('content')
        user_id=session.get('user_id')
        ques=Question(title=title,content=content)
        user=User.query.filter(User.id==user_id).first()
        ques.author=user
        #question.author_id=user_id 不用查询，直接写user_id应该也行吧
        db.session.add(ques)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/detail/<question_id>')
def detail(question_id):
    detail_info=Question.query.filter(Question.id==question_id).first()
    return render_template('detail.html',data=detail_info)



if __name__ == '__main__':
    app.run()
