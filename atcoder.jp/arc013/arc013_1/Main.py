def i_input(): return int(input())
def i_map(): return map(int, input().split())

def main():
    n, m, l = i_map()
    p, q, r = i_map()

    ans = 0

    ans = max(ans, (n//p) * (m//q) * (l//r))
    ans = max(ans, (n//p) * (m//r) * (l//q))
    ans = max(ans, (n//q) * (m//p) * (l//r))
    ans = max(ans, (n//q) * (m//r) * (l//p))
    ans = max(ans, (n//r) * (m//p) * (l//q))
    ans = max(ans, (n//r) * (m//q) * (l//p))

    print(ans)

if __name__ == '__main__':
    main()
