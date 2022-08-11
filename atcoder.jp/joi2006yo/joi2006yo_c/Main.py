def i_input(): return int(input())
def s_input(): return input()

def main():
    n = i_input()

    top = 1
    front = 2
    right = 3

    ans_sum = 1
    for _ in range(n):
        s = s_input()
        if s == 'East':
            top, front, right = 7 - right, front, top
        elif s == 'Left':
            top, front, right = top, 7 - right, front
        elif s == 'North':
            top, front, right = front, 7 - top, right
        elif s == 'Right':
            top, front, right = top, right, 7 - front
        elif s == 'South':
            top, front, right = 7 - front, top, right
        elif s == 'West':
            top, front, right = right, front, 7 - top
        ans_sum += top

    print(ans_sum)

if __name__ == '__main__':
    main()
