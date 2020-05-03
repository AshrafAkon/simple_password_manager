#!python3
import tkinter as tk
import pyautogui
import time
import pyperclip
import pickle
import os


password_dict = {'github' : '123',
 'facebook' : '456',
 'gmail' : '789'}

last_value = ""
def on_closing(last_value):
    try:
        if len(last_value) > 0:
            with open('last_item.pkl', 'wb') as f:
                f.write(pickle.dumps(last_value))
        root.destroy()
    except Exception as e:
        print(e)
        root.destroy()

def refresh(value):
    mylistbox.delete(0,len(password_dict) - 1)
    
    mylistbox.insert(0, value)
    for item in password_dict:
        if item == value:
            continue
        mylistbox.insert(tk.END, item)

def submit_func(evt=None):
    value=str(mylistbox.get(mylistbox.curselection()))
    pyperclip.copy(password_dict[value])
    print(value)
    root.after(500, refresh, value)

root=tk.Tk()
submit_button = tk.Button(root, text="Submit", command=submit_func, borderwidth=5,height = 3, width =10,)
submit_button.grid(column=0, row = 0, pady = 10)

listbox_frame = tk.Frame(root)
listbox_frame.grid(column = 0, row=1)

mylistbox=tk.Listbox(listbox_frame,width=20,height=20,font=('times',15), justify=tk.CENTER)
mylistbox.grid(column= 0, row = 0)

scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
scrollbar.grid(column = 1, row = 0,sticky='ns')
mylistbox.configure(yscrollcommand=scrollbar.set)


mylistbox.bind('<Double-Button-1>', submit_func)
mylistbox.bind('<Return>',submit_func)

if os.path.isfile('last_item.pkl'):
    with open('last_item.pkl', 'rb') as f:
        last_value = pickle.loads(f.read())
    if len(last_value) > 0:
        mylistbox.insert(0,last_value)

for item in password_dict:
    if item == last_value:
        continue
    mylistbox.insert(tk.END,item)

root.protocol("WM_DELETE_WINDOW", lambda : on_closing(last_value))
root.mainloop()