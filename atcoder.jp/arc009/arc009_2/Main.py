def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def s_input(): return input()
def s_row(N): return [s_input() for _ in range(N)]

def main():
    tmp_list = i_list()
    n = i_input()
    s_list = s_row(n)

    cur_list = []
    for i in range(10):
        cur_list.append(i)

    d2 = dict()
    for i in range(10):
        d2[tmp_list[i]] = cur_list[i]

    ans_list = []
    for s in s_list:
        tmp_s = ''
        for i in range(len(s)):
            tmp_s += str(d2[int(s[i])])
        ans_list.append([int(tmp_s), s])

    ans_list.sort()

    for ans in ans_list:
        print(ans[1])

if __name__ == '__main__':
    main()
