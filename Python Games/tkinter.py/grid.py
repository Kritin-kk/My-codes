import tkinter as tk

def press_button():
    print("it is pressed")
    label = tk.Label(text = 'pressed',background = 'black',foreground = 'white',font=('Times New Roman',29))
    label.pack()
window = tk.Tk()

label = tk.Label(text = 'pressed',background = 'black',foreground = 'white',font=('Times New Roman',29))

label.grid(row = 0,column=0)
button = tk.Button(text ='Click me',command=press_button)
button.grid(row=0,column = 1)

window.mainloop()