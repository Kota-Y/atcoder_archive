def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_row(N): return [i_input() for _ in range(N)]

def main():
    n, m = i_map()
    num_list = i_row(m)
    
    l = [i for i in range(1, n+1)]

    now = 0
    for num in num_list:
        if num not in l:
            continue
        index = l.index(num)
        l[index] = now
        now = num
       
    for ans in l:
        print(ans)

if __name__ == '__main__':
    main()
