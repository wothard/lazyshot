"""
test 2035
"""


class FormStruct():
    def __init__(self):
        self.head = 'type ^ {\n'
        self.foot = '}\n'

    def incorporate_field(self, field_list):
        inner_line = '【{}【{} `xorm:\"{}\" json:\"{}\"`\n'
        field_code = ''
        for i in field_list:
            field_code += inner_line.format(
                i["text"].capitalize(),
                i["lang_type"],
                i["type"],
                i["text"].lower()
            )
        return self.head + field_code + self.foot
