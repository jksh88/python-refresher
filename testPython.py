import random, sys, os, math
import copy, pprint
# print('I am Jay')
# age = input()
# # print(len('AAI') + float('8'))
# # print(int('42') == 42)
# # name = 'Jay'
# # if name == 'Alice':
# #   print('got it!')
# # elif name == 'Jay':
# #   print('close')
# if age:
#   print('I am ' + str(age) + ' years young')
# else: 
#   print('not yet')
# firstVal = 3
# while firstVal != 0:
#   print(firstVal)
#   firstVal -= 1

# name = ''
# while True:
#   print ('please enter your name')
#   name = input()
#   if name == 'jay':
#     continue
# print('thanks')

# print(range(20))
# print(random.randint(0, 20))
# total = 0
# count = 0
# for count in range(5, 0, -1):
#   print('first count ' + str(count))
#   total += 3
#   count += 1
#   if total > 20:
#     break
#   print("total now" + str(total))
#   sys.exit()
#   print("count now" + str(count))
# print ('last count: ' + str(count))

# def spam():
#   # eggs = 99
#   bacon()
#   print(eggs)

# def bacon():
#   ham = 101
#   eggs = 14
#   # print(eggs)

# eggs = 88
# spam()
# print(eggs)

# numerator = 42
# def divBy(num):
#   try:
#     print( numerator / num)
#   except:
#     print('Error')

# divBy(21)
# divBy(12)
# divBy(0)
# divBy(10)

# print('How many cats?')
# myCats = input()
# def response(num):
#  try:
#   if int(num) >= 3:
#     print(' a lot')
#   elif int(num) < 0:
#     print('Enter a positive number')
#   else:
#     print('You can handle it')
#  except ValueError:
#    print('Enter a number')
#  except TypeError: 
#     print('Enter a number')

# response(myCats)
# num = random.randint(1, 20)
# guess = None

# def guessNum(answer):
#   for i in range(1,7):
#     try:
#       print('Take a guess')
#       guess = int(input())
#       if guess == answer:
#         print('Bingo!')
#         break
#       elif guess < answer:
#         print('Your guess is too low')
#       elif guess > answer:
#         print('Your guess is too high')
#     except ValueError:
#       print('Enter a number')

# guessNum(num)
# print(guess)
# print(num)

# print(len(list(range(0,10,2))))

# for i in list(range(0,10,2)):
#   print(i)
 
# #   print(str(i) + ' go')

# cat = [1,2,5]
# me, you, him = cat
# print(you)

# a, b, c = 33, 44, 55
# print(c, b)

# a, b, c = c, b, a
# # answer = input()
# print(c, b)

# spam = ['heloo', 'yyoo', 'jo', 'mama', 'Ddd']
# spam.append('haha')
# spam.insert(1, 'shush')
# spam.remove('yyoo')

# # spam = 'sample'
# spam.sort(key = str.lower)
# # spam.reverse()
  


# # idx = spam.index('yyoo')
# # print(idx)
# print(spam)

# name = 'Zuloo'

# print('o' in name)

# def eggs(arg):
#   arg.append('Say what now?')

# print(eggs([]))
# testList = []
# newList = testList.append('yoo')
# print(testList)
# thirdList = copy.deepcopy(testList)
# thirdList.append(100)
# print(testList, thirdList)
# shallowCopyList = testList
# testList.append('me')
# print(shallowCopyList, testList)
# print('I am here' + \
#   'today')
# shallowCopyList.append('him')
# person1 = {'height': 199, 'weigt': 95, 'age': 33}

# # print('yoo' in shallowCopyList)
# # print(person1.keys())
# # print(person1.items())
# # if 'weigt' in person1:
# person1.setdefault('heigt', 0)
# print(person1)

# person1.setdefault('color', 'black')
# print(person1)
# if 'ethnicity' not in person1:
#   person1['ethnicity'] = 'brown'
# print(person1)

str = 'prommenade'

count = {}

for ltr in str.upper():
  if ltr in count:
    count[ltr] += 1
  else:
    count[ltr] = 1

pprint.pprint(count)
pprint.pformat(count)
