def room_2():
 print("Welcome to room 2")
 print("Would you like to look around?(Y/N)")
 ans=input()
 if(ans=='Y' or ans=='y'):
    print("You will find a piece of paper with a riddle mentioned on it, answer the riddle correctly to obtain the key to unlock the door!")
    print("would you like to answer the riddle?(Y/N)")
    ans1=input()
    if(ans1=='Y' or ans1=='y'):
        print("I am tall when I'm young and short when I'm old.What am I?")
        res=input("Your answer:")
        if(res.upper()=='CANDLE'):
            print("CONGRATULATIONS!YOU HAVE ANSWERED THE RIDDLE CORRECTLY AND UNLOCKED THE DOOR!")
            print("Proceed to room 3?(Y/N)")
            ans2=input()
        else:
            print("SORRY!you have failed to unlock the door!Better luck next time!")
            print("Would you like to restart?(Y/N)")
            ans3=input()
            if(ans3=='Y' or ans3=='y'):
                room_2()
            else:
                print("okie")
    else:
        print("okie")
 else:
  print('okie')

room_2()
