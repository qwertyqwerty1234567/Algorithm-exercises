import math
import cmath


def distance(p1, p2):
    ans = (p1[0] - p2[0]) ** 2
    ans += (p1[1] - p2[1]) ** 2
    ans = math.sqrt(ans)
    return ans


def get_points():
    list1 = []
    while True:
        try:
            inp = input("")
            # point1 = inp.split()
            pointlist = [int(x) for x in inp.split()]
            list1.append(pointlist)
        except EOFError:
            break
    return list1


def u():
    list1 = []
    yes = True
    while yes:
        try:
            points = input("")
            if not points:
                break
            else:
                cord = [int(x) for x in points.split()]
                list1.append(cord)
        except EOFError:
            break
    return list1


def bruteforce(xval):
    p2 = xval[1]
    p1 = xval[0]
    minimum = distance(xval[0], xval[1])
    len_x1 = len(xval)
    if len_x1 == 2:
        return p1, p2, minimum
    for i in range(len_x1 - 1):
        for j in range(i + 1, len_x1):
            if j != 1 and i != 0:
                d = distance(xval[i], xval[j])
                if d < minimum:
                    minimum = d
                    p1, p2 = xval[i], xval[j]
    return p1, p2, minimum


def calculate(my_points):
    x1 = sorted(my_points, key=lambda x: x[0])
    y1 = sorted(my_points, key=lambda x: x[1])
    a1, a2, d = closest(x1, y1)
    return d


def testrun():
    list1 = []
    yes = True
    while yes:
        try:
            points = input("")
            if not points:
                break
            else:
                cord = [int(x) for x in points.split()]
                list1.append(cord)
        except EOFError:
            break
    return list1


def closest(x1, y1):
    length_x = len(x1)
    if length_x < 4:
        an = bruteforce(x1)
        return an
    middle_value = length_x // 2
    midway = x1[middle_value][0]
    second_half = x1[middle_value:]
    first_half = x1[:middle_value]
    list1 = list()
    list2 = list()

    for x in y1:
        if x[0] < midway + 1:
            list1.append(x)
        elif x[0] >= midway + 1:
            list2.append(x)

    (p1, q1, d1) = closest(first_half, list1)
    (p2, q2, d2) = closest(second_half, list2)

    if d1 < d2 + 1:
        mini = (p1, q1)
        n = d1
    elif d1 >= d2 + 1:
        mini = (p2, q2)
        n = d2

    (p3, q3, d3) = closest_pair(x1, y1, n, mini)

    if n < d3 + 1:
        return mini[0], mini[1], n
    elif n >= d3 + 1:
        return p3, q3, d3


def closest_pair(value_x, value_y, delta, best_value):
    len_x = len(value_x)
    middle_x = value_x[len_x // 2][0]
    list_y = [x for x in value_y if middle_x - delta <= x[0] <= middle_x + delta]
    best = delta
    len_y = len(list_y)
    for i in range(len_y - 1):
        for j in range(i + 1, min(i + 7, len_y)):
            p, q = list_y[i], list_y[j]
            value = distance(p, q)
            if value < best:
                best_value = p, q
                best = value
    return best_value[0], best_value[1], best


def main():
    points = get_points()
    solution = calculate(points)
    solution = int(solution ** 2)
    print(solution)


main()
