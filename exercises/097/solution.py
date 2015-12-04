def love_meet(bob, alice):
    list = []
    for i in bob:
        for j in alice:
            if i == j:
                list.append(i)
                list2 = set(list)
    return set(list2)


def affair_meet(bob, alice, silvester):
    res = []
    for j in alice:
        for k in silvester:
            if j == k and j not in bob:
                res.append(j)
    return set(res)
