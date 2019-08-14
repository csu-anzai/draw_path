encoding = 'utf-8'


def get_distance(p1, p2):
    distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return distance


def get_arr_distance(arr):
    arr_sum = 0
    for i in range(len(arr) - 1):
        arr_sum += get_distance(arr[i], arr[i + 1])
    return arr_sum


def get_all_distance(arr):
    total_sum = 0
    for arr_ele in arr:
        total_sum += get_arr_distance(arr_ele)
    return total_sum


if __name__ == '__main__':
    arr = [[[1, 1], [1, 1], [1, 1]], [[1, 2], [3, 4], [4, 5]], [[1, 2], [3, 4], [4, 5]]]
    total_distance = get_all_distance(arr)
    print(total_distance)