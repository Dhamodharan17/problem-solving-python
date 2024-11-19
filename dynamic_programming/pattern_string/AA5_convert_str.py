class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        lcs = dp[n][m]

        deletes = n - lcs
        inserts = m - lcs
        return deletes + inserts

        
