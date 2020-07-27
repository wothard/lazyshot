from flask import Blueprint

import form.struct
from service.dblist import DBList

forms = Blueprint("forms", __name__, url_prefix="/form")

dbs = Blueprint('dblist', __name__, url_prefix="/db")


@forms.route('/')
def index():
    print(form.struct)
    return form.struct.FormStruct().incorporate_field([{
        "text": "fdgs",
        "lang_type": "golang",
        "type": "int"
    }])


@dbs.route('/')
def dbindex():
    try:
        table_list = DBList().get_table_struct_for_mysql()
        return {
            "code": 100,
            "data": table_list
        }
    except Exception as e:
        print(e)
        return {
            "code": 99,
            "data": "error"
        }
