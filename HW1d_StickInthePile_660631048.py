import random

def take_stick(n,Name):
    i=1
    Game_over = 0
    while n > 0 and Game_over == 0:                                         # n<0 and game_over != 0
        
        if i % 2 == 0:
            #print("Z ",i%2)                                                #Chack AI or man playing
            name1 = "AI"
            for _ in range(1):                                              #Loop random value of AI
                X = random.randint(1,2)
                print(name1, "I,smart computer, take: ",X)
                
        else :
            name1 = Name
            print(name1,end=" ")
            X = int(input(",how many sticks you want to take (1 or 2): "))
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
            Game_over = 1
            
        else:
            n = n - X
            print("There are",n,"Left in plie.\n")
            if n == 1:
                print(name1, ", Win!")
                Game_over = -1
                
            else :
                i += 1
            
    print("Game spent" , i ,"round.")    

n = int(input("How many sticks(N) in the pile: "))
print("There are", n , "sticks in the pile." )

Name = input("What is your name: ")
Process = take_stick(n,Name)
         