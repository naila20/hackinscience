import string
for x in string.ascii_lowercase:
    for y in string.ascii_lowercase:
        if x == y:
             print()
        else:
             print(x + y)
