# top down
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        def util(idx1, idx2):

            if idx1 < 0 or idx2 < 0:
                return 0
            # trying all possible ways to match string
            if text1[idx1] == text2[idx2]:
                return 1 + util(idx1-1,idx2-1)
            else:
                return max(util(idx1-1,idx2), util(idx1,idx2-1))
        
        return util(n1-1,n2-1)
        
#bottom up - building iteratively
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        #LCS of ""/"" = 0 since there is no character
        # Lcs with empty string
        for i in range(n1+1):
            dp[i][0] = 0
        for i in range(n2+1):
            dp[0][i] = 0
        
        for ind1 in range(1,n1+1):
            for ind2 in range(1,n2+1):
                if text1[ind1-1] == text2[ind2-1]:
                    #dp[ind1-1][ind2-1] - both string reduced by 1
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        
        return dp[n1][n2]

#space
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        n1 = len(text1)
        n2 = len(text2)

        prev = [0 for _ in range(n2+1)] 
        current = [0 for _ in range(n2+1)] 

        # Lcs with empty string
        prev[0] = 0
        current[0] = 0
        
        for ind1 in range(1,n1+1):
            for ind2 in range(1,n2+1):
                if text1[ind1-1] == text2[ind2-1]:
                    #dp[ind1-1][ind2-1] - both string reduced by 1
                    current[ind2] = 1 + prev[ind2-1]
                else:
                    current[ind2] = max(prev[ind2],current[ind2-1])
            prev = current[:]
        
        return prev[n2]

       

        
       

        

