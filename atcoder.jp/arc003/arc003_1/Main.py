def i_input(): return int(input())
def s_input(): return input()

def main():
    n = i_input()
    s = s_input()

    s = s.replace('A','4')
    s = s.replace('B','3')
    s = s.replace('C','2')
    s = s.replace('D','1')
    s = s.replace('F','0')

    sum_ans = 0
    for tmp_s in s:
        sum_ans += int(tmp_s)

    print(sum_ans/n)

if __name__ == '__main__':
    main()
