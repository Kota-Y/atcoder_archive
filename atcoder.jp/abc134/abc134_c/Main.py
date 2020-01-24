import copy

def main():
    n = int(input())
    num_list = [int(input()) for _ in range(n)]

    tmp = copy.deepcopy(num_list)
    tmp.sort()

    max_first = max(num_list)
    max_second = tmp[n-2]
    
    for num in num_list:
        if num == max_first:
            print(max_second)
            continue
        print(max_first)
        
if __name__ == '__main__':
    main()