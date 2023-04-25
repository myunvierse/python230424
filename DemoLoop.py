# DemoLoop.py
value = 5

while value >0:
    print(value)
    value -=1

lst = [100,200,300]
fruit = {"apple":100, "kiwi":200}
for item in fruit.items():
    print(item)

print("---break 구문---")
lst =list(range(1,11))
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue 구문---")
lst =list(range(1,11))
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))
    

print("--- range 함수 ---")
print(list(range(2000,2024)))
print(list(range(1,32)))
print(list(range(1,11)))
print("--- list comprehension ---")
print([i**2 for i in lst if i > 5])
fruits = {100:"apple",200:"orange"}
print([v.upper() for v in fruits.values()])

print("--- filtering X ---")
lst =[10,25,30]
itemL = filter(None,lst)
for i in itemL:
    print(i)

print("--- filtering func---")
lst =[10,25,30]
def getBiggerThen20(i):
    return i > 20
itemL = filter(getBiggerThen20,lst)
for i in itemL:
    print(i)

print("--- filtering with lambda---")
lst =[10,25,30]

itemL = filter(lambda x:x>20,lst)
for i in itemL:
    print(i)    