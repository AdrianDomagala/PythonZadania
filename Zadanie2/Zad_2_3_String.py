import re
from collections import Counter

def stringStatistic(s):
    lstWords = re.findall(r'\w+', s)
    words = ''.join(lstWords)
    countedLetters = Counter(words.lower())
    print('Liczba słów: ', len(words), ' Liczba liter: ', len(words))
    print('Liczba wystąpień każdej z liter (wielkość jest ignorowana): ')
    [print(key, value) for key, value in countedLetters.items()]


s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque "
stringStatistic(s)