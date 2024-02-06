import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from appunti import *

# Get the options from the file
def start():
    def show_message(message):
        messagebox.showinfo("Information", message)

def handle_button_click():
    selected_option = combobox.get()

    if selected_option in options:
        text_widget.delete("1.0", tk.END)  
        text_widget.insert(tk.END, options[selected_option])


def show_message(message):
    messagebox.showinfo("Information", message)

def close_window():
    window.destroy()

# Window elements
window = tk.Tk()
window.title("RecchettoBot")
title_font = ("Arial", 24, "bold")
window.attributes('-fullscreen', True)

# Label elements
label = tk.Label(window, text="Salve sono RecchettoBot e sono qui per aiutarti nel tuo esame di stato!", font=title_font)
label.pack(pady=15)
label.configure(bg="light gray")
label.pack()

# Create the combobox
combobox_style = ttk.Style()
combobox_style.configure('Custom.TCombobox', font=('Arial', 16))
combobox = ttk.Combobox(window, values=lista, font=("Arial", 16), width=40, height=40, style='Custom.TCombobox')
combobox.pack()

# Central button elements
button = tk.Button(window, text="Clicca per sapere",
                   font=("Arial", 14), width=20,height=1, command=handle_button_click)

def on_enter(event):
    button.configure(
        relief=tk.SOLID,
        fg="#ff96ad",
        bg="#17181c"
    )

def on_leave(event):
    button.configure(
        relief=tk.FLAT,
        fg="black",
        bg="white"
    )
# Bind the event handlers to button events
button.bind("<Enter>", on_enter)  # Pointer enters the button
button.bind("<Leave>", on_leave)  # Pointer leaves the button
button.pack(pady=10)
button.pack()


# Text_widget elements
text_widget = tk.Text(window, height=200, width=1000)
text_widget.pack()
text_widget.configure(font=("Arial", 12))
text_widget.configure(bg="#BAB1B6")
text_widget.pack(pady=10)

# Close button elements
close_button = tk.Button(window, text="Chiudi", command=close_window, font=("Arial", 14))
close_button.place(x=window.winfo_screenwidth() - 80, y=10)

window.mainloop()

start()

