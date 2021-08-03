def i_input(): return int(input())
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())

def main():
    n = i_input()
    str_list = s_list()

    ans_list = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']

    ans = 0

    for s in str_list:
        if s[len(s)-1] == '.':
            s = s[:len(s)-1]
        if s in ans_list:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()
