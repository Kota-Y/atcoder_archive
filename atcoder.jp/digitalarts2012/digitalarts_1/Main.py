def i_input(): return int(input())
def s_input(): return input()
def s_row(N): return [s_input() for _ in range(N)]

def main():
    s = s_input()
    n = i_input()
    ng_list = s_row(n)
    
    s_list = s.split(' ')

    for s in s_list:
        flag = True
        for ng in ng_list:
            if len(ng) != len(s):
                continue
            for i in range(len(s)):
                if s[i] == ng[i] or ng[i] == '*':
                    continue
                break
            else:
                print('*'*len(s), end=' ')
                flag = False
                break
        if flag:
            print(s, end= ' ')

    print()

if __name__ == '__main__':
    main()
