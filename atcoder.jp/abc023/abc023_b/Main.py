from collections import deque

def main():
    n = int(input())
    s = input()

    if n % 2 == 0:
        print(-1)
        exit()

    for i in range(303):
        if i == 0:
            d = deque('b')
        elif i % 3 == 1:
            d.appendleft('a')
            d.append('c')
        elif i % 3 == 2:
            d.appendleft('c')
            d.append('a')
        elif i % 3 == 0:
            d.appendleft('b')
            d.append('b')
        if 2 * i + 1 == n:
            if ''.join(d) == s:
                print(i)
            else:
                print(-1)
            exit()

if __name__ == '__main__':
    main()