list = [16, 32, 64, 8]

if len(list) > 1:
    x = list.pop()
    list.insert(0, x)
    print(list)
else:
    print(list)