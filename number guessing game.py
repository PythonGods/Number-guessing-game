#imports
import random
flag=True
#part 1
while flag:
    num=input("Type a number for an upper bound:")
    if num.isdigit():
        print("Game is generating")
        num=int(num)
        flag=False
    else:
        print("Invalid input! Try again!")
        
secret=random.randint(1,num)
guess=None
count=1 
count=count+1
#part 2
while guess != secret:
    guess=input("Please type a number between 1 and "+str(num)+":")
    if guess.isdigit():
        guess=int(guess)
    if guess==secret:
        print("You got it. You Won !")
        print("It took you ", count, "guesses.")
    if guess>secret:
        print("The number is too big: ")
        count+=1
    if guess<secret:
        print("The number is too small:")
        count+=1
    if guess==0:
        print("The secret number is: ",secret)
        break