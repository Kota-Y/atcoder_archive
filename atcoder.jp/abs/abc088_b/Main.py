def main():
    N = int(input())
    num_list = list(map(int, input().split()))
    
    num_list.sort(reverse=True)

    alice, bob = 0,0

    for i in range(N):
        if i % 2 == 0:
            alice += num_list[i]
        else:
            bob += num_list[i]

    print(alice-bob)

if __name__ == '__main__':
    main()