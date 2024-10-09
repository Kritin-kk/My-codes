#  1  | 2  |  3 
# ===============
#  4  | 5  |  6  
# ===============
#  7  | 8  |  9

def print_board():
        print("  "+B[0]+"  "+"|"+"  "+B[1]+"  "+"|"+"  "+B[2]+"  ")
        print("=================")
        print("  "+B[3]+"  "+"|"+"  "+B[4]+"  "+"|"+"  "+B[5]+"  ")
        print("=================")
        print("  "+B[6]+"  "+"|"+"  "+B[7]+"  "+"|"+"  "+B[8]+"  ")


def win_check():
    if B[0] == 'X' and B[1] == 'X' and B[2] == 'X':
        return 'x won'
    elif B[3] == 'X' and B[4] == 'X' and B[5] == 'X':
        return 'x won'
    elif B[6] == 'X' and B[7] == 'X' and B[8] == 'X':
        return 'x won'
    elif B[0] == 'X' and B[3] == 'X' and B[6] == 'X':
        return 'x won'
    elif B[1] == 'X' and B[4] == 'X' and B[7] == 'X':
        return 'x won'
    elif B[2] == 'X' and B[5] == 'X' and B[8] == 'X':
        return 'x won'
    elif B[0] == 'X' and B[4] == 'X' and B[8] == 'X':
        return 'x won'
    elif B[2] == 'X' and B[4] == 'X' and B[6] == 'X':
        return 'x won'
    elif B[0] == 'O' and B[1] == 'O' and B[2] == 'O':
        return 'o won'
    elif B[3] == 'O' and B[4] == 'O' and B[5] == 'O':
        return 'o won'
    elif B[6] == 'O' and B[7] == 'O' and B[8] == 'O':
        return 'o won'
    elif B[0] == 'O' and B[3] == 'O' and B[6] == 'O':
        return 'o won'
    elif B[1] == 'O' and B[4] == 'O' and B[7] == 'O':
        return 'o won'
    elif B[2] == 'O' and B[5] == 'O' and B[8] == 'O':
        return 'o won'
    elif B[0] == 'O' and B[4] == 'O' and B[8] == 'O':
        return 'o won'
    elif B[2] == 'O' and B[4] == 'O' and B[6] == 'O':
        return 'o won'




B = [" "," "," "," "," "," "," "," "," "]

print_board()

# x plays first
for x in range(0,9):
    in1 = int(input("enter a position: "))

    if x%2 == 0:  
        B[in1-1] = "X"
    else:
        B[in1-1] = "O"
    print_board()
