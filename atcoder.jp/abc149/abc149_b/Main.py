def main():
    A, B, K = map(int, input().split())

    if K < A:
        A = A - K
    elif K <= A + B:
        B = B - K + A
        A = 0
    else:
        A, B = 0,0

    print('{} {}'.format(A, B))

if __name__ == '__main__':
    main()