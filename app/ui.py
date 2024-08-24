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

        

def cmd( ):
    return print('AAA')

class Frame:
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

class Top_panel:
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        self.frame.pack(side='top')
        self.func = cmd
        self.btn = Button(self.frame,"Submit sheets")
        self.btn.pack(ipadx=10,ipady=10)
        self.checked = tk.BooleanVar()
        self.checkbox = Checkbox(self.frame, text="Ignorar Primeira Coluna",var=self.checked)        
        self.checkbox.pack(side="left")

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def button_config(self, **kwargs):
        self.btn.config(**kwargs)

class Left_panel:
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        self.listbox = Listbox(parent=parent, width=50, height=80)
        self.listbox.pack(pady=20, padx=20)
        self.bind = self.listbox.bind()


    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

class Entry:
    def __init__(self, parent):
        self.entry = tk.Entry(parent)

    def pack(self, **kwargs):
        self.entry.pack(**kwargs)

    def grid(self, **kwargs):
        self.entry.grid(**kwargs)

    def get(self):
        return self.entry.get()

class Label:
    def __init__(self, parent, text):
        self.label = tk.Label(parent,text=text)

    def pack(self, **kwargs):
        self.label.pack(**kwargs)

    def grid(self, **kwargs):
        self.label.grid(**kwargs)

    def get(self):
        return self.label.get()
    
class Button:
    def __init__(self, parent, text):
        self.button = tk.Button(parent, text=text, background="green")
    
    def pack(self, **kwargs):
        self.button.pack(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

    def config(self, **kwargs):
        self.button.config(**kwargs)

class Checkbox:
    def __init__(self, parent, text, var):
        self.checkbutton = tk.Checkbutton(master=parent, text=text, variable=var)

    def pack(self, **kwargs):
        self.checkbutton.pack(**kwargs)

    def grid(self, **kwargs):
        self.checkbutton.grid(**kwargs)  
    
    

class Listbox:
    def __init__(self, parent, **kwargs):
        self.listbox = tk.Listbox(parent, **kwargs)

    def pack(self, **kwargs):
        self.listbox.pack(**kwargs)

    def grid(self, **kwargs):
        self.listbox.grid(**kwargs)

    def delete(self):
        self.listbox.delete(0, tk.END)

    def insert(self, s, e):
        self.listbox.insert(s, e)

    def bind(self, **kwargs):
        return self.listbox.bind(**kwargs)
    
    def curselection(self):
        return self.listbox.curselection()

class Dropdown:
    def __init__(self, parent, **kwargs):
        self.dropdown = ttk.Combobox(parent, **kwargs)

    def pack(self, **kwargs):
        self.dropdown.pack(**kwargs)

    def grid(self, **kwargs):
        self.dropdown.grid(**kwargs)

    def current(self, i: int):
        self.dropdown.current(i)

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