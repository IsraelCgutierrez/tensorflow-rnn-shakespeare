import numpy as np
import random
import my_txtutils


# tab = 1
# space = 2
# all chars from 32 to 126 = c-30
# LF mapped to 127-30


def getLower():
    choices = [int(random.uniform(67, 92)), 2, 127 - 30]
    return np.random.choice(choices, 1, p=[0.9, 0.08, 0.02])


def getUpper():
    choices = [int(random.uniform(35, 60)), 2, 127 - 30]
    return np.random.choice(choices, 1, p=[0.9, 0.08, 0.02])


def get_char(d):
    c = getLower() if d == 0 else getUpper()
    return chr(my_txtutils.convert_to_alphabet(c))


start = 0
steps = 1024*2000
end = 2

# print(my_txtutils.encode_text("a bcz"))
# print(my_txtutils.encode_text("A BCZ"))

for i in range(start, end):
    with open("ABC_DATA/" + str(i) + ".txt", 'w+') as f:
        content = list(map(lambda x: get_char(i), list(range(0, steps))))
        f.write(str("".join(content)))
