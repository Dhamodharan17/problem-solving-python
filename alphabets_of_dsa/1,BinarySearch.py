#iterative
def binary_search_iterative(nums, target):
    
    start, end = 0, len(nums)-1
    
    # start == end -> when we have only one element -> it can be target
    while start <= end :
        
        mid = (start + end ) // 2
        
        if nums[mid] ==  target:
            return mid
        
        # mid greater -> need less -> move left
        if nums[mid] > target:
            end = mid - 1
        
        # mid lesser -> need greater -> move right
        elif nums[mid] < target:
            start = mid + 1
    

nums = [6, 7, 8, 9, 10, 11, 12, 13]

ans = binary_search_iterative(nums, 12)

print(ans)

#recursion

def binary_search_recursive(nums, target):
    
    def binary_search(start, end):
        
        if start > end:
            return -1
        
        mid = (start + end) // 2
        
        if nums[mid] == target:
            return mid
    
        # mid is greater -> i need go left
        if nums[mid] > target:
            return binary_search(start, mid-1)
            
        if nums[mid] < target:
            return binary_search(mid+1, end)
    
    return binary_search(0, len(nums)-1)

nums = [6, 7, 8, 9, 10, 11, 12, 13]

ans = binary_search_recursive(nums, 13)

print(ans)

