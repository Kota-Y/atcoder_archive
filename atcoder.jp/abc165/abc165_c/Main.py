from itertools import combinations_with_replacement

def main():
    n, m, q = map(int, input().split())
    num_list = []
    for _ in range(q):
        num_list.append(list(map(int,input().split())))

    max_num = 0

    l = [ i for i in range(1,m+1)]
    c_list = list(combinations_with_replacement(l, n))

    for c in reversed(c_list):
        tmp_count = 0
        for i in range(q):
            aa = num_list[i][0]
            bb = num_list[i][1]
            cc = num_list[i][2]
            dd = num_list[i][3]
            if c[bb-1] - c[aa-1] == cc:
                tmp_count += dd

        max_num = max(max_num, tmp_count)

    print(max_num)

if __name__ == '__main__':
    main()