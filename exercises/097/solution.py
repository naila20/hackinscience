def love_meet(bob, alice):
    list = []
    for i in bob:
        for j in alice:
            if i == j:
                list.append(i)
                list2 = set(list)
    return sorted(list2)


def affair_meet(bob, alice, silvester):
     list = []
     for i in bob:
         for j in alice:
             for k in silvester:
                 if i != j and j == k:
                    list.append(j)
                    list2 = set(list)
     return sorted(list2)
