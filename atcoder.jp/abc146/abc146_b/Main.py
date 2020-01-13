def main():
    N = int(input())
    S = input()

    slist = list(S)
    result = slist

    for i in range(len(S)):
        if ord(slist[i]) + N > 90:         
            result[i] = chr(ord(slist[i]) + N - 26)
        else:
            result[i] = chr(ord(slist[i]) + N)

    print(''.join(result))

if __name__ == '__main__':
    main()