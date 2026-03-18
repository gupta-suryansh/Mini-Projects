import functions as fn
import random

fn.load()

num = random.randint(1,999)

name = input("Enter your name: ")

# print(num)
count = 0

while True:
    guess = int(input("Guess the number (1-999 / 0 -> QUIT): "))
    if(guess==0):
        q = input("Do you want to quit the game? (y/n): ")
        if(q=='y'):
            print("Quitting the game.")
            break
        else:
            continue
    if(guess<1 or guess>999):
        print("Invalid Input!")
    elif(guess==num):
        print("Correct! You Won :)")
        print(f"You took {count+1} tries.")

        fn.players.append({"name" : name , "tries" : count+1})
        break
    else:
        print("Wrong Guess :(")
    count+=1

fn.save()
