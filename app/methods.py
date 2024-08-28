import os
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
        self.selected = ""
        self.global_data = {}
        self.spreadsheets = []
        self.model_csv = None
        self.data_csv= None

    def set_spread(self):
        file_path = filedialog.askopenfilename(filetypes=[("Files", "*.csv")])
        if file_path not in self.spreadsheets:
            spread = {
                "file_path": file_path,
                "file_name": os.path.basename(file_path)
            }
            self.spreadsheets.append(spread)

        default_value = 'None'
        self.ui.top.center_left.dropdown['values'] = (default_value, *(item['file_name'] for item in self.spreadsheets))
        self.ui.top.center_right.dropdown['values'] = (default_value, *(item['file_name'] for item in self.spreadsheets))

    def load_sheet_listbox(self, event):
        file_name = self.ui.top.center_left.value.get()
        file_path = next((item["file_path"] for item in self.spreadsheets if item["file_name"] == file_name), None)
        
        if file_path:
            try:
                # Read the Excel file
                df = pd.read_csv(file_path, sep=";", encoding_errors=False, engine='python', na_filter=False)
                self.model_csv = df
                #clear global data
                self.global_data = {}
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
                    self.global_data[k] = { "column": "", "max_char": -1, "reduceLast": -1, "remove": "", "value": list() }  # Note: Consider avoiding global variables


            except Exception as e:
                messagebox.showerror("Error", f"Could not load file: {e}")

    def load_sheet_data(self, event):
        file_name = self.ui.top.center_right.value.get()
        file_path = next((item["file_path"] for item in self.spreadsheets if item["file_name"] == file_name), None)

        if file_path:
            try:
                # Read the Excel file
                df = pd.read_csv(file_path, sep=";", encoding_errors=False, engine='python', na_filter=False)
                self.data_csv = df

                cols = []
                for column in df.columns:
                    cols.append(column)
                
                #Insert column names into the dropdown
                self.ui.right.column.dropdown['values'] = (cols)

                    
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file: {e}")    

    def on_select(self, event):
        try:
            # Get the selected index and value from the Listbox
            i = self.ui.left.listbox.curselection()[0]
            new_selection = self.ui.left.listbox.get(i)

            # If there is a previous selection, update global_data
            if self.selected is not None:
                self.update_global_data(self.selected)

            # Update self.selected to the new selection
            self.selected = new_selection

            # Load the data corresponding to the new selection
            self.load_selection_data(self.selected)

        except IndexError:
            print("No item is selected in the Listbox.")

    def update_global_data(self, event):
        """Update global_data with the current values from the entry widgets."""

        key = self.selected

        column = self.ui.right.column.value.get()
        max_char = self.ui.right.maxChars.entry.get()
        reduceLast = self.ui.right.reduceLast.entry.get()
        remove = self.ui.right.removeChar.entry.get()

        if key:
            self.global_data[key]['column'] = column if column != "" else ""
            self.global_data[key]['max_char'] = int(max_char) if max_char != "" else -1
            self.global_data[key]['reduceLast'] = int(reduceLast) if reduceLast != "" else -1
            self.global_data[key]['remove'] = remove if remove != "" else ""
        

    def load_selection_data(self, key):
        """Load the selected item's data into the entry widgets."""
        data = self.global_data[key]

        # self.ui.right.column.entry.delete(0, tk.END)
        # self.ui.right.column.entry.insert(0, data['column'])

        self.ui.right.maxChars.entry.delete(0, tk.END)
        self.ui.right.maxChars.entry.insert(0, data['max_char'] if data['max_char'] != -1 else "")

        self.ui.right.reduceLast.entry.delete(0, tk.END)
        self.ui.right.reduceLast.entry.insert(0, data['reduceLast'] if data['reduceLast'] != -1 else "")

        self.ui.right.removeChar.entry.delete(0, tk.END)
        self.ui.right.removeChar.entry.insert(0, data['remove'])
        

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
        print("FCOD",self.global_data['FCOD'])
        print(self.selected)

    def deploy(self, event=None):
        k = list(self.global_data)

        for i in k:
            if self.global_data[i]['column']:

                col = self.global_data[i]['column']
                for key in list(self.data_csv[col]):
                    item = key
                    if self.global_data[i]['max_char'] != -1:
                        item = self.reduce(item,self.global_data[i]['max_char'])
                    if self.global_data[i]['reduceLast'] != -1:
                        item = self.reduceLast(item, self.global_data[i]['reduceLast'])
                    if self.global_data[i]['remove']:
                        item = self.removeChars(item, self.global_data[i]['remove'])
                    self.global_data[i]['value'].append(item)
    
    def removeChars(self, item, chars):
        rc = list(chars)
        a = str(item)
        for i in rc:
            a.replace(i, "")
        return a
    
    def reduce(self, item, n):
        item = str(item)
        return item[:n]

    def reduceLast(self, item, n):
        item = str(item)
        return item[:len(item)-n]

