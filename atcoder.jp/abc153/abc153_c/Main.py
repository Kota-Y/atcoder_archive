def main():
    n, k = map(int, input().split())
    hit_list = list(map(int, input().split()))

    hit_list.sort(reverse=True)

    if n <= k:
        print(0)
        exit()

    for i in range(k):
        hit_list[i] = 0

    print(sum(hit_list))

if __name__ == '__main__':
    main()