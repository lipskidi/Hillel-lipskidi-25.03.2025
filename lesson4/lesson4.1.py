lst = [0, 2, 122, 6, 0, 5, 0, 22]

x = len(lst)

while 0 in lst:
    lst.remove(0)

y = x - len(lst)
lst += [0] * y

print(lst)

