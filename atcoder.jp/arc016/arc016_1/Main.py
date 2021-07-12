def i_input(): return int(input())
def i_map(): return map(int, input().split())

def main():
    n, m = i_map()
    
    ans_list = [i+1 for i in range(n)]

    for ans in ans_list:
        if ans != m:
            print(ans)
            exit()

if __name__ == '__main__':
    main()
