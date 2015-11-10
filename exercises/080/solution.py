import string
for x in string.ascii_lowercase:
    for y in string.ascii_lowercase:
        if y <= x:
            pass
        else:
            print(x + y)
