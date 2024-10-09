#importing the libraries
import numpy as np
from random import randint
from mod import*   

#maze definition
maze = np.zeros(shape=(10,10))

#loop for randomization and intitiation of mo
for i in range(len(maze)):
    for n in range(len(maze[i])):
        maze[i][n]=randint(0,1)       

#entry and exit
inc = randint(0,9)
inr = 0
outc = randint(0,9)
outr = 9
maze[inr][inc] = 8  
maze[outr][outc] = 5

#ensuring the path
xc = inc
xr = inr
while outr != xr or outc != xc:
    j = randint(0,2)
    if j == 0 and xc >=1:
        xc -= 1
    elif j == 1 and xr <=8:
        xr += 1
    elif j == 2 and xc <= 8:
        xc += 1    
    if maze[xr][xc]== 1:
        maze[xr][xc] = 0

#ouput
print_maze(maze)
q = 0

#gameplay
while outr != inr or outc != inc:
    x = input('enter move key w/a/s/d')
    #move(maze,inr,inc,x)
    if x.lower()=="w":
        if maze[inr-1][inc]!= 1:
            if inr>=1:
                maze[inr][inc]=0
                inr -= 1
                maze[inr][inc] = 8
    elif x.lower()=="a":
        if maze[inr][inc-1]!= 1:
            if inc >= 1:
                maze[inr][inc]=0
                inc -= 1
                maze[inr][inc] = 8
    elif x.lower()=="s":
        if maze[inr+1][inc]!= 1:
            if inr <=8:   
                maze[inr][inc]=0
                inr += 1
                maze[inr][inc] = 8
    elif x.lower()=="d":
        if maze[inr][inc+1]!= 1:
            if inc <=8:           
                maze[inr][inc]=0
                inc += 1
                maze[inr][inc] = 8
    #df
    q+=1
    print_maze(maze)

#ending mesaages
print (f'Congrats you won in {q} moves')