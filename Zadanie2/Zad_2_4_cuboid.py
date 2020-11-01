def cuboidCoordinates():
    args = input('Podaj x:  y:  z:  n: ')
    x, y, z, n = args.split()
    coordinates = [(i, j, k) for i in range(0, int(x)+1) for j in range(0, int(y)+1) for k in range(0,int(z)+1) if i + j + k != int(n)]
    return coordinates

print(cuboidCoordinates())