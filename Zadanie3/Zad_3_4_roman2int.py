roman = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}


def roman2int(num_in_roman: str):
    num_in_arabic = 0
    while len(num_in_roman) > 0:
        if len(num_in_roman) > 1 and ((n := num_in_roman[:2]) in roman.keys()):
            num_in_arabic += roman[n]
            num_in_roman = num_in_roman[2:]
        else:
            n = num_in_roman[0]
            num_in_arabic += roman[n]
            num_in_roman = num_in_roman[1:]
    return num_in_arabic


print(roman2int('I'))
print(roman2int('IV'))
print(roman2int('CMXCVIII'))  # 998
print(roman2int('XCIV'))  # 44
print(roman2int('MMDCCCLXII'))  # 2862
print(roman2int('CXVIII'))

# dict make in different way
roman_2 = dict([
    ('I', 1),
    ('IV', 4),
    ('V', 5),
    ('IX', 9),
    ('X', 10),
    ('XL', 40),
    ('L', 50),
    ('XC', 90),
    ('C', 100),
    ('CD', 400),
    ('D', 500),
    ('CM', 900),
    ('M', 1000)
])
