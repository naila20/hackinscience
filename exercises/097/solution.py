def love_meet(bob, alice):
    for i in bob:
        for j in alice:
            if i == j:
                return sorted(i)
