import numpy as np

def main():
    n = int(input())
    value_list = list(map(int, input().split()))
    cost_list = list(map(int, input().split()))

    ans = 0

    value_list = np.array(value_list)
    cost_list = np.array(cost_list)

    value_list -= cost_list

    for i in range(n):
        if value_list[i] > 0:
            ans += value_list[i]

    print(ans)

if __name__ == '__main__':
    main()