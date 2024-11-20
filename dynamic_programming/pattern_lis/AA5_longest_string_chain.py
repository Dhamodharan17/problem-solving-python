class Solution(object):
    def longestStrChain(self, words):

        def isCompare(s1,s2):
            if len(s1) != len(s2)+1:
                return False

            i, j = 0, 0
            while i < len(s1):
                if j < len(s2) and s1[i] == s2[j]:
                    j+=1
                i+=1
            # we checked string sizes
            # if we more we don't have enough match chars
            # j will not increase
            return j == len(s2)
            
          

        n = len(words)
        words.sort(key = len)# sort based on length
        dp = [1] * n
        maxi = 1

        for cur in range(n):
            for prev in range(cur):

                if isCompare(words[cur], words[prev]):
                    if dp[cur] < dp[prev] + 1:
                        dp[cur] = dp[prev] + 1
                        maxi = max(maxi, dp[cur])
    
        return maxi

        

        
    
