def main():
    a, b, k = map(int, input().split())

    output_list = []

    for i in reversed(range(1,min(a,b)+1)):
        if a % i == 0 and b % i == 0:
            output_list.append(i)

    print(output_list[k-1])

if __name__ == '__main__':
    main()