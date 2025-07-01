while True :
    bot = input("Do you want to start the @dayoftheweekBOT(y/n)")
    if bot == "y" :
        day = int(input("Enter a day in number: "))
        if day == 1 :
            print("It's Monday")
        elif day == 2 :
            print("It's Tuesday")
        elif day == 3 :
            print("It's Wednesday")
        elif day == 4 :
            print("It's Thursday")
        elif day == 5 :
            print("It's Friday")
        elif day == 6 :
            print("It's Saturday")
        elif day == 7 :
            print("It's Sunday")
        else :
           print("Invalid number type number between(1-7)")
    else :
        print("Thanks for Using The @dayofthewwekBOT")
        break 
