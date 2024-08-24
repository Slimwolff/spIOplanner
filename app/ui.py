import tkinter as tk
from tkinter import Menu, filedialog, messagebox, ttk
from app.methods import Applogic

def od():
    pass

def sd():
    pass

class WidModify:
    def __init__(self, anywidget):
        self.any = anywidget
    def pack(self, **kwargs):
        self.any.pack(**kwargs)
    def grid(self, **kwargs):
        self.any.grid(**kwargs)

class MainFrame:
    def __init__(self, root, geometry):
        self.logic = Applogic(self)
        self.root = root
        self.root.title("SpreadSheets IO Importation")
        self.root.geometry(geometry)
        self.menu_bar = Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=od)
        self.file_menu.add_command(label="Save", command=sd)


        self.top = Top_panel(self.root, width=200, background='blue', height=150)
        self.top.pack(side='top', fill='x', expand=True)
        self.top.button.config(command=self.logic.load_sheet)

        self.left = Left_panel(self.root, width=300, height=600)
        self.left.pack(side='left', fill='both', expand=True)
        self.left.listbox.bind(sequence='<<ListboxSelect>>', func=self.logic.on_select)

        self.right = Right_panel(self.root, width=300, height=600)
        self.right.pack(side='right', fill='both', expand=True)
        
class Top_panel(WidModify):
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        super().__init__(self.frame)
        self.frame.pack(side='top')

        self.button = tk.Button(self.frame,text="Submit sheets")
        self.button.pack(ipadx=10,ipady=10)
        self.checked = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame, text="Ignorar Primeira Coluna",var=self.checked)        
        self.checkbox.pack(side="left")


class Left_panel(WidModify):
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        super().__init__(self.frame)

        self.listbox = tk.Listbox(parent, width=50, height=80)
        self.listbox.pack(pady=20, padx=20)


class Right_panel(WidModify):
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        super().__init__(self.frame)
        self.removeChar = Cont_label_input(self.frame, width=100, height=100)
        self.removeChar.pack(side='top', fill='x', expand=False)
        self.removeChar.label.config(text="Remover estes caracteres")


class Cont_label_input(WidModify):
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        super().__init__(self.frame)
        self.label = tk.Label(self.frame)
        self.entry = tk.Entry(self.frame)




class Data:
    def __init__(self):
        self._attributes = {}

    def __setitem__(self, key, value):
        self._attributes[key] = value

    def __getitem__(self, key):
        return self._attributes[key]
    
    def __getattr__(self, key):
        getattr(self, key)

    def __setattr__(self, key, value):
        if key == '_attributes':
            super().__setattr__(key, value)
        else:
            self._attributes[key] = value

    def keys(self):
        return self._attributes.keys()

    def values(self):
        return self._attributes.values()

    def items(self):
        return self._attributes.items()