#Recursion
class Solution:
    def minimumEnergy(self, height, n):
        
        def minUtil(height, n):
            
            # Invalid path to reach n
            if n < 0 :
                return float('inf')
            
            # See each n as individual subproblem to be solved
            if n == 0:
                return 0 # No Energy requried to reach 0th step
            
            jump1 = abs(height[n] - height[n-1]) + minUtil(height,n-1)
          
            jump2 = float('inf')
            if n > 1:
               jump2 = abs(height[n] - height[n-2]) + minUtil(height,n-2)
          
            return min(jump1,jump2)
        
        return minUtil(height,n-1)   

#Top Down
class Solution:
    def minimumEnergy(self, height, n):
        
        dp = [-1] * n
        
        def minUtil(height, n):
            
            # Invalid path to reach n
            if n < 0 :
                return float('inf')
            
            # See each n as individual subproblem to be solved
            if n == 0:
                return 0 # No Energy requried to reach 0th step
            if dp[n] != -1:
                return dp[n]
                
            jump1 = abs(height[n] - height[n-1]) + minUtil(height,n-1)
          
            jump2 = float('inf')
            if n > 1:
               jump2 = abs(height[n] - height[n-2]) + minUtil(height,n-2)
          
            #Store min on each step in dp array for reuse
            dp[n] = min(jump1,jump2)
            
            return dp[n]
        
        return minUtil(height,n-1)

#Bottom Up
class Solution:
    def minimumEnergy(self, height, n):
        
        if n == 1:
            return 0
            
        dp = [-1] * n
        
        dp[0] = 0
        dp[1] = abs(height[0] - height[1])
        
        for i in range(2, n):
        # current single jump + jumps need to reach that single jump
            jump1 = abs(height[i] - height[i-1]) + dp[i-1]
            jump2 = abs(height[i] - height[i-2]) + dp[i-2]
            
            dp[i] = min(jump1,jump2)
        
        return dp[n-1]
# Space Optmization

class Solution:
    def minimumEnergy(self, height, n):
        
        if n == 1:
            return 0
        # min cost to reach 0   
        prev2 = 0
        # min cost to reach 1
        prev1 = abs(height[0] - height[1])
        
        for i in range(2, n):
        # current single jump + jumps need to reach that single jump
            jump1 = abs(height[i] - height[i-1]) + prev1
            jump2 = abs(height[i] - height[i-2]) + prev2
            
            cur = min(jump1,jump2)
            # mincost to reach at any step-> not gonna change
            prev2 = prev1  
            prev1 = cur
        
        return prev1
