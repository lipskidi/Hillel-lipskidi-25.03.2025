x = int(input("enter number: "))

x1 = (x % 10)
x2 = (x // 10) % 10
x3 = (x // 100) % 10
x4 = (x // 1000) % 10
x5 = x // 10000

y = x1 * 10000 + x2 * 1000 + x3 * 100 + x4 * 10 + x5

print(y)
