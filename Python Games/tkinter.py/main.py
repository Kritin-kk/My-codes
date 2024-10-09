#Importing
import tkinter as tk

def press_button():
    print("it is pressed")
    label = tk.Label(text = 'pressed',background = 'black',foreground = 'white',font=('Times New Roman',29))
    label.pack()

window = tk.Tk()
button = tk.Button(text ='Click me',command=press_button)
#label = tk.Label(text = 'I am a label with custom properties',background = 'black',foreground = 'white',font=('Times New Roman',29))
#label.pack()
button.pack()
window.mainloop()