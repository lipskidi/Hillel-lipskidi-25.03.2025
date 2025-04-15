list = [1, 2, 3]
if len(list) == 0:
    res = [[], []]
else:
    middle = (len(list) + 1) // 2
    list1 = list[:middle]
    list2 = list[middle:]
    res = [list1, list2]
print(res)