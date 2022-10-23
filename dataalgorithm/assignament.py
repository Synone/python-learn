'''
def count_rotations(nums):
    try:
        smallest_num = None
        for i in nums:
            if smallest_num == None or i < smallest_num:
                smallest_num = i
        position = nums.index(smallest_num)
        rotations = len(nums[None:position])
        return rotations
    except ValueError as a:
        print(a)
    return 0
test = {
    'input': {
        'num': []
    },
    'output': 0
}

nums = test['input']['num']
count_rotations(nums)
# solution 2
output = test['output']
result = count_rotations(nums)
print(result)
def count_rotations_linear(nums):
    position = 0              
    while position <= len(nums):                     
        if position > 0 and nums[position] < nums[position -1]:   # How to perform the check?
            return position
        
        position += 1
    return 0  
'''
##### BINARY SEARCH METHOD
def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    while lo<=hi:
        mid = (lo+hi)//2
        print(mid)
        mid_number = nums[mid]
    
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        if mid > 0 and  mid_number < nums[mid-1]:
            return mid
        elif mid_number < nums[hi]:
            hi = mid - 1 
        else:
            lo = mid + 1
    return 0


list = [8,9,10,5,6,7]
count_rotations_binary(list)
