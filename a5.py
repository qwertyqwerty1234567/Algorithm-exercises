def main():
    get_points()


def get_points():
    while True:
        try:
            listx = []
            n = input().split()
            for i in range(len(n)):
                listx.append(int(n[i]))

            #solution(listx)
            sum1 = sum(listx)

            ans = (result(listx))
            print(ans, sum1 - ans)
            listx = []
        except EOFError:
            break


def result(listx):
    def result2(listx: int) -> int:
        x = 0
        y = 0
        for i in range(len(listx)):
            x, y = y, max(x + listx[i], y)
        return y

    y = result2(listx[1:])
    x = result2(listx[:-1])
    #return max(x, y) if len(nums) is not 1 else nums[0]
    if len(listx) != 1:
        return max(x, y)
    else:
        return listx[0]

def solution(listx):
    print(listx)


main()