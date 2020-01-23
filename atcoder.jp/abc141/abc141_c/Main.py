import numpy as np

def main():
    n, k, q = map(int, input().split())
    
    ls = [q] * n

    rls = [k] * n

    maru_list = [0] * n

    ls = np.array(ls)
    rls = np.array(rls)
    maru_list = np.array(maru_list)

    for i in range(q):
        maru = int(input())
        maru_list[maru-1] += 1

    ls = ls - maru_list

    rls = rls - ls

    for i in range(n):
        print('Yes' if rls[i] > 0 else 'No')

if __name__ == '__main__':
    main()