def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]

def main():
    n = i_input()
    num_list = i_row(n)
    
    print(min(num_list))

if __name__ == '__main__':
    main()
