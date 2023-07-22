import random

def take_stick(n,Name):
    i=1
    while n > 0 :
        
        if i % 2 == 0:
            #print("Z ",i%2)
            name1 = "AI"
            for _ in range(1): ####
                X = random.randint(1,2)
                print(name1, "I,smart computer, take: ",X)
        #  print("There are",n-X,"Left in plie.")
        
        else :
            name1 = Name
            print(name1,end=" ")
            x = input(",how many sticks you want to take (1 or 2): ")
            X = int(x)
            #print("i= ",i)
            #print("X= ",X)
            #print("n= ",n)
            
            if X<1 or X>2 :
                print("No you can't take less 1 or more than 2 ") 
                continue
            #else :
            #   X=0
            #  continue
        if X>n or X==n :
            #print("There are not enough stick to take.")
            print(name1, ", Lose!")
            #break
        else:
            n = n - X
            print("There are",n,"Left in plie.\n")
            if n == 1:
                print(name1, ", Win!")
                #break
            else :
                i += 1
            
    print("Game spent" , i ,"times. ")

N = input("How many sticks(N) in the pile: ")
print("There are", N , "sticks in the pile." )
Name = input("What is your name: ")
n = int(N)
Process = take_stick(n,Name)
#print(Process)