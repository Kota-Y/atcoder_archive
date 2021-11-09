from math import ceil
from collections import Counter
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def s_input(): return input()

def main():
    n, m = i_map()
    s = s_input()
    t = s_input()

    s_co = Counter(s)
    t_co = Counter(t)

    ans = 0
    for k, v in s_co.items():
        if k in t_co:
            ans = max(ans, ceil(v/t_co[k]))
        else:
            print(-1)
            exit()

    print(ans)

if __name__ == '__main__':
    main()
