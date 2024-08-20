import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Two Containers Example")
root.geometry("400x300")

# Create the first container (Frame)
frame1 = tk.Frame(root, width=200, height=300)
frame1.pack(side="left", fill="both", expand=True)

# Create the second container (Frame)
frame2 = tk.Frame(root, width=200, height=300)
frame2.pack(side="right", fill="both", expand=True)

# Run the application
root.mainloop()