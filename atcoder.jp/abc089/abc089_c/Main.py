from collections import Counter # 重複個数のカウント: Counter(num_list)
import itertools

def main():
    n = int(input())
    str_list = [input()[0] for _ in range(n)]

    str_count = Counter(str_list)

    ans = 0

    seq = ['M', 'A', 'R', 'C', 'H']

    for l in list(itertools.combinations(seq,3)):
        ans += str_count[l[0]] * str_count[l[1]] * str_count[l[2]]

    print(ans)

if __name__ == '__main__':
    main()