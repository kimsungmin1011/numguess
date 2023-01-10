from random import randint
from time import sleep
# Print answer for debugging
answer=randint(0,100)

#User interaction
username=input("Hi there, What is your name?")
print(f"Hi, {username}! Please be my guest!")

#Get and print User's guess
guess=int(input(f"So {username}, Guess the number(1~100): "))
print(f"Well choice {username}~ You picked {guess}!!")

#compare answer with user's guess   
if guess==answer:
    print('********************')
    sleep(1)
    print('********************')
    sleep(1)
    print('********************')
    sleep(1)
    print(f'You got it right!! The answer is {answer}!!')
elif guess>answer:
    print(f'Keep going man~! That was too high {username}')
elif answer>guess:
    print(f'Kepp going man~! That was too low {username}')
