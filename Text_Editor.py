# Text Editor Project

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
import csv

# Function to delete the content of a Text widget
def delete_txt(text):
    text.delete(1.0 , tk.END)

# Function to open a file and display its content in the Text widget
def open_file():
    # Ask the user to select a text file
    filepath = askopenfilename(filetypes=[("Text File", "*.txt")])
    
    # Check if a file is selected
    if not filepath:
        return
    
    # Read the content of the selected file
    with open(filepath, "r") as input_file:
        text = input_file.read()
        # Clear the current content of the Text widget
        delete_txt(txt_area)
        # Insert the content of the file into the Text widget
        txt_area.insert(tk.END, text)

# Function to save the content of the Text widget to a file
def save_file():
    # Ask the user to select a location to save the file
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text File", "*.txt")])

    # Check if a location is selected
    if not filepath:
        return
    
    # Write the content of the Text widget to the selected file
    with open(filepath, "w") as output_file:
        text = txt_area.get(1.0, tk.END)
        output_file.write(text)

# Create the main Tkinter application window
app = tk.Tk()
app.geometry('800x500')
app.title("Text Editor")

# Create a frame to hold other widgets
frame = ttk.Frame(app, padding=10)
frame.grid(row=0, column=0, columnspan=4, rowspan=4)

# Create a left frame for buttons
left_frame = ttk.Frame(frame, padding=5)
left_frame.grid(row=0, column=0, sticky='ns')
left_frame['borderwidth'] = 5
left_frame['relief'] = "solid"

# Create a main frame for the Text widget
main_frame = ttk.Frame(frame, padding=5)
main_frame.grid(row=0, column=2, columnspan=3)
main_frame['borderwidth'] = 5
main_frame['relief'] = "solid"

# Create "Open File" button
b1 = Button(left_frame, text ="Open File", width=12, command=open_file)
b1.grid(row=0, column=0, columnspan=2, pady=5)

# Create "Save As" button
b2 = Button(left_frame, text ="Save As", width=12, command=save_file)
b2.grid(row=1, column=0, pady=5)

# Create a Text widget for editing text
txt_area = Text(main_frame)
txt_area.grid(row=0, column=0)

# Start the Tkinter event loop
app.mainloop()
