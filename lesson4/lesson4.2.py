lst = [0, 1, 7, 2, 4, 8]

if not lst:
    res = 0
else:
    x = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            x += lst[i]
    y = lst[-1]
    res = x * y

print(res)

