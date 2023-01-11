from random import randint
from time import sleep
# Print answer for debugging
answer=randint(0,100)

#User interaction
username=input("Hi there, What is your name?")
print(f"Hi, {username}! Please be my guest!")
i=0
while i<5:
    i+=1
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
        break
    elif guess>answer:
        print(f'Keep going man~! That was too high {username}')
        continue
    elif answer>guess:
        print(f'Kepp going man~! That was too low {username}')
        continue
