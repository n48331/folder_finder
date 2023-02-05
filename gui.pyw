from tkinter import *
from tkinter import ttk
import os
import subprocess

def openFolder():
    found.set(f'Search another') 
    parent_folder = f".\{directory.get()}"
    search_folder = search.get()
    for root, subdirs, files in os.walk(parent_folder):
        for d in subdirs:
            if d == search_folder:
                found.set(f'Found at {root}\{d}')
                subprocess.Popen(f'explorer "{root}\{d}"')
                break
        break  
            


root = Tk()
style = ttk.Style()
style.configure('TEntry', foreground = 'green')
root.config(bg='powderblue')
root.option_add('verdana', '19')
root.title('Folder Finder')
# root.iconbitmap('./link.ico')
root.geometry('400x200')

found = StringVar()
# input link
Label(root, text='Enter your parent folder name and mysheet ID to search',
      bg="powderblue", pady=10).pack()
directory = ttk.Entry(root, width=50)
directory.insert(INSERT, 'folder_name')
directory.pack()
search = ttk.Entry(root, justify = CENTER,
                                     font = ('courier', 15, 'bold'))
search.pack(pady=10)

# button
findButton = Button(root, text='Open folder',
                    command=openFolder)
findButton.pack(pady=10)


# no of links
Label(root, text='', textvariable=found, bg="powderblue").pack()


root.mainloop()
