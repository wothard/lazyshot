from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from service.dblist import DBList

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wot:123@127.0.0.1/lazyshot'
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class HelloWorld(Resource):
    def get(self):
        # table_list = DBList().get_table_struct()
        table_list = DBList().get_table_struct_for_mysql()
        return {'hello': table_list}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
