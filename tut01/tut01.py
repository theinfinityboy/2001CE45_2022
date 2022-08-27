import os
os.system("cls")
def factorial( x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
x=int(input("Enter the number whose factorial is to be found\n"))
print(factorial(x))
exit()