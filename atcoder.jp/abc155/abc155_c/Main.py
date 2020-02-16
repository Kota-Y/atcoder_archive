import collections

def main():
    n = int(input())
    str_list = [input() for _ in range(n)]

    if len(str_list) == len(set(str_list)):
        str_list.sort()
        print(*str_list,sep='\n')
        exit()

    count_list = collections.Counter(str_list)

    max_num = max(count_list.values())

    output_list = []

    for k, v in count_list.items():
        if max_num == v:
            output_list.append(k)

    output_list.sort()

    print(*output_list,sep='\n')

if __name__ == '__main__':
    main()
