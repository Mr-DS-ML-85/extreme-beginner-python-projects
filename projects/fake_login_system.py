system = True
count = 0
try:
  while system and count < 3:
      x = input("Enter Your Username = ")
      y = input("Enter Your Password = ")
      users = ["Alice","Bob","David Joe","Darwin", "imjohnny"]
      admins = ["Douglas", "Joel", "Sarah"]
      admins_pass = {"Douglas": "abc123!@#",
                   "Joel": "joel2024$%",
                   "Sarah": "sarahSecure99"
                  }
      users_pass = {"imjohnny": "jangoboy86",
                    "Alice": "alicePass1",
                   "Bob": "bobSecure2",
                   "David Joe": "davidJ2024",
                   "Darwin": "darwinX99"
                   }
      if x in admins and y == admins_pass[x]:
       print("Username Valid") 
       print(f"Login Successfully\nWelcome {x}(@admin)")
       system = False
      elif x in users and y == users_pass[x]:
         print("Username Valid")
         print(f"Login Successfully\nWelcome {x}(@user)")
         system = False
      else:
               print("Invalid Username or Password")
               print("Login Failed \n Try Again")
               count += 1
      if count == 3:
          print("Maximum login attempts reached. Exiting.")
          system = False
except KeyboardInterrupt:
    m = input("\n\nDo you want to exit the login page?(y/n):")
    z = m.lower()
    if z == 'y':
        system = False
