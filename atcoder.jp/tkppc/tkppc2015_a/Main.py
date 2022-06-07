def i_input(): return int(input())
def i_map(): return map(int, input().split())

def main():
    n = i_input()
    for _ in range(n):
        a, b = i_map()
        print(a+b)

if __name__ == '__main__':
    main()
