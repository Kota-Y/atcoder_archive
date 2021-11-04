def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

def main():
    n = i_input()

    ans = 0
    for _ in range(n):
        tmp_l = i_list()
        if sum(tmp_l) < 20:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
