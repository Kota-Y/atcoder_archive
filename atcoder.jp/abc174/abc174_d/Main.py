import sys, re
def i_input(): return int(input())
def s_input(): return input()
sys.setrecursionlimit(10 ** 6)

def main():
    n = i_input()
    s = list(s_input())

    r_count = s.count('R')
    w_count = n - r_count

    if r_count == n or w_count == n:
        print(0)
        exit()

    r_s = s[::-1]

    count = 0

    index = 0
    for i in range(len(s)):
        if r_s[i] == 'W':
            continue
        for j in range(index, n - i - 1):
            if s[j] == 'R':
                index = j + 1
                continue
            index = j + 1
            count += 1
            break

    print(min(count, min(r_count, w_count)))

if __name__ == '__main__':
    main()
