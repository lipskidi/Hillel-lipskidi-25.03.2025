x = int(input("Enter number: "))
while x > 9:
    res = 1
    for digit in str(x):
        res *= int(digit)
    x = res
print("Result: ", x)