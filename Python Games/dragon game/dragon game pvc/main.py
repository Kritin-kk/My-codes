#importing
from random import randint 
from functools import reduce

#ouptput funtion
def show(row):
    for i in range(0,len(row)):
        print(f'{i})',end ='')
        for j in range(0,(row[i])):
            print('#' ,end = '')
        print()

#xor of list function
def xor(list):
    res = reduce(lambda x,y:x^y,list)
    return res

#initialisation
pl = randint(2,9)
row = []
for i in range(0,pl):
    row.append(randint(1,9))

#gameplay
show(row)
m = 0
if xor(row) >= 0:
    play = 1
else:
    play = 0
while True:
    m+=1
    #player chance
    if m%2 ==play:
        g = int(input("enter the row number(the no behind the bracket)"))
        b = int(input("enter the number of hashes to remove from that row"))
        if g <= len(row):
            if b <= row[g]:
                row[g] -= b
            else:
                print('invalid number of hashes')
        else:
            print("invalid row number")
    #computer chance
    elif m%2 != play:
        overallxor = xor(row)
        for i in range(len(row)):
            if row[i] != 0:
                x = row[i]^overallxor
                if x < row[i]:
                    temp = row[i]-x
                    row[i] -= temp
                    print(f"computer played row:{i} hashes:{temp}")
                    break
    show(row)
    if sum(row) == 0:
        break

#ending message
if m%2 == play:
    print('The Player won')
elif m%2 != play:
    print('The computer won')