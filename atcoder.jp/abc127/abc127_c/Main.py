def main():
    n, m = map(int, input().split())

    card_list = [0] * n

    l_list = []
    r_list = []

    for _ in range(m):
        l, r = map(int, input().split())
        l_list.append(l)
        r_list.append(r)

    max_l = max(l_list)
    min_r = min(r_list)

    print(min_r-max_l+1 if min_r >= max_l else 0)

if __name__ == '__main__':
    main()