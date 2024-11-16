#notes
# divide on mid
# left (size = m - l+1 ) and right array (size = r - mid)
# offset - left [ l+ i ] right[ mid+1+j]
# 2 pointer
class Solution:
 
    def mergeSort(self,arr, l, r):
        
        # when there is only on element - no need to split
        if l >= r :
            return
        
        # to divide
        mid = l + (r-l)//2
        
        # divide into 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid+1, r)
        # merge at all
        self.merge(arr, l, mid, r)
    
    def merge(self, arr, l, mid, r):
        
        n1 = mid - l + 1 # array size 1 [since 0 index based]
        n2 = r - mid  # array size 2 
        
        left = [0] * n1
        right = [0] * n2
        
        for i in range(n1):
            left[i] = arr[i+l] # since element start from l
        
        for i in range(n2):
            right[i] = arr[i+mid+1] # since mid came 
        
        i, j = 0, 0
        
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[l] = left[i]
                i+=1
            else:
                arr[l] = right[j]
                j+=1
            l+=1

        
        while i < n1:
            arr[l] = left[i]
            i+=1
            l+=1
            
        while j < n2:
            arr[l] = right[j]
            j+=1
            l+=1
            
