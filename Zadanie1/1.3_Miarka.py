def draw_miarka(length):
    s = length * '|....' + '|\n0'
    for i in range(1, length+1):
        s+='{:>5}'.format(i) 

    print(s)

length =  int(input("Podaj długość miarki: "))
draw_miarka(length)