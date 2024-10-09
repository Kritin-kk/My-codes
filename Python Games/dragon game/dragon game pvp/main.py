#importing
from random import randint

#ouptput funtion
def show(row):
    for i in range(0,len(row)):
        print(f'{i})',end ='')
        for j in range(0,(row[i])):
            print('#' ,end = '')
        print()

#initialisation
pl = randint(2,9)
row = []
for i in range(0,pl):
    row.append(randint(1,9))

#gameplay
m = 1
show(row)
while sum(row) != 0:
    if m%2 != 0:
        print("Player 1")
    else:
        print("Player 2")
    g = int(input("enter the row number(the no behind the bracket)"))
    b = int(input("enter the number of hashes to remove from that row"))
    if g <= len(row):
        if b <= row[g]:
            row[g] -= b
            m += 1
        else:
            print('invalid number of hashes')
    else:
        print("invalid row number")
    show(row)
    if sum(row) == 0:
        break

if m%2 == 0:
    print('Player 1 won')
elif m%2 == 1:
    print('Player 2 won')
