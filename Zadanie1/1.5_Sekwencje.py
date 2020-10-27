import random
import string 

def random_sequence(size):
    random_seq = []
    for i in range(0, size):
        random_seq.append(random.choice(string.ascii_letters + string.digits))
    return random_seq



random_seq_sizes = list(input("Podaj wielkości dwóch losowych sekwencji: ").split())

random_seq_a = random_sequence(int(random_seq_sizes[0]))
random_seq_b = random_sequence(int(random_seq_sizes[1]))
print(random_seq_a, '\n', random_seq_b)

print('Część wspólna sekwencji: ', set(random_seq_a).intersection(random_seq_b))
print('Suma bez powtórzeń: ', set(random_seq_a + random_seq_b))