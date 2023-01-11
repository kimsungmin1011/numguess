from random import shuffle, choice
stay_win=0
move_win=0
result={
    "move_win":0,
    "stay_win":0,
}

Number=int(input("시뮬레이션 횟수를 선택하시오: "))
for _ in range(Number):
  doors=[0,0,1]
  shuffle(doors)
  user_choice_1=choice(doors)
  doors.remove(0)
  if user_choice_1==0:
    result["move_win"]+=1
  else:
    result["stay_win"]+=1
print(result)
