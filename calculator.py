import tkinter as tk
import math

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "π":
        entry.insert(tk.END, str(math.pi))
    elif button_text == "e":
        entry.insert(tk.END, str(math.e))
    elif button_text == "sqrt":
        try:
            result = math.sqrt(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("480x500")

# Create the entry widget
entry = tk.Entry(window, width=30, font=("Arial Black", 16), justify="right", bg="#B8D0EA")
entry.grid(row=0, column=0, columnspan=6)

# Define the buttons
buttons = [
    ("c", "(", ")", "/", "sqrt"),
    ("7", "8", "9", "*", ),
    ("4", "5", "6", "-",),
    ("1", "2", "3", "+",),
    (".", "0", "e", "=",)
]

# Add the buttons to the window
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        if buttons[i][j] == "=":  # Check if the button is '='
            btn = tk.Button(window, text=buttons[i][j], width=5, height=2,
                            font=("Arial Black", 16), command=lambda text=buttons[i][j]: on_click(text), fg='white', bg='green')
        else:
            btn = tk.Button(window, text=buttons[i][j], width=5, height=2,
                            font=("Arial Black", 16), command=lambda text=buttons[i][j]: on_click(text),fg='black')
        btn.grid(row=i+1, column=j, padx=5, pady=5)

# Run the GUI main loop
window.mainloop()
