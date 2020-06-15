def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row_list(N): return [i_list() for _ in range(N)]

def main():
    n = i_input()
    num_list = i_row_list(n)

    max_num = 0
    for i in range(n-1):
        for j in range(i+1,n):
            tmp_ix = num_list[i][0]
            tmp_iy = num_list[i][1]
            tmp_jx = num_list[j][0]
            tmp_jy = num_list[j][1]
            tmp_num = pow(pow(tmp_ix-tmp_jx,2)+pow(tmp_iy-tmp_jy,2),0.5)
            max_num = max(max_num, tmp_num)

    print(max_num)

if __name__ == '__main__':
    main()
