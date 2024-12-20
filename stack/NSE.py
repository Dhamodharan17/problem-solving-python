nums = [1, 9, -7, 3, 2, 10, 0]
n = len(nums)

# next smaller element for each element
# search smaller element 

def next_smaller_element():
    # for last index -> it is easy to find the next smaller since there is nothing on right

    nse_map = {}
    stack = []

    for i  in range(n-1, -1, -1):
        current = nums[i]

        # search smaller element -> if greater remove it
        # current becomes smaller for remainig
        while stack and stack[-1] >= current:
            stack.pop()

        nse_map[current] = stack[-1] if stack else -1

        stack.append(current)
    
    print(nse_map)

next_smaller_element()
