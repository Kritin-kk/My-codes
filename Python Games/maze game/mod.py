#importing
from colorama import Fore

#defining output funciton
def print_maze(maze):
    for i in range(0,10):
        for n in range(0,10):
            if maze[i][n]==0:
                print(Fore.GREEN, f'{"__"}',end="")
            elif maze[i][n]==1:
                print(Fore.RED, f'{"XX"}',end="")
            elif maze[i][n]==8:
                print(Fore.WHITE, f'{"@@"}',end="")
            elif maze[i][n]==5:
                print(Fore.BLUE, f'{"^^"}',end="")
        print()


    
    
    
             