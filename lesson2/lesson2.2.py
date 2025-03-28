x = int(input("enter number: "))

x1 = (x % 10)
x2 = (x // 10) % 10
x3 = (x // 100) % 10
x4 = (x // 1000) % 10
x5 = x // 10000

print(x1, x2, x3, x4, x5)