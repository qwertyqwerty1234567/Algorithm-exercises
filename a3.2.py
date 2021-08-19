def main():
    get_points()


def get_points():
    n = input()
    n = int(n)
    total = []
    for i in range(n):
        listx = []
        line = input().split()
        for j in range(0, len(line), 2):
            list1 = []
            list1.append(int(line[j]))
            list1.append(int(line[j+1]))
            listx.append(list1)

        sortx(listx)
        total.append(listx)
    for x in total:
        solution(x)




def sortx(listx):
    listx.sort(key=lambda x: x[1])


def solution(listx):
    minx = min(listx)
    minimum = minx[0]
    counts = 0
    for i in range(minimum, listx[-1][1]+1):
        xx = 0
        for x in listx:
            if x[0] <= i <= x[1]:
                xx += 1
        if xx > counts:
            counts = xx

    print(counts)



main()