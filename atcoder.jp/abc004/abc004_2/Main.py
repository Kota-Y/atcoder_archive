def s_input(): return input()
def s_row_list(N): return [list(s_input()) for _ in range(N)]

def main():
    str_list = s_row_list(4)

    for i in range(4):
        for j in range(7):
            print(str_list[3-i][6-j], end='')
        print()

if __name__ == '__main__':
    main()
