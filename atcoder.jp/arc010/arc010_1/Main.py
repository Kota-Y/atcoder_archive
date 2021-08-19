def i_input(): return int(input())
def i_map(): return map(int, input().split())

def main():
    n, m, a, b = i_map()

    for i in range(m):
        c = i_input()
        if n <= a:
            n += b
        n -= c
        if n < 0:
            print(i+1)
            exit()

    print('complete')

if __name__ == '__main__':
    main()
