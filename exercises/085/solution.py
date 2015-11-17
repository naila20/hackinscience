def sort_a_list(l):
    return sorted(l, key=int, reverse=True)


from operator import itemgetter
def sort_by_mark(my_class):
    for i in sorted(my_class, key=itemgetter(0), reverse=True):
        print(i)


from operator import itemgetter
def sort_by_name(my_class):
    for i in sorted(my_class, key=itemgetter(1)):
        print(i)
