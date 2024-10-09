import tkinter as tk

window = tk.Tk()
entry = tk.Entry()

def submit():
    print(entry.get())

button = tk.Button(text='Submit',command=submit)
entry.pack()
button.pack()
window.mainloop()