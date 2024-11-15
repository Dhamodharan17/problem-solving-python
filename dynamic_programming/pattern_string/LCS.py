# recursion
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

