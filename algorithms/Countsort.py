input = [9,8,7,6,5,4,3,2,1]

max = max(input)

countArr = [0] * (max+1)

#countArr
for i in input:
    countArr[i]+=1
  
#count Sum
for i in range(1,len(countArr)):
    countArr[i] += countArr[i-1]

outArr = [0]*len(input)

#start from back
for i in range(len(input)-1,-1,-1):
    #take element
    current_element = input[i]
    #take index from countArr
    countArr[current_element]-=1 #since 0 based indexing
    new_position = countArr[current_element]
    #place in output array
    outArr[new_position] = current_element

print(outArr)
