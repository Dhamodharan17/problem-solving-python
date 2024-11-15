#top down
def minimumDifference( nums):
       
       total_sum = sum(nums)
       n = len(nums)

       dp = [[False for _ in range(total_sum+1)] for _ in range(n)]

       #all sets can form 0
       for i in range(n):
         dp[i][0] = True
    
       if nums[0] <= total_sum:
         dp[0][nums[0]] = True

       for idx in range(1,n):
        for cur_sum in range(1,total_sum+1):
            include = False
            if nums[idx] <= cur_sum:
                include = dp[idx-1][cur_sum-nums[idx]]
            exclude = dp[idx-1][cur_sum]

            dp[idx][cur_sum] = include or exclude

       mini = float('inf') 
       for cur_sum in range(total_sum+1):
        if dp[n-1][cur_sum] == True:
            s1 = total_sum - cur_sum
            s2 = cur_sum
            mini = min(mini, abs(s1 - s2))

       return mini

arr = [1, 2, 7]
print("The minimum absolute difference is:", minimumDifference(arr))

# space
def minimumDifference( nums):
       
       total_sum = sum(nums)
       n = len(nums)

       prev = [False for _ in range(total_sum+1)]

       prev[0] = True
    
       if nums[0] <= total_sum:
         prev[nums[0]] = True

       for idx in range(1,n):
        current = [False for _ in range(total_sum+1)]
        current[0] = True
        for cur_sum in range(1,total_sum+1):
            include = False
            if nums[idx] <= cur_sum:
                include = prev[cur_sum-nums[idx]]
            exclude = prev[cur_sum]

            current[cur_sum] = include or exclude
        prev = current

       mini = float('inf') 
       for cur_sum in range(total_sum+1):
        if current[cur_sum] == True:
            s1 = total_sum - cur_sum
            s2 = cur_sum
            mini = min(mini, abs(s1 - s2))

       return mini

arr = [1, 2, 7]
print("The minimum absolute difference is:", minimumDifference(arr))
