def main():
    n = int(input())
    s = input()

    sum_count = s.count('R') * s.count('G') * s.count('B')

    r_list = set()
    g_list = set()
    b_list = set()

    for i in range(n):
        if s[i] == 'R':
            r_list.add(i)
        elif s[i] == 'G':
            g_list.add(i)
        elif s[i] == 'B':
            b_list.add(i)

    for r in r_list:
        for g in g_list:
            L = g - r
            if g + L in b_list:
                sum_count -= 1
            if r - L in b_list:
                sum_count -= 1
            if L % 2 == 0 and L//2 + r in b_list:
                sum_count -= 1

    print(sum_count)

if __name__ == '__main__':
    main()