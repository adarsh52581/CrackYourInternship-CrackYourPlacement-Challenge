# My code
# def cookies(k, A):
#     # Write your code here
#     result = 0
#     while True:
#         A.sort()
#         if len(A)==1 and A[0]<k:
#             return -1
#         elif A[0]>=k:
#             return result
#         else:
#             ele=A[0]+2*A[1]
#             A=A[2:]
#             A.append(ele)
#             result+=1

# 1. So this is the code that I came up with, with a small mistake in the slicing statement in 12th license
# 2. The mistake was to use 0-based indexing while splicing and I used 1-based indexing
# 3. But this is time inefficient, the best method would be to use heap--I didnt know heap well enough to understand when to use it.

# Optimized Code:
import heapq
def cookies(k, A):
    # Write your code here
    result = 0
    heapq.heapify(A)
    while len(A)>=2 and A[0]<k:
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        new=first+2*second
        heapq.heappush(A, new)
        result+=1
    if A[0]>=k:
        return result
    else:
        return -1
# 1. So basically heap is a data structure that is similar to tree but the root node will have the smallest value(min_heap)
# and its child nodes will have either equal or greater values
# 2. And the functions like heapq.heappush, heapq.heappop will automatically re-adjust the heap by itself to hold the min element 
# at its root, unlike the brute force method where we had to perform sort evertime an element was removed or appended, thats why
# this method is time efficient