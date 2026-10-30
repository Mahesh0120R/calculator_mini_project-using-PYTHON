print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n1
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2==0:
        return "enter non zero value"
    return n1/n2
def calucator(option,n1,n2):
    if option==1:
        return add(n1,n2)
    elif option==2:
        return sub(n1,n2)
    elif option==3:
        return mul(n1,n2)
    elif option==4:
        return div(n1,n2)
    elif option==5:
        exit
    else:
        return "Enter a valid option"
option=int(input("Choose function: "))
n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
x=calucator(option,n1,n2)
print(x)





        