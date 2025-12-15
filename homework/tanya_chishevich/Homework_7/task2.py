words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def calc_world(word):
    for i, j in word.items():
        print(i * j)


calc_world(words)
