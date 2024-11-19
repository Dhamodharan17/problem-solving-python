class Solution(object):
    def change(self, amount, coins):
       
        def util(i, amount):
        
            if amount == 0:
                return 1
            
            if i < 0:
                return 0

            pick = 0
            if coins[i-1] <= amount:
                pick = util(i, amount-coins[i-1])

            skip = util(i-1, amount)

            return pick + skip

        return util(len(coins)-1, amount)
