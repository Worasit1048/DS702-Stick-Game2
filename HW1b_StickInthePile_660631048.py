# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
    
N = input("How many sticks(N) in the pile: ")
print("There are", N, "sticks in the pile." )
Name = input("What is your name: ")

n = int(N)
i = 0

while n > 0 :
    print("\n")
    print(Name,end=" ")
    X = input(",how many sticks you want to take (1 or 2): ")
    
    if int(X)<1 or int(X)>2 :
       print("No you can't take less 1 or more than 2 ") 
       
    elif int(X)>n :
        print("There are not enough stick to take.")
    
    if n >= int(X) and 0< int(X) <=2 :
        i += 1
        n = n-int(X)
        print("There are",n,"Left in plie.")

    if n==0:
        print("OK, There is no stick left in the plie.",end=" ")
        print("You spent" , i ,"times. ")



