def i_input(): return int(input())
def i_row(N): return [i_input() for _ in range(N)]

def main():
    n = i_input()
    coin_list = i_row(n)

    ans = 0.0

    for i in range(n):
        co = 0
        for j in range(n):
            if i == j:
                continue
            if coin_list[i] % coin_list[j] == 0:
                co += 1

        if co % 2 == 0:
            ans += 1.0 * (co+2) / (2*co+2)
        else:
            ans += 0.5

    print(ans)

if __name__ == '__main__':
    main()
