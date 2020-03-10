from collections import deque

def main():
    s = input()
    q = int(input())

    is_true = True

    d = deque(s)

    for _ in range(q):
        input_list = list(input().split())
        if input_list[0] == '1':
            if is_true:
                is_true = False
            else:
                is_true = True
            continue
        if input_list[1] == '1':
            if is_true:
                d.appendleft(input_list[2])
            else:
                d.append(input_list[2])

        else:
            if is_true:
                d.append(input_list[2])
            else:
                d.appendleft(input_list[2])
            
    if not is_true:
        d.reverse()

    print(''.join(d))

if __name__ == '__main__':
    main()
