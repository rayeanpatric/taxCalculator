import tkinter as tk

def on_entry_click(event):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg="black")  # Change text color to black

def on_entry_leave(event):
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(fg="gray")  # Change text color to gray

root = tk.Tk()
root.title("Entry Box with Placeholder")

placeholder_text = "Enter text here"

entry = tk.Entry(root, fg="gray")  # Set text color to gray
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_entry_leave)

entry.pack()

entry = tk.Entry(root, fg="gray")  # Set text color to gray
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_entry_leave)

entry.pack() 

root.mainloop()
