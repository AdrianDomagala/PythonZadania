import random
import numpy as np

PROBABILITY = 0.2


def unique_random(quantity=100, scope=1000):
    try:
        return random.sample(range(0, scope), quantity)
    except ValueError:
        print("Range size is to small")


def unique_random_sorted(quantity=100, scope=1000):
    random_list = unique_random(quantity, scope)
    random_list.sort()
    return random_list


def unique_almost_sorted(quantity=100, scope=1000):
    random_list = unique_random_sorted(quantity, scope)
    for i in range(len(random_list) - 1):
        if __change(PROBABILITY):
            random_list[i], random_list[i + 1] = random_list[i + 1], random_list[i]
    return random_list


def unique_almost_sorted_reverse(quantity=100, scope=1000):
    random_list = unique_almost_sorted(quantity, scope)
    random_list.reverse()
    return random_list


def nonunique_random(quantity=100, min=0, max=50):
    return [random.randint(min, max) for r in range(0, quantity)]


def random_floats_from_Gaussian_distribution(centre=0.0, sigma=1, quantity=1000):
    return np.random.normal(centre, sigma, quantity)


def __change(probability):
    return random.random() < probability

