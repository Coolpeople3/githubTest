import random
score= 0
print("Copyright 2024 Hitarth Yagnik All rights reserved")
print("This is a game of Higher or Lower!")
print("you must guess if the next number will be higher or lower than the first number")
print("if you guess correctly you will gain a point")
print("if you guess wrong, you lose a point")
print("remember, type your answer with first letter uppercase")
print("The numbers are between 1 and 13.")
print("")
num=random.randint(1,13)
for i in range(0,100):
  num2=random.randint(1,13)
  print("First number:",num)
  a=input("Will the next number be Higher or lower? ")
  if a == "Higher":
    if num2>num:
      print("roll:",num2)
      print("correct! Score:",score+1)
      score+=1
      print("")
    else:
      print("roll:",num2)
      print("incorrect! Score:",score-1)
      print("")
  if a == "Lower":
    if num2<num:
      print("roll:",num2)
      print("correct! Score:",score+1)
      score+=1
      print("")
    else:
      print("roll:",num2)
      print("incorrect! Score:",score-1)
      print("")
  num=num2
