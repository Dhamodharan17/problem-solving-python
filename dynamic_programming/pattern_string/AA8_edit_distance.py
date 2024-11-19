class Solution(object):
    def minDistance(self, word1, word2):
        
        n1 = len(word1)
        n2 = len(word2)

        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = i # to convert "" to i string
        
        for j in range(n2+1):
            dp[0][j] = j
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delete1 = dp[i][j-1]
                    delete2 = dp[i-1][j]
                    insert = dp[i-1][j-1]#same for replace
                    dp[i][j] = 1 + min(insert, min(delete1, delete2))
        
        return dp[n1][n2]
