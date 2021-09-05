def i_map(): return map(int, input().split())

def main():
    a, b = i_map()
    
    if 112.5<=a<=337.5:
            x="NNE"
    elif 337.5<=a<562.5:
        x="NE"
    elif 562.5<=a<=787.5:
        x="ENE"
    elif 787.5<=a<=1012.5:
        x="E"
    elif 1012.5<=a<=1237.5:
        x="ESE"
    elif 1237.5<=a<=1462.5:
        x="SE"
    elif 1462.5<=a<=1687.5:
        x="SSE"
    elif 1687.5<=a<=1912.5:
        x="S"
    elif 1912.5<=a<=2137.5:
        x="SSW"
    elif 2137.5<=a<=2362.5:
        x="SW"
    elif 2362.5<=a<=2587.5:
        x="WSW"
    elif 2587.5<=a<=2812.5:
        x="W"
    elif 2812.5<=a<=3037.5:
        x="WNW"
    elif 3037.5<=a<=3262.5:
        x="NW"
    elif 3262.5<=a<=3487.5:
        x="NNW"
    else:
        x="N"

    b=round(b/60+10**(-5),1)

    if b<=0.2:
        y=0
    elif b<=1.5:
        y=1
    elif b<=3.3:
        y=2
    elif b<=5.4:
        y=3
    elif b<=7.9:
        y=4
    elif b<=10.7:
        y=5
    elif b<=13.8:
        y=6
    elif b<=17.1:
        y=7
    elif b<=20.7:
        y=8
    elif b<=24.4:
        y=9
    elif b<=28.4:
        y=10
    elif b<=32.6:
        y=11
    else:
        y=12
    if y==0:
        x="C"
    print(x,y)

if __name__ == '__main__':
    main()
