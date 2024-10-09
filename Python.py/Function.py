# lets define a function
# def Function_Name(argument_1    argument_2):
#     do whatever you want this function to do
#     using argument 1 and 2

# use Function_Name to call the function
# Function_name(value_1   value_2)

############ START of function ###############

def add(a,b):
    sum = a+b
    print(sum)

def sub(a,b):
    dif = a-b
    print(dif)

def mul(a,b):
    pro = a*b
    print(pro)

def div(a,b):
    quo = a/b
    print(quo)

a=float(input("Enter Your Value:"))
b=float(input("Enter Your Value:"))

sum=a+b
print(a+b)

dif=a-b
print(a-b)

pro=a*b
print(a*b)

quo=a/b
print(a/b)