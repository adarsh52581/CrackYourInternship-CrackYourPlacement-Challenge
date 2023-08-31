def maxSubarray(arr):
    # Write your code here
    pos_numbers=[num for num in arr if num>=0]
    neg_numbers=[num for num in arr if num<0]
    if not pos_numbers:
        subsequence_sum=max(neg_numbers)
    else:
        subsequence_sum=sum(pos_numbers)
    subarray_sum=float('-inf')
    temp=0
    for num in arr:
        temp+=num
        if temp>subarray_sum:
            subarray_sum=temp
        if temp<0:
            temp=0
    return (subarray_sum,subsequence_sum)
# this is the optimal code wiht just O(n) time complexity, my first solution was brute force to use two for loops,
# but instead it can done with a single iteration, as replacing the temp value with 0 whenever its value became below 0
# meaning preventing the use of a second for to iterate through the subsets in the array