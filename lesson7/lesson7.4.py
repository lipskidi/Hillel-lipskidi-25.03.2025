def common_elements():
    lst1 = [x for x in range(100) if x % 3 == 0]
    lst2 = [x for x in range(100) if x % 5 == 0]
    res = set(lst1).intersection(set(lst2))
    return res
x = {0, 75, 45, 15, 90, 60, 30}
assert common_elements() == x
print("Done")