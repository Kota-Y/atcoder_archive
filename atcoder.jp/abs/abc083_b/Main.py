def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)

def main():
    N, A, B = map(int, input().split())
    
    sum = 0

    for n in range(N+1):
        tmp = digitSum(n)
        if A <= tmp and tmp <= B:
            sum += n

    print(sum)

if __name__ == '__main__':
    main()