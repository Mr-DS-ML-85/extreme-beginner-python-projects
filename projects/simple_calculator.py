while True :
    cal = input("Do you want to use calculator(y/n): ").lower()
    if cal == "y":
        x = int(input("Enter 1st number(base for '^' only ) :"))
        y = int(input("Enter 2nd number :"))
        z = (input("Which Calculation \n1.(+)\n2.(-)\n3.(x)\n4.(÷)\n5.(^)\nEnter:"))

        if z == "+" or z == "1" :
           k = x+y
           print(f"Result of addition = {k}")
        elif z == "-" or z == "2":
           k = x-y
           print(f"Result of subtraction = {k}")
        elif z == "x" or z == "3" :
           k = x*y
           print(f"Result of multiplication = {k}")
        elif z == "÷" or z == "4":
           if y == 0 :
              print("can't divide by zero ❌")
           else :
              k = x/y
              print(f"Result of division = {k}")
        elif z == "^" or z == "5" :
           print(f"Result of division = {x**y}")
        else :
           print("Invalid Operator⚠️")
    else :
       exit("Thanks For Running Calculator")