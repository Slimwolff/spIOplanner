_global_cond_ = False

global_data = {}

data_boilerplate = {
    "column": "",
    "max_char": -1,
    "reduceLast": -1,
    "remove": "",
    "$": []
}

class Boilerplate:
    def __init__(self, column="", max_char=-1, reduceLast=-1, remove=""):
        self.column = column
        self.max_char = max_char
        self.reduceLast = reduceLast
        self.remove = remove
        self.content = []