def i_input(): return int(input())
def s_input(): return input()
str_list = []

def main():
    n = i_input()
    for _ in range(n):
        s = s_input()
        str_list.append(s)

    ans_list = []
    for s in str_list:
        ans_list.append(s[::-1])

    ans_list.sort()

    for ans in ans_list:
        print(ans[::-1])

if __name__ == '__main__':
    main()
