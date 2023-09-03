import heapq
q = int(input())
heap_new=[]
lookup = set()
for _ in range(q):
    t=input().split()
    if t[0]=='1':
        ele=int(t[1])
        heapq.heappush(heap_new,ele)
        lookup.add(ele)
    elif t[0]=='2':
        lookup.discard(int(t[1]))
    else:
        while heap_new[0] not in lookup:
            heapq.heappop(heap_new)
        print(heap_new[0])
# 1. so I was able to complete 9 testcases by myself but it was apparently time consuming when the choice was to delete an element
# 2. So we created a new set to hold all the elements and then delete it from just the set
# 3. Later when the smallest element in the heap was to be displayed we delete all the first elements from heap hich is not in lookup
# 4. Thereby reducing the time to nlogn from n^2.