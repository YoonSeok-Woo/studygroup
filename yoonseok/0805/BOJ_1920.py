N = int(input())
nums = list(map(int,input().split()))
nums.sort()
_ = int(input())
TC = list(map(int,input().split()))
for tc in TC:
    l = 0
    r = N-1
    check = False
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==tc:
            print(1)
            check = True
            break
        elif nums[mid]<tc:
            l = mid+1
        else :
            r = mid-1
    if not check :
        print(0)