def s_input(): return input()
def s_row(N): return [s_input() for _ in range(N)]

def main():
    str_list = s_row(15)

    str_list.sort()
    
    print(str_list[6])

if __name__ == '__main__':
    main()
