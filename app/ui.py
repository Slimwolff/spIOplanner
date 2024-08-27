import tkinter as tk
from tkinter import Menu, filedialog, messagebox, ttk
from app.methods import Methods


class WidModify:
    def __init__(self, anywidget):
        self.any = anywidget
    def pack(self, **kwargs):
        self.any.pack(**kwargs)
    def grid(self, **kwargs):
        self.any.grid(**kwargs)
    def bind(self, event, command):
        self.any.bind(event, command)

class MainFrame:
    def __init__(self, root, geometry):
        self.logic = Methods(self)
        self.root = root
        self.root.title("SpreadSheets IO Importation")
        self.root.geometry(geometry)
        self.menu_bar = Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.logic.open_data)
        self.file_menu.add_command(label="Save", command=self.logic.save_data)


        self.top = Top_panel(self.root, width=200, background='blue', height=150)
        self.top.pack(side='top', fill='x', expand=True)
        self.top.button.config(command=self.logic.set_spread)
        self.top.debug.config(command=self.logic.debug_data)
        self.top.deploy.config(command=self.logic.deploy)
        self.top.center_left.dropdown.bind('<<ComboboxSelected>>', self.logic.load_sheet_listbox)
        self.top.center_right.dropdown.bind('<<ComboboxSelected>>', self.logic.load_sheet_data)

        self.right = Right_panel(self.root, width=300, height=600, background='green')
        self.right.pack(side='right', fill='both', expand=True)

        self.left = Left_panel(self.root, width=300, height=600)
        self.left.pack(side='top', fill='both', expand=True)
        self.left.listbox.bind(sequence='<<ListboxSelect>>', func=self.logic.on_select)

        
        
class Top_panel(WidModify):
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        super().__init__(self.frame)

        self.right = tk.Frame(self.frame, width=100, height=150)
        self.right.pack(side='right',)

        self.left = tk.Frame(self.frame, width=100, height=150)
        self.left.pack(side='left', expand=False)
        self.button = tk.Button(self.left,text="Submit sheets")
        self.button.pack(ipadx=10,ipady=10)
        self.checked = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.left, text="Ignorar Primeira Coluna",var=self.checked)        
        self.checkbox.pack(side="left")

        self.center = tk.Frame(self.frame, height=150)
        self.center.pack(fill='both', expand=True)

        self.center_right = Cont_dropdown(self.center, width=150, height=150) 
        self.center_right.pack(side='right')
        self.center_right.label.config(text='Planilha de dados')
        self.center_left = Cont_dropdown(self.center, width=150, height=150)
        self.center_left.pack(side='left')
        self.center_left.label.config(text='Coluna modelo:')
        # right container
        self.debug = tk.Button(self.right, text="Debug global_data")
        self.debug.pack(side='right',ipadx=10,ipady=10)

        self.deploy = tk.Button(self.right, text="Deploy spreadsheet")
        self.deploy.pack(side='right',ipadx=10,ipady=10)
        


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

        self.column = Cont_dropdown(self.frame, width=100, height=100)
        self.column.pack(side='top', pady=5, fill='x', expand=False)

        self.removeChar = Cont_label_input(self.frame, width=100, height=100)
        self.removeChar.pack(side='top', pady=5, fill='x', expand=False)
        self.removeChar.label.config(text="Remover estes caracteres")

        self.maxChars = Cont_label_input(self.frame, width=100, height=100)
        self.maxChars.pack(side='top', pady=5, fill='x', expand=False)
        self.maxChars.label.config(text="Maximo de chacteres")

        self.reduceLast = Cont_label_input(self.frame, width=100, height=100)
        self.reduceLast.pack(side='top', pady=5,fill='x', expand=False)
        self.reduceLast.label.config(text="Remover charecters finais")

class Cont_label_input(WidModify):
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        super().__init__(self.frame)
        self.label = tk.Label(self.frame)
        self.label.pack(side='left',padx=10)
        self.entry = tk.Entry(self.frame)
        self.entry.pack(side='left',ipadx=40, ipady=10)


class Cont_dropdown(WidModify):
    def __init__(self, parent, **kwargs):
        self.frame = tk.Frame(parent, **kwargs)
        super().__init__(self.frame)
        self.label = tk.Label(self.frame,text="Select Column for model")
        self.label.pack(side='left')
        self.value = tk.StringVar()
        self.dropdown = ttk.Combobox(self.frame, textvariable=self.value)
        self.dropdown['values'] = ('None')
        self.dropdown.current(0) 
        self.dropdown.pack(pady=20)
