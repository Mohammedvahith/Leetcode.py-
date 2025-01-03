nums = [1,2,2]
# nums = [1,1,2]
# output = [0,1,2,3]
count = 1
l = len(nums)
for i in range(1,l):
    if nums[i-1] != nums[i]:
        nums[count]=nums[i]
        count+=1
print(count)
