def main():
    n = int(input())

    evidences = [[] for _ in range(n)]

    for i in range(n):
        a = int(input())
        for _ in range(a):
            x, y = map(int, input().split())
            evidences[i].append((x - 1, y))

    ans = 0

    for i in range(1, 2 ** n):
        consistent = True
        for j in range(n):
            if (i >> j) & 1 == 0:
                continue
            for x, y in evidences[j]:
                if (i >> x) & 1 != y:
                    consistent = False
                    break
            if not consistent:
                break
        if consistent:
            ans = max(ans, bin(i)[2:].count('1'))

    print(ans)

if __name__ == '__main__':
    main()
