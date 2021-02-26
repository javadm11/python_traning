def buy_sell (sequence):
    min=0
    max=0
    dif=0
    for (i,v) in enumerate(sequence):

        for (j,vv) in enumerate(sequence[i:]):
            
            if vv-v > dif:
                dif=vv-v
                min=i
                max=j+i

    return (min,max)

list=[2,6,0,4,12,1]
a=buy_sell(list)
print(a)
            