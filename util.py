import random
def colid(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
def randomGrid():
    return (random.randint(10, 580)//10 * 10, random.randint(10, 380)//10 * 10)

