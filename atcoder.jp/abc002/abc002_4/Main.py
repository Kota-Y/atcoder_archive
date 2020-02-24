from itertools import product
from itertools import combinations

def main():
    n, m = map(int, input().split())
    num_list = []
    for _ in range(m):
        num_list.append(list(map(int,input().split())))

    ans = 1

    if n == 1:
        print(ans)
        exit()

    for bit in list(product([0, 1], repeat = n)):
        count = bit.count(1)
        if count == 0 or count == 1:
            continue
        member = []
        for i in range(n):
            if bit[i] == 1:
                member.append(i+1)
        flag = True
        for x, y in list(combinations(member, 2)):
            for j in range(m):
                if num_list[j][0] == x and num_list[j][1] == y:
                    break
            else:
                flag = False
        if flag:
            ans = max(ans, count)

    print(ans)

if __name__ == '__main__':
    main()