# Given an array of integers and a target value, determine the number of pairs of array elements that have a
# difference equal to the target value.
def pairs(k, arr):
 # Write your code here
    count = 0
    arr.sort()
    set1 = {}
    for i in range(len(arr)):
        if arr[i]-k in set1:
            count+=1
        set1[arr[i]]=arr[i]-k
    return count