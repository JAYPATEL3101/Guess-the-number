#Guess The Number:
import random

target= random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit : ")
    if(userChoice == "Quit"):
         break
    userChoice = int(userChoice)    
    if(userChoice == target):
        print("Success : Correct Guess !!")
        break
    elif(userChoice < target):
        print("your number is too small. Take  a bigger number")
    else:
        print("your number is too big. Take a smaller number")
print("----GAME OVER----")