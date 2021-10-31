# https://www.realpythonproject.com/day9-pass-by-value-pass-by-reference-and-pythons-pass-by-object-reference/
# Read the above link explanation: pass by Object Reference!!

t = ('a', 'b');
t1 = ('a', 'b')

print('t:  ' + str(id(t)))
print('t1: ' + str(id(t1)))

l = [1, 2]
l1 = [1, 2]

print('l:  ' + str(id(l)))
print('l1: ' + str(id(l1))
)

a = 10
b = 10
c = 11
print('c: ' + str(id(c)))
#pass by value
c = a
print('c: ' + str(id(c)))
d = 12

print('a: ' + str(id(a)))
# print('b: ' + str(id(b)))
# print('d: ' + str(id(d)))

d1 = {"A": 1, "B": 2}
d2 = {"A": 1, "B": 2}
print('d1: ' + str(id(d1)))
print('d2: ' + str(id(d2)))
d3 = d2
#pass by reference
print('d3: ' + str(id(d3)))

x = [1, 2, 3]
print('list before mutation ' + str(id(x)))
x.pop()
x.append(6)
print('list after mutation ' + str(id(x)))
y = x
print('list id of y after assignment of x: ' + str(id(y))) 

tpl = 22, 33, 44, 44
print("tpl id: " + str(id(tpl)))
tpl = 11, 0
print(tpl)
print("tpl id: " + str(id(tpl)))
tpl2 = tpl
print("tpl2 id: " + str(id(tpl)))
tplSet = set(tpl)
print(tplSet)
print("tplSetid: " + str(id(tplSet)))

s1 = "hello"
s2 = s1
print("s1 id: " + str(id(s1)))
print("s2 id: " + str(id(s2)))

s1 = "world"
print("s2: " + s2)
print("s1 id: " + str(id(s1)))
print("s2 id: " + str(id(s2)))