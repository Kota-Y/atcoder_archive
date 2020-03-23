from itertools import combinations

def main():
    n, m = map(int, input().split())

    ans = 0

    n_list = [i+1 for i in range(n)]
    m_list = [i+1 for i in range(m)]

    ans += len(list(combinations(n_list, 2)))
    ans += len(list(combinations(m_list, 2)))

    print(ans)

if __name__ == '__main__':
    main()