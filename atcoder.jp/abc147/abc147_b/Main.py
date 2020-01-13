def main():
    S = input()

    result = 0

    lenS = len(S)

    for i in range(lenS//2):
        if S[i] != S[lenS-1-i]:
            result += 1

    print(result)

if __name__ == '__main__':
    main()