from array import *
import random

collection = array('i',[])

for i in range(0, 5):
    num = random.randint(0,32000)
    collection.append(num)

for i in collection:
    print(i)

print(collection)