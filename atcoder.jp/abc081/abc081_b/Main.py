def main():
    N = int(input())
    nums = list(map(int, input().split()))

    count = 0
    flag = True

    while(flag):
        for num in nums:
            if num % 2 == 0:
                continue
            else:
                flag = False
                break
        nums = [n/2 for n in nums]
        count += 1

    print(count-1)

if __name__ == '__main__':
    main()
