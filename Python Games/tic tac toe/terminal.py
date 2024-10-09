def check(O,X):
    winlist = [['00','11','22'],['02','11','20'],['00','01','02'],['10','11','12'],['20','21','22'],['00','10','20'],['01','11','21'],['02','12','22']]
    for i in range(0,8):
        #if winlist[i] in O:
        if(all(x in O for x in winlist[i])):
            return1 = "O"
            break
        elif(all(x in X for x in winlist[i])):
            return1 = "X"
            break
        else:
            return1 = '--'
    return return1

def output(main):
    for k in range(3):
        print(main[k])

main = []
O =[]
X = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append('--')
    main.append(temp)

turn = 0
while check(O,X) == '--':
    turn += 1
    output(main)
    if turn%2== 1:
        move = 0
        while move == 0:
            print("player X chance")
            a = int(input("enter row number"))
            b = int(input("enter column number"))
            if main[a][b] == '--':
                main[a][b] = 'X'
                X.append(str(a)+str(b))
                move += 1
    elif turn%2== 0:
        move = 0
        while move == 0:
            print("player O chance")
            a = int(input("enter row number(from 0 to 2)"))
            b = int(input("enter column number(from 0 to 2)"))
            if main[a][b] == '--':
                main[a][b] = 'O'
                O.append(str(a)+str(b))
                move += 1
if check(O,X) == 'X':
    print('Player X won')
elif check(O,X) == 'O':
    print('Player O won')