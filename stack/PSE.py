nums = [1, 9, -7, 3, 2, 10, 0]
n = len(nums)

def brute_force():
    pge_map = {}
    for i in range(n-1, -1, -1):
        current = nums[i]
        for j in range(i-1, -1, -1):
            comp = nums[j]
            if comp > current:
                pge_map[current] = comp
                break
        if current not in pge_map:
            pge_map[current] = -1
    print(dict(sorted(pge_map.items())))

def prev_greater_element():
    #for index 0 -> it is easier to find previous greater element
    stack = []
    pge_map = {}
    for i in range(n):
        current = nums[i]

        #look for greater element
        while stack and stack[-1] < current:
            stack.pop()

        pge_map[current] = stack[-1] if stack else -1

        stack.append(current)

    print(dict(sorted(pge_map.items()))) 


print("previous greater element - brute force")
brute_force()
print("previous greater element - optimised")
prev_greater_element()
