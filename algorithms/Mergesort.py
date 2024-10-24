# T(n) = O(nlogn) S(n) = O(n)
arr = [9,8,7,6,5,4,3,2,1]


def mergeSort(arr,left,right):
    
    if left >= right:
        return
    
    mid = left + (right - left)//2
    # divide phase - O(logn)
    mergeSort(arr,left,mid)
    mergeSort(arr,mid+1,right)
    # merge phase - O(n)
    merge(arr,left,mid,right) 
    
def merge(arr, left, mid, right):
    
    # +1 since left contains mid 
    n1 = mid-left+1 
    n2 = right - mid
    
    leftArr = [0] * n1
    rightArr = [0] * n2
    
    for i in range(n1):
        leftArr[i] = arr[left+i]
   
    for i in range(n2):
        # since right array has elements from mid+1
       rightArr[i] = arr[mid+i+1]
    
    i=0
    j=0
    
    while i<n1 and j<n2:
        if leftArr[i] < rightArr[i]:
            arr[left] = left[i]
            left+=1
            i+=1
        else:
            arr[left] = rightArr[j]
            left+=1
            j+=1
            
    while i<n1:
        arr[left] = leftArr[i]
        left+=1
        i+=1
        
    while j<n2:
        arr[left] = rightArr[j]
        left+=1
        j+=1
        
mergeSort(arr,0,len(arr)-1)
print(arr)
