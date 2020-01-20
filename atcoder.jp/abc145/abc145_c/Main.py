import itertools

def powpow(xl,yl):
    tmp = pow(xl[0]-yl[0], 2) + pow(xl[1]-yl[1], 2)
    dist = pow(tmp, 0.5)
    return dist


def main():
    n = int(input())
    num_list = [list(map(int, input().split())) for _ in range(n)]

    sum = 0

    ls = []
    for i in range(n):
        ls.append(i+1)

    p_list = list(itertools.permutations(ls, n))

    for i in range(len(p_list)):
        for j in range(n-1):
            xl = num_list[p_list[i][j] - 1]
            yl = num_list[p_list[i][j+1] - 1]
            sum += powpow(xl,yl)

    print(sum/len(p_list))

if __name__ == '__main__':
    main()