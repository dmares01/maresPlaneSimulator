import tkinter as tk
from tkinter import filedialog
import sys

def browse_files():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files",
                                                                                    "*.txt*"), ("all files","*.*")))
    sys.argv.append(filename)
    window.destroy()

# Create the root window
window = tk.Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x300")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = tk.Label(window, text="Please select an input file", width=75, height=4, fg="blue")

#Creating buttons for functionality
button_files = tk.Button(window, text="Browse Files", command=browse_files)
button_exit = tk.Button(window, text="Exit", command=exit)

# Layout of objects on screen
label_file_explorer.grid(column=1, row=1)
button_files.grid(column=1, row=2)
button_exit.grid(column=1, row=3)

# Let the window wait for user click
window.mainloop()