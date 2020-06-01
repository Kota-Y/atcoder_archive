def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

def main():
    n, k = i_map()
    num_list = i_list()

    num_list.sort()

    rate = 0

    num_list = num_list[n-k:]

    for num in num_list:
        rate = (rate+num) / 2

    print(rate)

if __name__ == '__main__':
    main()
