import tkinter as tk
from tkinter import Pack, filedialog, Text
import os
import pathlib

root =tk.Tk()

def addApp():

    filename = filedialog.askopenfilename(initialdir="/", filetype=(("exexutables", "*.exe"), ("all files", "*.*")))





canvas = tk.Canvas(width=700, height=700,bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFileButton = tk.Button(root, text="Open File", padx=10, pady=10, fg="white", bg="#263D42", command=addApp)
openFileButton.pack()

root.mainloop()