def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

def main():
    e_list = i_list()
    b = i_input()
    l_list = i_list()

    ans_num = 0
    b_num = 0

    for l in l_list:
        if l in e_list:
            ans_num += 1
        if l == b:
            b_num += 1
    
    if ans_num == 6:
        print(1)
    elif ans_num == 5 and b_num == 1:
        print(2)
    elif ans_num == 5:
        print(3)
    elif ans_num == 4:
        print(4)
    elif ans_num == 3:
        print(5)
    else:
        print(0)

if __name__ == '__main__':
    main()
