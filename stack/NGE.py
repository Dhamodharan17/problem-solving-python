nums = [1, 9, -7, 3, 2, 10, 0]
n = len(nums)

#next greater element -> for every element greater element on right

def brute_force():

    nge_map = {}
    for i in range(n):
        current = nums[i]
        #compare with other elements
        for j in range(i+1, n):
            temp = nums[j]
            #find 1st greater
            if temp > current:
                nge_map[current] = temp
                break
        if current not in nge_map:
            nge_map[current] = -1
            
    print(dict(sorted(nge_map.items())))

def stack_app():
    # if we start from start -> we have to search full to get the max
    stack = []
    # we don't put larger elements on top of smaller elements
    # decreasing stack
    nge_map = {}
    for i in range(n-1, -1, -1):
        current = nums[i]

        # remove until we get greater
        while stack and stack[-1] < current:
            stack.pop()
        
        nge_map[current] = stack[-1] if stack else -1
        
        stack.append(current)
    
    print(dict(sorted(nge_map.items())))


print("brute force")
brute_force()
print("monotonic stack")
stack_app()

        


    

