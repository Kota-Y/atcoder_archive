def main():
    a, b, t = map(int, input().split())

    ans = 0

    time = 0
    while(t+0.5 > time):
        time += 1
        if time % a == 0 and time < t+0.5:
            ans += b

    print(ans)

if __name__ == '__main__':
    main()