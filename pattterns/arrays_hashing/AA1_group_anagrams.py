#AP1 - Sorting + Hashing
class Solution(object):
    def groupAnagrams(self, strs):
        
        str_map = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in str_map:
                str_map[key].append(str)
            else:
                str_map[key] = [str]

        result =[]
        for list in str_map.values():
            result.append(list)
        
        return result

        
#AP2 - String Alg + Hashing
class Solution(object):

    def getSignature(self, s):
        #alphabet array with count for eaach
        count = [0] * 26
        #increase the count
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        #take each alphabets
        for i in range(26):
            #when available
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])
        #key - result = ['a', '3', 'b', '0'].
        return ''.join(result)

    def groupAnagrams(self, strs):
        
        str_map = {}
        for str in strs:
            key = self.getSignature(str)
            if key in str_map:
                str_map[key].append(str)
            else:
                str_map[key] = [str]

        result =[]
        for list in str_map.values():
            result.append(list)
        
        return result
        
