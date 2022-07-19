def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

def main():
    n, k = i_map()
    num_list = i_list()

    num_list.sort(reverse=True)

    co = 0
    for i, num in enumerate(num_list):
        co += num
        if co >= k:
            print(i+1)
            exit()
    
    print(-1)

if __name__ == '__main__':
    main()
