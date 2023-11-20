fname=input("Enter your name ")
lenname=len(fname)
if lenname >= 2:
  print(f"Hello {fname}! Welcome to namegame3")  
  fchar=fname[0]
  lchar=fname[-1]
  print(f"The length of your  name is {lenname}")
  print(f"The first character of your name is {fchar}")
  print(f"The last character of your name is {lchar}")
else: 
    print(f"Your name cannot be less than two characters long, try again!")

