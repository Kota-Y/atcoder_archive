def i_input(): return int(input())

def main():
    n = i_input()

    num_list = [1, 2, 3, 4, 5, 6]

    for i in range(n%30):
        x, y = num_list[i%5], num_list[i%5+1]
        num_list[i%5] = y
        num_list[i%5+1] = x

    print(*num_list, sep='')

if __name__ == '__main__':
    main()
