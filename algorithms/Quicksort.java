
arr = [9,8,7,6,5,4,3,2,1]

# smaller element should go left of boundry (case 1)
# greater element on right of boundry
def partition(arr, left, right):
    
    pivot = arr[right]
    #place we put the pivot element
    boundry = left
    
    for i in range(left,right):
        if arr[left] < pivot:#case 1 - push smaller element to left
            arr[left], arr[boundry] = arr[boundry], arr[left]
            boundry+=1
            
    #place pivot in correct place
    arr[right], arr[boundry] = arr[boundry], arr[right]
    
    return boundry# correct index for pivot 
    


def quickSort(arr,left,right):
    
    if left>=right:
        return

    pivot = partition(arr, left, right);
    quickSort(arr,left,pivot-1)
    quickSort(arr,pivot+1,right)


quickSort(arr, 0, len(arr)-1)
print(arr)
