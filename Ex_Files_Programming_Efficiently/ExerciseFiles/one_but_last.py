#https://app.coderpad.io/sandbox

from random import randint 
mylist=[]

def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

for i in range(100):
    mylist.append(randint(0,100))

print("normal", mylist)
mylist.sort()
print("reverse", mylist[::-1])
print("one but last", mylist[::-1][1:2])
print()

for i in range(100):
    mylist.append(randint(0,100))

mylist.sort(reverse=True)
print("new list", mylist)
print("new list sliced", mylist[1:2])

for i in range(100):
    mylist.append(randint(0,100))

print("max:", max(mylist))

# pandas.nlargest(mylist)

print("sorted", sorted(mylist)[-3:-2])
