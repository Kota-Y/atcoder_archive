def main():
    A = int(input())
    B = int(input())

    result = [1, 2, 3]

    result.remove(A)
    result.remove(B)

    print(result[0])

if __name__ == '__main__':
    main()