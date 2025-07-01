
cal = input("Do you want to use calculator(y/n): ").lower()
if cal == "y":
    x = int(input("Enter 1st number :"))
    y = int(input("Enter 2nd number :"))
    z = (input("Which Calculation \n1.(+)\n2.(-)\n3.(x)\n4.(÷)\nEnter:"))
    if z == "+" or z == "1" :
       k = x+y
       print(f"Result of addition = {k}")
    if z == "-" or z == "2":
       k = x-y
       print(f"Result of subtraction = {k}")
    if z == "x" or z == "3" :
       k = x*y
       print(f"Result of multiplication = {k}")
    if z == "÷" or z == "4":
       k = x/y
       print(f"Result of division = {k}")
else :
   exit("Thanks For Running Calculator")

   