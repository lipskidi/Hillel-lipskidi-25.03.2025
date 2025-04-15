import random

x = random.randint(3,10)

lst1 = [random.randint(1,10) for _ in range(x)]

lst2 = [lst1[0], lst1[2], lst1[-2]]

print(lst1)
print(lst2)