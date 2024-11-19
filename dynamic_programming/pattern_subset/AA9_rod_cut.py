class Solution:
    def cutRod(self, price, n):
        
        def util(price, i, n):
           
           if i == 0:
               return n*price[0]
             
           not_cut = util(price, i-1, n)
           
           cut = float('-inf')
           
           # after each cut, len increases
           rod_len = i + 1
           if rod_len <= n:# we cannot cut more then n
               cut = price[i] + util( price, i, n-rod_len)
           
           return max(cut, not_cut)
         
        return util(price, n-1, n)
