def factorial( x):
    i =1
    fact = 1
    if x==0:
        print(fact)
    else:
        while i<=x:
            fact=fact*i
            i=i+1  
        print(fact)
    
x=int(input("Enter the number whose factorial is to be found\n"))
factorial(x)
