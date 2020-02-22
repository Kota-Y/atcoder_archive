import itertools

def main():
    n = int(input())
    s = input()

    ans = 0
    output_list = []

    for i in range(1000):
        if len(str(i)) == 1:
            a = 0
            b = 0
            c = i
        elif len(str(i)) == 2:
            a = 0
            b = i // 10
            c = i - b * 10
        else:
            a = i // 100
            b = (i - a * 100) // 10
            c = i - a * 100 - b * 10
        tmp = str(a) + str(b) + str(c)
        output_list.append(tmp)
    
    for i in range(1000):
        a = output_list[i][0]
        b = output_list[i][1]
        c = output_list[i][2]
        first_flag = False
        second_flag = False
        for j in range(n):
            if not first_flag and s[j] == a:
                first_flag = True
                continue
            if first_flag and not second_flag and s[j] == b:
                second_flag = True
                continue
            if first_flag and second_flag and s[j] == c:
                ans += 1
                break

    print(ans)

if __name__ == '__main__':
    main()