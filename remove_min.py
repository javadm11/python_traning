def remove_min(sequence):
    min=sequence[0]
    index=0
    for (i,v) in enumerate(sequence[1:],start=1):
        if v<min:
            min=v 
            index=i
    sequence.pop(index)
    return sequence


list=[1,7,4,7,9,43,23,6,43,43,7,4,6,8,0,432,-1,1]
a=remove_min(list)
print(a)