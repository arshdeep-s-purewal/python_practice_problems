if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr)
    arr = list(s)
    arr.sort(reverse = True)
    print(arr[1])