#recursion
class Solution:
    #biggger problem - does sum exist in subset
    def isSubsetSum (self, arr, target):
        
        n = len(arr)
        
        def util(current_index, current_target):
            
            if current_target < 0:
                return False
            #smaller problem - does sum 0 exist in empty subset
            #which means first element == some sum
            if current_target == 0:
                return True
            
            if current_index == 0:
                return arr[current_index] == current_target
                
            #include
            pick = util(current_index-1, current_target-arr[current_index])
            #exclude
            skip = util(current_index-1, current_target)
            
            return pick or skip
        
        #who can give indepent result i.e 0
        return util(n-1,target)

#bottom up
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)

        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        
        for i  in range(n):
            dp[i][0] = True # all sets can make sum 0 by empty subset
            
        if target >= arr[0]:
            dp[0][arr[0]] = True #subset of size 1

        for i in range(1, n):# since we already considered element at 0
            for current_sum in range(1, target + 1):
                include = False
               
                if arr[i] <= current_sum:
                    include = dp[i-1][current_sum - arr[i]]

                exclude = dp[i-1][current_sum]

                dp[i][current_sum] = include or exclude

        return dp[n-1][target]
#space
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)

        prev = [False for _ in range(target + 1)]
        # all elements can form sum 0 by empty set
        prev[0] = True
        if arr[0] <= target:
            prev[arr[0]] = True  #base case

        for i in range(1, n):# since we already considered element at 0
            current = [False for _ in range(target + 1)]
            # all elements can form sum 0 by not including them
            current[0] = True
            for current_sum in range(1, target + 1):
                include = False
               
                if arr[i] <= current_sum:
                    include = prev[current_sum - arr[i]]

                exclude = prev[current_sum]

                current[current_sum] = include or exclude
                
            prev = current
        
        return prev[target]
