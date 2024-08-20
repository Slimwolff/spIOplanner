import tkinter as tk
def on_select(event):
    # Get selected item(s)
    selected_indices = listbox.curselection()
    selected_values = [listbox.get(i) for i in selected_indices]
    print("Selected:", selected_values)

# Create the main window
root = tk.Tk()
root.title("Select Option Listbox")

# Create a listbox widget
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)  # selectmode=tk.SINGLE for single selection

# Insert options into the listbox
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
for option in options:
    listbox.insert(tk.END, option)

# Bind the select event to the listbox
listbox.bind('<<ListboxSelect>>', on_select)

# Pack the listbox into the window
listbox.pack()

# Run the application
root.mainloop()