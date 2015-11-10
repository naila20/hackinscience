import string
for x in string.ascii_lowercase:
    for y in string.ascii_lowercase:
        if x == y:
            pass
        else:
            print(x + y)
