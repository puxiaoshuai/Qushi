# 主要是进行表单的验证


from wtforms import validators, fields, widgets, Form


class RegisterForm(Form):
    telephone = fields.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='电话号码不能为空'),
            validators.length(min=6, max=11, message='电话号长度不满足条件')
        ],
        widget=widgets.TextInput(),  # 表示是一个文本控件
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入用户名',
            'required': '',
            'autofocus': ''
        }
    )
    username = fields.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
        ],
        widget=widgets.TextInput(),
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入用户名字',
            'required': '',
            'autofocus': ''
        }
    )
    password1 = fields.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.length(min=6, message='密码必须大于%(min)d位')
        ],
        widget=widgets.PasswordInput(),
        render_kw={
            'class': 'form-control',
            'placeholder': '请确认密码',
            'required': '',
            'autofocus': ''
        }
    )

    password2 = fields.PasswordField(
        label='确认密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.length(min=6, message='密码必须大于%(min)d位')
        ],
        widget=widgets.PasswordInput(),
        render_kw={
            'class': 'form-control',
            'placeholder': '请确认密码',
            'required': '',
            'autofocus': ''
        }
    )
