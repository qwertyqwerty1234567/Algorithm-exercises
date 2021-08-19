import math
import cmath


def closest_pair(value_x, value_y, best, bv):
    len_x = len(value_x)
    middle_x = value_x[len_x // 2][0]
    list_y = [x for x in value_y if middle_x - best <= x[0] <= middle_x + best]
    len_y = len(list_y)
    best1 = best
    for i in range(len_y - 1):
        for j in range(i + 1, min(i + 7, len_y)):
            p = list_y[i]
            q = list_y[j]
            value = distance(p, q)
            if value < best1:
                best1 = value
                bv = p, q
    return bv[0], bv[1], best1


def bruteforce(x_value):
    p2 = x_value[1]
    p1 = x_value[0]
    minimum = distance(x_value[0], x_value[1])
    len_x1 = len(x_value)
    if len_x1 == 2:
        return p1, p2, minimum
    for i in range(len_x1 - 1):
        for j in range(i + 1, len_x1):
            if j != 1 and i != 0:
                d = distance(x_value[i], x_value[j])
                if minimum > d:
                    p1, p2 = x_value[i], x_value[j]
                    minimum = d
    ret = min(p1, p2)
    return ret


def closest(my_x, my_y):
    length_x = len(my_x)
    if length_x < 4:
        an = bruteforce(my_x)
        return an
    middle_value = length_x // 2
    midway = my_x[middle_value][0]
    second_half = my_x[middle_value:]
    first_half = my_x[:middle_value]
    list1 = list()
    list2 = list()

    for x in my_y:
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

    (p3, q3, d3) = closest_pair(my_x, my_y, n, mini)

    if n < d3 + 1:
        return mini[0], mini[1], n
    elif n >= d3 + 1:
        return p3, q3, d3


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


def test_points():
    lsit1 = []
    while True:
        try:
            user = input("")
            cord = [int(x) for x in user.split()]
            lsit1.append(cord)
        except EOFError:
            break
    return lsit1


def distance(p1, p2):
    ans = (p1[0] - p2[0])**2
    ans += (p1[1] - p2[1])**2
    ans = math.sqrt(ans)
    return ans


def calculate(my_points):
    x1 = sorted(my_points, key=lambda x: x[0])
    y1 = sorted(my_points, key=lambda x: x[1])
    a1, a2, d = closest(x1, y1)
    return d


def main():
    points = test_points()
    solution = calculate(points)
    solution = int(solution**2)
    print(solution)


main()





