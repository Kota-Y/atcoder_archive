def main():
    a,b,c,d = map(int, input().split())

    left = a + b
    right = c + d

    if left == right:
        print('Balanced')
    elif left > right:
        print('Left')
    else:
        print('Right')

if __name__ == '__main__':
    main()