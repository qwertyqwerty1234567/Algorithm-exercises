
def main():
    get_points()


def get_points():
    n = input()
    n = int(n)
    for i in range(n):
        listx = []
        line = input().split()
        for j in range(0, len(line), 2):
            list1 = []
            list1.append(int(line[j]))
            list1.append(int(line[j+1]))
            listx.append(list1)

        sortx(listx)

        solution(listx)


def sortx(listx):
    listx.sort(key=lambda x: x[1])


def solution(listx):
    count = 1
    curr = int(listx[0][1])
    for i in range(len(listx)):
        if curr < int(listx[i][0]):
            count += 1
            curr = int(listx[i][1])
    print(count)


main()