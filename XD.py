import random


def xd(sen):
    a = True
    x = len(sen)
    for i in range(x):
        if sen[i] != " " and a == True:
            xx = random.randrange(1,3)
            if xx == 2:
                a = False
        if sen[i] != " " and a == False:
            sen[i] = sen[i].upper()
            a = True
    print(sen)


def main():
    sen = input("Input sentence(s): ")
    xd(sen)


main()
