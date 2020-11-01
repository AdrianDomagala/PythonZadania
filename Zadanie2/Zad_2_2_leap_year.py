def isLeapYear():
    year = int (input("Podaj rok (1900-100000): "))
    while(1900 > year or year > 100000):
        year = int (input("Podaj rok z zakresu (1900-100000): "))
    
    if(year % 400 == 0):
        return True
    elif(year % 100 == 0):
        return False
    elif(year % 4 == 0):
        return True
    else:
        return False
