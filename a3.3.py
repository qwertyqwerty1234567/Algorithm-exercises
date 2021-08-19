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
    listx.sort(key=lambda x: x[0])


def solution(listx):
    sol = []
    setx = [listx[0]]
    curr = listx[0]
    for x in listx:
        if x[0] <= curr[1] <= x[1]:

            setx.append(x)
            curr = x

        elif x[0] > curr[1]:

            sol.append(setx)
            setx = [x]

            curr = x


    sol.append(setx)

    maxx = []


    for a in sol:

        last = int(a[-1][1])
        first = int(min(a[0]))
        dist = last - first
        maxx.append(dist)
    print(max(maxx))



main()