def main():
    s = input()

    slist = ['Sunny','Cloudy','Rainy']

    index = slist.index(s) + 1

    if index == 3:
        index = 0

    print(slist[index])

if __name__ == '__main__':
    main()