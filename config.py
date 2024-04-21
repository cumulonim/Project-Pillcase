HOSTNAME = "127.0.0.1"
PORT = 3306
# MySQL监听的端口号默认3306
USERNAME = ""
PASSWORD = ""
# 发布时删除
DATABASE = "pilldb"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:3306/{DATABASE}?charset=utf8mb4"

SQLALCHEMY_TRACK_MODIFICATIONS = True #测试完改成False

# SWAGGER_TITLE = "API"
# SWAGGER_DESC = "API接口"
# # 地址，必须带上端口号
# SWAGGER_HOST = "localhost:5000"

    # 'APISPEC_SPEC': APISpec(
    #     title='Flask Restful API project',
    #     version='v1',
    #     plugins=[MarshmallowPlugin()],
    #     openapi_version='2.0.0'
    # ),
    # 'APISPEC_SWAGGER_URL': '/swagger/',
    # 'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
