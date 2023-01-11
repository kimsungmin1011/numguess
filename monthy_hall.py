from random import shuffle, choice
win=0
lose=0

Number=int(input("시뮬레이션 횟수를 선택하시오: "))
for i in range(Number):
  doors=[0,0,1]
  shuffle(doors)
  user_choice_1=choice(doors)
  doors.remove(0)
  if user_choice_1==1:
    user_choice_2=choice(doors)
    if user_choice_2==1:
      win+=1
    elif user_choice_2==0:
      lose+=1
  elif user_choice_1==0:
    user_choice_2=choice(doors)
    if user_choice_2==1:
      win+=1
    elif user_choice_2==0:
      lose+=1
print(win,lose)
