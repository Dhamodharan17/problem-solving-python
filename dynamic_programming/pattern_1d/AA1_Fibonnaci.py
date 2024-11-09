# Recursion
class Solution(object):
    def fib(self, n):
        
        if n <= 1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)
# Top Down
class Solution(object):
    def fib(self, n):
         
        dp = [-1] * (n+1)

        return self.fib_memoize(n,dp)
        
    def fib_memoize(self,n, dp):

        if n <= 1 :
            return n
        
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.fib_memoize(n-1,dp) + self.fib_memoize(n-2,dp)

        return dp[n]
      
# Bottom Up
class Solution(object):
    def fib(self, n):

        if n == 0:
            return 0
            
        dp = [-1] * (n+1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
# Space Optimised
class Solution(object):
    def fib(self, n):

        if n == 0:
            return 0

        prev2 = 0
        prev1 = 1
    
        for i in range(2, n+1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        
        return prev1
        
