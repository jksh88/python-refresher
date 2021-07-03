import random
answer = random.randint(0,100)
print('ANSWER: ', answer)
clueList = ['hi', 441, 55, '11q']
print(bool(answer%2 == 0))
print(bool(answer%3 == 0))
print(bool(answer%5 == 0))

score = 10

for i in range(0,7):
  guess = input('ENTER YOUR GUESS: ')
  print('ANSWER IN LOOP: ', answer)
  print('GUESS IN LOOP: ', guess)
  if int(guess) == answer:
    print('Bingo')
    break
  else:
    score -= 1
    print('SCORE NOW: ', score)
    print(clueList[random.randint(0, len(clueList)-1)])
