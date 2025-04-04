x = int(input("n1: "))
y = int(input("n2: "))
act = input("act: ")
if act == "+":
    res = x + y
elif act == "-":
    res = x - y
elif act == "*":
    res = x * y
elif act == "/":
    if y == 0:
        print("not devisible by 0")
        res = None
    else:
        res = x / y
else:
    print("Mistake action")
    res = None
print(res)