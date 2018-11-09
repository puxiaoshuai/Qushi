from  flask_script import Manager
from exts import db
from  flask_migrate import Migrate,MigrateCommand
from  manage_run import app
#迁移的话必须导入 models下的
from  models import User,Question,Answer
manager=Manager(app)
#使用migrte绑定app,db
migrate=Migrate(app=app,db=db)
#添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manager.run()