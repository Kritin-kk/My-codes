# def factorial(n):
#     n=n if n>1 else 1
#     j=1
#     for i in range(1, n+1):
#         j=j*i
#     return j

for i in range(1,8):
    print(i, '->', factorial (i))

# n!= (n)*(n-1)!

def factorial (num):

    if num <= 1:
        return 1
    else:
        return(num * factorial (num - 1))
    
print (factorial (5))
