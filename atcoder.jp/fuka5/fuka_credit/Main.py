def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

def main():
    for _ in range(1010):
        n, k = i_map()
        if n == 0 and k == 0:
            exit()
        l = i_list()
        l.sort()
        ans = sum(l[:k])
        print(ans)

if __name__ == '__main__':
    main()
