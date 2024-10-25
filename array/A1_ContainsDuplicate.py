class Solution(object):

    #AP1 - Nested Loop T(n) = O(n^2)  S(n) = O(1)    
    def containsDuplicateNestedLoop(self, nums):
        inputLen = len(nums)
        for currentIndex in range(inputLen):
            for nextIndex in range(currentIndex+1,inputLen):
                if nums[currentIndex] == nums[nextIndex]:
                    return True

        return False

    ##AP2 - Sort and 2 Pointer T(n) = O(nlogn) S(n) = O(n)
    def containsDuplicateSorted(self,nums):
        inputLen = len(nums)
        nums.sort()

        for currentIndex in range(inputLen-1):
            if nums[currentIndex] == nums[currentIndex+1]:
                return True
        return False
    
    ##AP3 - Set T(n) = O(n) S(n) = O(1){based on hash function}
    def containsDuplicateSet(self,nums):

       numberSet = set()
       for currentElement in nums:
            if currentElement in numberSet:
                return True
            else:
                numberSet.add(currentElement)

       return False

    def containsDuplicateBits(self,nums):

        nChecker = 0
        pChecker = 0
        for currentElement in nums:
            # check ith bit already set
            if currentElement>=0:
                ##Since 1<<Current make all 0's Except ith bit
                ## if pChecker have the same element then only 1 will come
                if (pChecker & 1<<currentElement )> 0:
                    return True
                ## Set the ith bit
                pChecker |= (1<<currentElement)
            else:
                currentElement = abs(currentElement)
                if (nChecker & 1<<currentElement) > 0:
                    return True
                nChecker |= (1<<currentElement)

        return False

    ## Main Method    
    def containsDuplicate(self, nums):
        #return self.containsDuplicateNestedLoop(nums) - TLE
        #return self.containsDuplicateSorted(nums)
        #return self.containsDuplicateSet(nums)
        return self.containsDuplicateBits(nums)
       
    
        
        
        
