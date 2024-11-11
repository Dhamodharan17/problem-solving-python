# Topdown
class Solution:
    def maximumPoints(self, arr, n):

        dp = [[-1 for j in range(4)] for i in range(n)]

        def util(current_day, prev_task):
            if dp[current_day][prev_task] != -1:
                return dp[current_day][prev_task]
            
            if current_day == 0:
                # Base case: Choose the max score for tasks other than prev_task
                max_value = 0
                for current_task in range(3):
                    if current_task != prev_task:
                        dp[current_day][prev_task] = max(max_value, arr[current_day][current_task])
                dp[current_day][prev_task] = max_value
                return max_value

            # Recursive case: Compute max profit for current day
            max_profit = 0
            for current_task in range(3):
                if current_task != prev_task:
                    # current + remaining
                    local_profit = arr[current_day][current_task] + util(current_day - 1, current_task)
                    max_profit = max(max_profit, local_profit)
            
            dp[current_day][prev_task] = max_profit
            return dp[current_day][prev_task]

        return util(n-1, 3)

#Bottom Up
class Solution:
    def maximumPoints(self, arr, n):
        
        dp = [[0 for j in range(4)] for i in range(n)]
        
        # Base case = independet problesm
        dp[0][0] = max(arr[0][1], arr[0][2])
        dp[0][1] = max(arr[0][0], arr[0][2])
        dp[0][2] = max(arr[0][0], arr[0][1])
        dp[0][3] = max(arr[0][0], max(arr[0][1], arr[0][2]))
        
        # each cell, we need to max value, so try all possible combos
        for current_day in range(1,n):
            for last_task in range(4):
                max_profit = 0
                for current_task in range(3):
                    if current_task != last_task:
                        local_max = arr[current_day][current_task] + dp[current_day-1][current_task]
                        max_profit = max(max_profit, local_max)
                dp[current_day][last_task] =  max_profit
        
        return dp[n-1][3]
  #Space opt
  class Solution:
    def maximumPoints(self, arr, n):
        
        prev = [0] * 4
        
        # Base case = independet problesm
        prev[0] = max(arr[0][1], arr[0][2])
        prev[1] = max(arr[0][0], arr[0][2])
        prev[2] = max(arr[0][0], arr[0][1])
        prev[3] = max(arr[0][0], max(arr[0][1], arr[0][2]))
        
        # each cell, we need to max value, so try all possible combos
        for current_day in range(1,n):
            temp = [0] * 4
            for last_task in range(4):
                for current_task in range(3):
                    if current_task != last_task:
                        local_max = arr[current_day][current_task] + prev[current_task]
                        temp[last_task] = max(temp[last_task], local_max)
            prev = temp

        return prev[3]
