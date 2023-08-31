def equalStacks(h1, h2, h3):
    # Write your code here
    pos1=pos2=pos3=0
    sum1=sum(h1)
    sum2=sum(h2)
    sum3=sum(h3)
    result = min(sum1,sum2,sum3)
    while result!=sum1 or result!=sum2 or result!=sum3:
        if sum1>result:
            sum1-=h1[pos1]
            pos1+=1
        if sum2>result:
            sum2-=h2[pos2]
            pos2+=1
        if sum3>result:
            sum3-=h3[pos3]
            pos3+=1 
        result = min(sum1,sum2,sum3)    
    return result
# hey there! so basically this is my code and I tried the method of first finding the sum of each list and then subtracting each element 
# from the front of the list until the result was equal to the sums, my problems were:
# 1. the while condition I first put result!=sum11=sum2 and so on its wrong as in python it execuets ina a linear fashion so it would return false results
# 2. then I put and condition which is also rong, it must be 'or'
# 3. the built in function to find sumk of all elements in a list is sum(array_name) and not array_name.sum()
# 4. needed help from chatGPT so many times. Speed too slow