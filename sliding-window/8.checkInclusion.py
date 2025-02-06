class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ns1, ns2 = len(s1), len(s2)
        s1_counter = Counter(s1)

        left = right = 0
        s2_counter =  Counter()

        while right < ns2:
            s2_counter[s2[right]] += 1

            if s2_counter == s1_counter:
                return True

            #undo effect
            if right - left == ns1-1:
                s2_counter[s2[left]] -= 1
                if s2_counter[s2[left]] == 0:
                    del s2_counter[s2[left]]
                left += 1
            
            right += 1
        
        return False
        # for i in range(ns2-ns1+1):
        #     cur_string = s2[i:i+ns1]
        #     if s1_counter == Counter(cur_string):
        #         return True
        
        # return False
            
        
