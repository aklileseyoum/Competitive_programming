if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    high = max(arr)
    second = min(arr[0], arr[1])
    if high == second:
        second = min(arr[2], arr[n - 1])
    for i in arr:
        if i > second and i != high:
            second = i
    print(second)
