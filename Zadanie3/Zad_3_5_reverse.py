def reverse_in_place(l, left, right):
    l[left:right + 1] = l[right:left - 1:-1]


l = [1, 2, 3, 4, 5, 6]
reverse_in_place(l, 1, 3)
print(l)
