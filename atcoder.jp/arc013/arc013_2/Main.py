def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

def main():
    n = i_input()

    a = []
    b = []
    c = []

    for _ in range(n):
        l = i_list()
        l.sort(reverse=True)
        a.append(l[0])
        b.append(l[1])
        c.append(l[2])

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    print(a[0] * b[0] * c[0])

if __name__ == '__main__':
    main()
