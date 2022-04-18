def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_row(N): return [i_input() for _ in range(N)]
INF = float('inf')

def main():
    n, k = i_map()
    num_list = i_row(n)

    ruiseki = [0]
    for i in range(n):
        ruiseki.append(num_list[i]+ruiseki[i])

    ans = -INF
    for i in range(n-k):
        ans = max(ans, ruiseki[i+k] - ruiseki[i])

    print(ans)

if __name__ == '__main__':
    main()
