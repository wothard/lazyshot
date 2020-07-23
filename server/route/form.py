from flask import Blueprint

import form.struct

forms = Blueprint("forms", __name__, url_prefix="/form")


@forms.route('/')
def index():
    print(form.struct)
    return form.struct.FormStruct().incorporate_field([{
        "text": "fdgs", 
        "lang_type": "golang",
        "type": "int"
        }])
