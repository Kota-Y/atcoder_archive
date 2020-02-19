def main():
    num_list = []
    for _ in range(3):
        num_list.append(list(map(int,input().split())))

    a1 = 0
    b1 = num_list[0][0] - a1
    b2 = num_list[0][1] - a1
    b3 = num_list[0][2] - a1
    a2 = num_list[1][0] - b1
    a3 = num_list[2][0] - b1

    isGood = True

    if a1 + b1 != num_list[0][0]:
        isGood = False
    if a1 + b2 != num_list[0][1]:
        isGood = False
    if a1 + b3 != num_list[0][2]:
        isGood = False
    if a2 + b1 != num_list[1][0]:
        isGood = False
    if a2 + b2 != num_list[1][1]:
        isGood = False
    if a2 + b3 != num_list[1][2]:
        isGood = False
    if a3 + b1 != num_list[2][0]:
        isGood = False
    if a3 + b2 != num_list[2][1]:
        isGood = False
    if a3 + b3 != num_list[2][2]:
        isGood = False

    print('Yes' if isGood else 'No')

if __name__ == '__main__':
    main()