import string
import keyword

name = input("Enter the name: ")
if name[0].isdigit():
    print(False)
elif any(ch.isupper() for ch in name):
    print(False)
elif any(ch in string.punctuation and ch != "_" for ch in name):
    print(False)
elif name.count("__"):
    print(False)
elif " " in name:
    print(False)
elif name in keyword.kwlist:
    print(False)
else:
    print(True)