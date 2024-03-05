import random 

number= random.randint(1,100)
attempt = 1
guess = 0

while guess != number:
    guess = int(input("Enter Guess = "))

    if(guess < number) :
       print("Too Low!!")
       attempt = attempt + 1
    elif(guess > number) :
       print("Too High!")
       attempt = attempt + 1
    else:
       print("You Won the Game ") 

print(f"Total Attempts = {attempt}")     