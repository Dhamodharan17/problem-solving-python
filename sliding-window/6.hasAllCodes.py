class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        n = len(s)
        string_set = set()
      #generate all strings of length k
        for i in range(n-k+1):
            current_string = s[i:i+k]
            string_set.add(current_string)
        
        return len(string_set) == pow(2,k)

#optimised rolling hash


        
