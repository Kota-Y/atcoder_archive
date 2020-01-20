def main():
    a,b = map(int,input().split())

    al = [a]*b
    bl = [b]*a

    if al > bl:
        print(''.join(map(str,bl)))
    else:
        print(''.join(map(str,al)))


if __name__ == '__main__':
    main()