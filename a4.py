from random import randint


def main():
    p = 8000017
    a, b = randint(0, 8000017), randint(0, 8000017)
    email = int(input("enter an email"))
    arrayB = createB(a, b, p)
    if _hash(email, arrayB, a, b, p) == 1:
        print("email is not spam")
    elif _hash(email, arrayB, a, b, p) == 0:
        print("email is spam")


def _hash(x, arrayB,a, b, p):
    if arrayB[hashFunction(x, a, b, p)] == 1:
        return 1
    elif arrayB[hashFunction(x, a, b, p)] == 0:
        return 0


def hashFunction(x, a, b, p):
    ans = ((a*x + b) % p) % 8000000
    return ans


def createB(a, b, p):
    arrayB = []
    for x in range(8000000):
        arrayB.append(0)
    for i in range(1000000):
        nonspam = hashFunction(i, a, b, p)
        arrayB[nonspam] = 1
    return arrayB


main()







