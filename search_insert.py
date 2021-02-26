
def searchInsert(nums,target):
    start = 0
    end=len(nums)
    mid = len(nums)//2 -1
    while start<= end:
        if target>mid:
            mid +=1
            start=mid
        else:
            mid-=1
            end=mid
    return start

    



print(searchInsert([1,2,3,4,5],98))