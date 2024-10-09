from random import randint
pscore = 0
cscore = 0
while pscore != 5 and cscore != 5:
    psign = int(input("enter the integer for the choice \n 1)rock \n 2)paper \n 3)scisor"))
    if psign == 1 or psign == 2 or psign==3:
        csign = randint(1,3)
        if psign == csign:
            print("the pc chose the same so it is a tie")
            print(f"Player score:{pscore} Computer score:{cscore}")
        elif psign == 1:
            if csign == 2:
                print("the pc chose paper and won")
                cscore +=1
                print(f"Player score:{pscore} Computer score:{cscore}")
            elif csign == 3:
                print("the pc chose scisor and you won")
                pscore += 1
                print(f"Player score:{pscore} Computer score:{cscore}")
        elif psign == 2:
            if csign == 1:
                print("the pc chose rock and you won")
                pscore += 1
                print(f"Player score:{pscore} Computer score:{cscore}")
            elif csign == 3:
                print("the pc chose scisor and won")
                cscore += 1
                print(f"Player score:{pscore} Computer score:{cscore}")
        elif psign == 3:
            if csign == 1:
                print("the pc chose rock and won")
                cscore += 1
                print(f"Player score:{pscore} Computer score:{cscore}")
            elif csign == 2:
                print("the pc chose paper and you won")
                pscore += 1
                print(f"Player score:{pscore} Computer score:{cscore}")
    else:
        print("error invalid choice")
if pscore == 5:
    print("Congrats the player won")
elif cscore == 5:
    print("The pc won")
