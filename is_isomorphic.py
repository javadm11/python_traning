
# whole thing is wrong i got worng undrestanding of what isomorphic is!
#so this program don't have any relation to isomorphic

def isomorphic_check(value):
    size=len(value) 
    half=size//2
    half-=1
    state=1
    if size % 2 ==1:
        state=2
        
    check=True
    end=half+state
    start=half
    print
    while(start>-1):
        print(value[end],value[start])
        if value[start] != value[end]:
            
            check=False
        end+=1
        start-=1

    return check

a=isomorphic_check('asfdfsa')
print(a)