import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from sqlalchemy.exc import IntegrityError
from datetime import datetime


basedir= os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# 启用这一段是sqlite
# basedir = os.path.abspath(os.path.dirname(__name__))
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#    'sqlite:///' + os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 启用这一段是mysql+mysqldb
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:test@127.0.0.1/restful_db'
app.config.from_pyfile('../config.py', silent=True)

# 这一段是swagger相关，暂时不启用
# app.config.update({
#     'APISPEC_SPEC': APISpec(
#         title='Flask Restful API',
#         version='v1',
#         plugins=[MarshmallowPlugin()],
#         openapi_version='2.0.0'
#     ),
#     'APISPEC_SWAGGER_URL': '/swagger/',
#     'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
# })

api = Api(app, catch_all_404s=True)
db = SQLAlchemy(app)

# 测试mysql是否正常连接
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute("select 1")
#         print(rs.fetchone())

# # 创建instance文件夹，似乎没用
# try:
#     os.makedirs(app.instance_path)
# except OSError:
#     pass
    
# @app.route('/test/<pill_id>')
# def pill_test(pill_id):
#     try:
#         # 创建一个新的药品实例
#         from models.pillm import PillModel
#         pill = PillModel(
#             name=f"测试药物{pill_id}",
#             breakfast_piece=1,
#             lunch_piece=2,
#             supper_piece=3,
#             update_time=datetime.now(),
#         )
#         db.session.add(pill)
#         db.session.commit()
#         return 'OK'

    # except IntegrityError:
    #     db.session.rollback()
    #     return "name existed" # 发生异常时回滚

@app.route('/')
def hello_world():
    return 'Welcome!'

from resources import pillr
from resources import userr

# swagger = Swagger(app)
