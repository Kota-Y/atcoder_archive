from math import factorial
def com(n,r):
    if n<r:
        return 0
    return int(factorial(n) // factorial(r) // factorial(n-r))

def main():
    n = int(input())
    str_list = [input() for _ in range(n)]

    count = 0

    for i,s in enumerate(str_list):
        str_list[i] = sorted(s)

    str_list = sorted(str_list)

    i = 0
    j = 1
    while i < n:
        tmp = 0
        while i + j < n and str_list[i] == str_list[i + j]:
            tmp += 1
            j += 1
        if tmp != 0:
            count += com(tmp+1, 2)
        i += j
        j = 1

    print(count)

if __name__ == '__main__':
    main()