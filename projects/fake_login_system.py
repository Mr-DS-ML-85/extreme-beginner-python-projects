system = True
while system :
    x = input("Enter Your Username = ")
    y = input("Enter Your Password = ")
    if x == "Douglas":
       print("Username Valid")
       if y == "abc123!@#" :
           print("Login Successfully\nWelcome David Douglas(@admin)")
           system = False
       else :
            print("Invalid Password")
    elif x == "imjohnny":
         print("Username Valid")
         if y == "jangoboy86":
             print("Login Successfully\nWelcome Johnny Davy(@user)")
             system = False
         else :
              print("Invalid Password")
    else:
       print("Login Failed \nInvalid Username")