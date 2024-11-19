class Solution(object):
    def coinChange(self, coins, amount):
        
        n = len(coins)

        prev = [float('inf') for _ in range(amount+1)]

        # no coins can only make amount 0
        prev[0] = 0

        for i in range(1, n+1):
            current = [float('inf') for _ in range(amount+1)]
            for cur_sum in range(amount+1):
                
                pick = float('inf')
                if coins[i-1] <= cur_sum:
                    pick = 1 + current[cur_sum - coins[i-1]]
                skip = prev[cur_sum]
                
                current[cur_sum] = min(pick, skip)
            prev = current
        
        ans = prev[amount]

        return ans if ans != float('inf') else -1
                
       
