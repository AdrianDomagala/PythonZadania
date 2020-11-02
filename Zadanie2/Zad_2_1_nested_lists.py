def depestNested(lst):
    for elem in lst:
        if(type(elem) == list):
            elem = depestNested(elem)
            return lst
    lst.append(lst[-1]+1)
    return lst

lst =  [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
print(depestNested(lst))