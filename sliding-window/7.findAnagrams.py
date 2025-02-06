class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ns = len(s)
        np = len(p)
        p_counter = Counter(p)
        result = []
        
        #generate all string of size p
        #check characters are equal

        for i in range(ns-np+1):
            cur_counter = Counter(s[i:i+np])
            if cur_counter == p_counter:
                result.append(i)
        
        return result





        
