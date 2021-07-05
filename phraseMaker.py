comment = ''
while True:
  value = input("Say something: ")
  if value == "\end":
    print(comment[:-1])
    break
  else: 
    comment = comment + (value + ' ')
    continue 