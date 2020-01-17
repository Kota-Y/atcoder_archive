import itertools

def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    q_list = list(map(int, input().split()))

    l = []
    for i in range(1,n+1):
        l.append(i)

    l = list(itertools.permutations(l, n))

    p_tu = tuple(p_list)
    q_tu = tuple(q_list)

    p_count = l.index(p_tu)

    q_count = l.index(q_tu)

    print(abs(p_count-q_count))

if __name__ == '__main__':
    main()