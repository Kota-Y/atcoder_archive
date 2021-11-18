def i_input(): return int(input())
def s_input(): return input()
def s_row(N): return [s_input() for _ in range(N)]
str_list = []

def main():
    n = i_input()
    str_list = s_row(n)
    
    s = set()
    before_s = ''
    for i in range(n):
        tmp = str_list[i]
        if tmp in s:
            if i % 2 == 0:
                print('LOSE')
            else:
                print('WIN')
            exit()
        if i != 0 and before_s != tmp[0]:
            if i % 2 == 0:
                print('LOSE')
            else:
                print('WIN')
            exit()   
        s.add(tmp)
        before_s = tmp[-1]

    print('DRAW')

if __name__ == '__main__':
    main()
