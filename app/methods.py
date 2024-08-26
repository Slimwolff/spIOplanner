import tkinter as tk
from tkinter import filedialog, messagebox
from data.constants import global_data, data_boilerplate, Boilerplate

import pandas as pd
import json

global global_index
global_index = "" #global variale to set active listbox


class ListboxMethods:
    def __init__(self, ui):
        self.ui = ui

    def get(self, index):
        return self.ui.left.listbox.get(index)
    def fill(self,value):
        self.ui.left.listbox.insert(tk.END, value)
    def delete(self):
        self.ui.left.listbox.delete(0, tk.END)
    def select_set(self, i):
        self.ui.left.listbox.select_set(i)

class Methods:
    def __init__(self, ui):
        self.ui = ui
        self.listbox = ListboxMethods(self.ui)

    def load_sheet(self):
        # Open a file dialog to select the Excel file
        file_path = filedialog.askopenfilename(filetypes=[("Files", "*.csv")])
        
        if file_path:
            try:
                # Read the Excel file
                df = pd.read_csv(file_path, sep=";", encoding_errors=False, engine='python', na_filter=False)
                
                # Clear the listbox before showing new column names
                self.listbox.delete()
                cols = []
                cond = self.ui.top.checked.get()  # Access checked state from MainFrame
                for column in df.columns:
                    if cond == True:
                        print("first column ignored")
                        cond = False
                    else:
                        cols.append(column)
                
                #Insert column names into the listbox
                for k in cols:
                    self.listbox.fill(k)
                    global_data[k] = { "column": "", "max_char": -1, "reduceLast": -1, "remove": "", "$": []}  # Note: Consider avoiding global variables

                self.listbox.select_set(0)
                global_index = self.listbox.select_set(0)
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file: {e}")

    def on_select(self, event):
        global global_index
        i = self.ui.left.listbox.curselection()[0]
        selected = self.listbox.get(i)
        print(selected)

        if(global_index != ""):
            column = self.ui.right.column.value.get()
            max_char = self.ui.right.maxChars.entry.get()
            reduceLast = self.ui.right.reduceLast.entry.get()
            remove = self.ui.right.removeChar.entry.get()

            if(column != ""):
                global_data[selected]['column'] = column
            else:
                global_data[selected]['column'] = ""
            if(max_char != ""):
                global_data[selected]['max_char'] = int(max_char)
            else:
                global_data[selected]['max_char'] = -1
            if(reduceLast != ""):
                global_data[selected]['reduceLast'] = int(reduceLast)
            else:
                global_data[selected]['reduceLast'] = -1
            if(remove != ""):
                global_data[selected]['remove'] = remove
            else:
                global_data[selected]['remove'] = ""

        if(selected != ""):

            column = global_data[selected]['column']
            max_char = global_data[selected]['max_char']
            reduceLast = global_data[selected]['reduceLast']
            remove = global_data[selected]['remove']

            if(column == ""):
                pass
            
            if(max_char == -1):
                self.ui.right.maxChars.entry.delete(0, tk.END)
                self.ui.right.maxChars.entry.insert(0, "")
            else:
                self.ui.right.maxChars.entry.delete(0, tk.END)
                self.ui.right.maxChars.entry.insert(0, max_char)

            if(reduceLast == -1):
                self.ui.right.reduceLast.entry.delete(0, tk.END)
                self.ui.right.reduceLast.entry.insert(0, reduceLast)
            else:
                self.ui.right.reduceLast.entry.delete(0, tk.END)
                self.ui.right.reduceLast.entry.insert(0, reduceLast)

            if(remove == ""):
                self.ui.right.removeChar.entry.delete(0, tk.END)
                self.ui.right.removeChar.entry.insert(0, "")
            else:
                self.ui.right.removeChar.entry.delete(0, tk.END)
                self.ui.right.removeChar.entry.insert(0, remove)

    # Function to save Data to a JSON file
    def save_data(self, event=None):
        print(event)
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(global_data, file, indent=4, ensure_ascii=False)
            messagebox.showinfo("Save", "File saved successfully!")

    # Function to open and load Data from a JSON file
    def open_data(self, event=None):
        print(event)
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            global global_data
            with open(file_path, 'r') as file:
                global_data = json.load(file)
            messagebox.showinfo("Open", "File opened successfully!")
            # Optionally, refresh the GUI to reflect loaded data

    def debug_data(self, event=None):
        print(global_data)


def tdt(a,removeChars="",reduce=-1,reduceLast=-1):
    arr = a
    for a in range(len(arr)):
        arr[a] = str(arr[a])

    if(removeChars != ""):
        rc = list(removeChars)
        for i in range(len(arr)):
            for x in rc:
                arr[i] = arr[i].replace(x, "")
    
    if(reduce != -1):
        for i in range(len(arr)):
            arr[i] = arr[i][0:reduce]

    if(reduceLast != -1):
        for i in range(len(arr)):
            arr[i] = arr[i][0:len(arr[i])-reduceLast]

    return arr