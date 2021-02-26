def move_zero(sequence):
    index=0
    zero_num=0
    cp=[]
    while index < len(sequence):
        if sequence[index]==0:
            zero_num+=1
        else:
            cp.append(sequence[index])
        index+=1
    for _ in range(zero_num):
        cp.append(0)
    return cp
        

list=[0,6,5,0,5,4,2,0,43,23,0,0,4,0,3,0]

a=move_zero(list)
print(a)
