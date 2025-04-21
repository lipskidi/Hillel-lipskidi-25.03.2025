import string

x = input("Enter string: ")
y = ''.join(ch for ch in x if ch not in string.punctuation)
wrd = y.split()
wrd2 = [word.capitalize() for word in wrd]
j = ''.join(wrd2)
h = '#' + j
h = h[:140]
print(h)
