from math import floor

def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]

def main():
    n = i_input()
    num_list = i_row_list(n)
    
    ans = 0

    for a, b in num_list:
        ans += a * b

    print(floor(ans*1.05))

if __name__ == '__main__':
    main()
