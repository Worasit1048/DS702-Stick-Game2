import random

def take_stick(n,Name,mp):
    i=1
    Game_over = 0
    while n > 0 and Game_over == 0:                                                 # n<0 and game_over != 0
        if n == mp+2 and i == 1:                                                    # if Num of pile is magic num, assigh player play before 
            print(Name,end=" ")
            X = int(input(",how many sticks you want to take: "))
            n = n - X
            print("There are",n,"Left in plie.\n")
            X = n-1
            print("AI, I smart computer take: ", X)
            print(Name,", Defeated and AI WON")
            Game_over = 1

        else :   
            if i % 2 != 0: 
                #print("Z ",i%2)                                                    #Chack AI or man playing
                name1 = "AI"
                if (n<=2*mp+2) and (n>mp+2) :
                    X = n-(mp+2)
                    print(name1, "I smart computer, take: ",X,)
                    #print("AI (((IF)))")

                elif mp+2> n >= mp+1:
                    X = mp
                    print(name1, "I smart computer, take: ",X,)
                    #print("AI (((ELSE2 IF)))")

                elif n == mp :
                    X = mp-1
                    print(name1, "I smart computer, take: ",X)
                    #print("AI (((ELSE2 IF)))")

                else:
                    for _ in range(1):                                              #Loop random value of AI
                        X = random.randint(1,mp)
                        print(name1, "I,smart computer, take: ",X)
                        #print("AI (((Else2)))")
                
            else :                                                                  # Loop player
                name1 = Name
                print(name1,end=" ")                    
                X = int(input(",how many sticks you want to take: "))       
                #print("i= ",i)
                #print("X= ",X)
                #print("n= ",n)
                
                if X<1 or X>mp :
                    print("No you can't take less 1 or more than ",mp) 
                    continue
                
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
mp = int(input("Maximum number of stick, we can take it off?: "))

Name = input("What is your name: ")
Process = take_stick(n,Name,mp)
         