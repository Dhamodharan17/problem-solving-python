class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n1 = len(text1) - 1
        n2 = len(text2) - 1
        
        def util(i, j):

            if i < 0 or j < 0:
                return 0
              
            #when char matches
            if text1[i] == text2[j]:
                return 1 + util(i-1, j-1)
            else:
              #when char doesn't match - any side can make result
                return 0 + max(util(i, j-1) , util(i-1, j))
            
        return util(n1, n2)
