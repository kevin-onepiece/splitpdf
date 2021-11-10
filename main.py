import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import pdfplumber

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    filetypes = (
        ('text files', '*.pdf'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )

    for file in filenames:
        split_pdf(file)

def split_pdf(filename):
    print(filename)
    with pdfplumber.open(filename) as pdf:
        # print(pdf.pages)
        # todo: 对不同的页数进行操作
        first_page = pdf.pages[0].page_number

        print(first_page)
        # print(first_page.chars[0])

# open button
open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)

open_button.pack(expand=True)

root.mainloop()