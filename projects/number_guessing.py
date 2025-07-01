guess = True
while guess :
   x = int(input("Enter a number: "))
   if x == 40 :
     print("CORRECT")
     break
   if x < 40 :
    print("TOO LOW")
   if x > 40 :
    print("TOO HIGH")


