import tkinter as tk

window = tk.Tk()
play_area = tk.Frame(window,width=300,height=300,bg='white')

window.resizable(False,False)
window.title("Tic Tac Toe")

def press_button():
    print("it is pressed")

def reset_button(button):
    button.configure(test='',bg ='white')

def create_xo_point(x,y):
    button = tk.Button(play_area,text='',width =10,height=5)
    button.grid(row=x,column=y)
    return button

play_area.pack(pady=10,padx=10)

XO_buttons = []
for x  in range(1,4):
    for y in range(1,4):
        button=create_xo_point(x,y)
        XO_buttons.append((button))
    
print(XO_buttons)
tk.Label(window,text="Tic Tac Toe",font =('Ariel',25)).pack()
window.mainloop()
