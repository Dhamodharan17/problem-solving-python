nums = [1, 9, -7, 3, 2, 10, 0]
n = len(nums)

#for each number, find its previous smaller number
#for index 0 ,it is easy to find previous since nothing

def previous_smaller_element():

    stack = []
    pse_map = {}
    for i in range(n):
        current = nums[i]

        #look for smaller -> remove greater
        while stack and stack[-1] >= current:
            stack.pop()
        
        pse_map[current] = stack[-1] if stack else -1

        stack.append(current)
    
    print(pse_map)
        
previous_smaller_element()
