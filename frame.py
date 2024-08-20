# Import Module
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

_global_cond_ = False

global_data = {}

data_boilerplate = {
    "column": "",
    "max_char": -1,
    "reduceLast": -1,
    "remove": "",
    "$": []
}


def load_sheet():
    # Open a file dialog to select the Excel file
    file_path = filedialog.askopenfilename(filetypes=[("Files", "*.csv")])
    
    if file_path:
        try:
            # Read the Excel file
            df = pd.read_csv(file_path,sep=";",encoding_errors=False,engine='python',na_filter=False)
            
            # Clear the listbox before showing new column names
            listbox.delete(0, tk.END)
            
            cols = []

            for column in df.columns:
                if(_global_cond_ == True):
                    print("first column ignored")
                    changeCond()
                else:
                    cols.append(column)
            
            cols = df.columns

            print("colunas",cols)
            # Insert column names into the listbox
            for column in df.columns:
                if(_global_cond_ == True):
                    print("first column ignored")
                    changeCond()
                else:
                    listbox.insert(tk.END, column)
                    
                    
        except Exception as e:
            messagebox.showerror("Error", f"Could not load file: {e}")

# create root window
root = tk.Tk()
 
# root window title and dimension
root.title("SpreadSheets IO Importation")
# Set geometry(widthxheight)
root.geometry('700x550')
 
# Create first container
frame1 = tk.Frame(root, width=200, height=300)
frame1.pack(side="top", fill="both", expand=True)

# Create the second container (Frame)
frame2 = tk.Frame(root, width=200, height=300)
frame2.pack(side="right", fill="both", expand=True)

# create container to encapsulate elements
select_column = tk.Frame(frame2, width=100, height=80)
select_column.pack(side="top", fill="x")

label_sc = tk.Label(select_column, text="selecionar coluna").pack(side="left",padx=10)

dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(select_column, textvariable=dropdown_var)
dropdown['values'] = ('First', 'Second', 'Third')
dropdown.current(0)  # Set the default option to 'First'
dropdown.pack(pady=20)

def changeCond():
    global _global_cond_ 
    _global_cond_ = not _global_cond_
    print(_global_cond_)

var1 = tk.BooleanVar()
cb1 = tk.Checkbutton(frame1, text="Ignorar Primeira coluna", variable=var1, command=changeCond)
cb1.pack(side="left")

# Create and place the Submit button
submit_button = tk.Button(frame1, text="Submit Sheet", command=load_sheet)
submit_button.pack(ipady=10,ipadx=40)



# Create a label
label = tk.Label(frame2, text="Remover caracteres:")
label.pack(side="left",padx=10)


# Create a text input field
entry = tk.Entry(frame2, width=30)
entry.pack(side="left")


listFrame = tk.Frame(root, width=100, height=300)
listFrame.pack(side="left", fill="both", expand=True)

# Create a listbox to display the column names
listbox = tk.Listbox(listFrame, width=50, height=80)
listbox.pack(pady=20, padx=20 )


scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side="right", fill="y")
# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command = listbox.yview) 

# setting scrollbar command parameter  
# to listbox.yview method its yview because 
# we need to have a vertical view 

# Execute Tkinter
root.mainloop()

