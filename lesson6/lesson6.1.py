import string

x = input("Enter 2 letters across -: ")
start_ch, end_ch = x.split('-')
y = string.ascii_letters
start_i = y.index(start_ch)
end_i = y.index(end_ch)
res = y[start_i:end_i + 1]
print(res)