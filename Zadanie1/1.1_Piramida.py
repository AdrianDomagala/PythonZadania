def draw_pyramid(pyramid_size):
    i = 0
    while(i < pyramid_size//2 + 1 ):
        print((i * " ") + ((pyramid_size-2*i) * '*') + (i * ' '))
        i+=1



pyramid_size = int (input("Jak dużą piramidę zbudować? Podaj nieparzystą liczbę: "))

while(pyramid_size % 2 == 0):
    pyramid_size = int (input("Prosiłem o nieparzystą liczbę... podaj inną:"))

draw_pyramid(pyramid_size)