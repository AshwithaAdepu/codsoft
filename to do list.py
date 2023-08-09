import tkinter as tk

def add_item():
    item = entry.get()
    if item:
        tasks.append(item)
        refresh_listbox()

def delete_item(index):
    tasks.pop(index)
    refresh_listbox()

def edit_item(index):
    item = tasks[index]
    entry.delete(0, tk.END)
    entry.insert(tk.END, item)
    delete_item(index)

def refresh_listbox():
    for widget in listbox_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        task_frame = tk.Frame(listbox_frame)
        task_frame.grid(row=i, column=0, padx=5, pady=5, sticky="w")
        
        task_textbox = tk.Text(task_frame, height=1, width=30)
        task_textbox.insert(tk.END, task)
        task_textbox.pack(side=tk.LEFT)
        
        edit_button = tk.Button(task_frame, text="Edit", command=lambda i=i: edit_item(i), fg="black",bg=("light blue"))
        edit_button.pack(side=tk.LEFT, padx=5)
        
        delete_button = tk.Button(task_frame, text="Delete", command=lambda i=i: delete_item(i), bg="red",fg="black")
        delete_button.pack(side=tk.LEFT)

# Create the main application window
root = tk.Tk()
root.title("TODO List")

tasks = []

# Styling the title label 
title_label = tk.Label(root, text="TO-DO List", font=("ARIAL", 24, "bold"), fg="green")
title_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=10)

# Adding a subtitle "ADD ITEM" under the main title
subtitle_label = tk.Label(root, text="ADD ITEM", font=("ARIAL", 12, "bold","italic"), fg="black")
subtitle_label.grid(row=1, column=0, sticky="w", padx=10, pady=0)

# Entry to add items

entry = tk.Entry(root, width=30)
entry.grid(row=2, column=0, padx=10, pady=5)

# Adding a subtitle "TASKS" under the entry box

tasks_subtitle_label = tk.Label(root, text="TASKS", font=("ARIAL", 12, "bold","italic"), fg="black")

tasks_subtitle_label.grid(row=3, column=0, sticky="w", padx=10, pady=0)

# Button to add item
add_button = tk.Button(root, text="submit", command=add_item, fg="black",bg="white")

add_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Frame to hold the list of tasks
listbox_frame = tk.Frame(root)
listbox_frame.grid(row=4, column=0, columnspan=2)
root.mainloop()
