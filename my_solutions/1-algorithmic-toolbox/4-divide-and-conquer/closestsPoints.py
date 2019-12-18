

def brute_force(arr):
    min_d = calc_distance(arr[0], arr[1])
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            min_d = min(min_d, calc_distance(arr[i], arr[j]))
    return min_d

def calc_distance(x1, x2):
    return ((x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2) ** 0.5


def unite(arr, mid, min_d, y_sorted):
    mid_x = arr[mid][0]
    min_x = mid_x - min_d
    max_x = mid_x + min_d
    to_compute = [x for x in y_sorted if min_x <= x[0] <= max_x]
    if len(to_compute) == 0:
        return min_d
    for i in range(0, len(to_compute) - 1):
        for j in range(i+1, min(i+7, len(to_compute))):
            min_d = min(min_d, calc_distance(to_compute[i], to_compute[j]))
    return min_d


def closests_points(arr, y_sorted):
    if len(arr) <= 3:
        min_d = brute_force(arr)
        return min_d
    mid = len(arr) // 2
    small_arr = arr[mid:]
    arr_set_big = set(small_arr)
    y_sorted_big = []
    y_sorted_small = []
    for var in y_sorted:
        if var in arr_set_big:
            y_sorted_big.append(var)
        else:
            y_sorted_small.append(var)
    d1 = closests_points(small_arr, y_sorted_big)
    d2 = closests_points(arr[: mid], y_sorted_small)
    min_d = min(d1, d2)
    min_d = unite(arr, mid, min_d, y_sorted)
    return min_d


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(tuple(int(x) for x in input().split()))
    arr.sort(key=lambda x: x[0])
    y_sorted = sorted(arr, key=lambda x: x[1])
    number = closests_points(arr, y_sorted)
    print('{0:.9f}'.format(number))
