def bead_sort(sequence):
    if any(not isinstance(x,int) or x<0  for x in sequence):
        raise  TypeError('sequence must be list of non-negative integers')

    for _ in range(len(sequence)):
        for i,(rod_upper,rod_lower) in enumerate(zip(sequence,sequence[1:])):
            if rod_upper > rod_lower :
                sequence[i] -= rod_upper - rod_lower
                sequence[i+1] += rod_upper - rod_lower

    return sequence


def bead_sortt(sequence):
    if any(not isinstance(x,int) or x<0 for x in sequence):
        raise  TypeError('dfsdfjakhgfagahagl')
    for _ in range(len(sequence)):
        for i,(rod_upper,rod_lower) in enumerate(zip(sequence,sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper-rod_lower
                sequence[i+1] += rod_upper-rod_lower

    return sequence
                


list=[3,1,6,9,2,4,10,15,12]

a=bead_sortt(list)
print(a)