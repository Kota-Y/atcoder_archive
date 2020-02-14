def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    total = H * W - h * W - (H-h) * w

    print(total)

if __name__ == '__main__':
    main()