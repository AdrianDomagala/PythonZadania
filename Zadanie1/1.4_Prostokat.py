def draw_rectangle(x, y):
    first_line = x * '+---' + '+\n'
    second_line = x * '|   ' + '|\n'
    s = y * (first_line + second_line) + first_line
    print(s)


y = int(input('Podaj ilość kratek w pionie: '))
x = int(input('Podaj ilość kratek w poziomie: '))

draw_rectangle(x, y)