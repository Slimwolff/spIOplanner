import tkinter as tk
from tkinter import ttk

class MainFrame:
    def __init__(self, root, geometry, master=None):
        self.root = root
        self.root.title("SpreadSheets IO Importation")
        self.root.geometry(geometry)
        self.mainloop = self.root.mainloop
        self.top = Top_panel(self.root, width=200, background='blue', height=150)
        self.top.pack(side='top', fill='x', expand=True)

        top = self.top

        print(top)
        # self.checked = tk.BooleanVar()
        # self.checkbox = Checkbox(parent=self.top, text="Ignorar Primeira Coluna",var=self.checked)        
        # self.checkbox.pack(side="left")

        

        # self.left = Frame(self.root,width=300, height=600)
        # self.left.pack(side='left', fill='both', expand=True)

        # self.right = Frame(self.root,width=300, height=600)
        # self.right.pack(side='right', fill='both', expand=True)

        

def cmd(msg: str ):
    return print(msg)

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
        self.btn = Button(self.frame,"Submit sheets",com=cmd)
        self.btn.pack(ipadx=10,ipady=50)

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
    def __init__(self, parent, text, com):
        self.button = tk.Button(parent, text=text, command=com, background="green")
    
    def pack(self, **kwargs):
        self.button.pack(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

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

    def bind(self, sequence: str | None, func):
        self.listbox.bind(sequence=sequence,func=func)

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