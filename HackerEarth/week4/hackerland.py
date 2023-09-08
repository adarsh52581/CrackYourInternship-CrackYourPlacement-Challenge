def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x.sort()
    
    n = len(x)
    result = 0
    i = 0
    
    while i < n:
        # Find the leftmost house that needs a transmitter.
        loc = x[i]
        
        # Place the transmitter at the rightmost house within range.
        while i < n and x[i] - loc <= k:
            i += 1
        
        # Now, i points to a house that is out of range. Place the transmitter one house to the left.
        i -= 1
        loc = x[i]
        
        # Move to the rightmost house that needs a transmitter.
        while i < n and x[i] - loc <= k:
            i += 1
        
        # Increment the result count.
        result += 1
    
    return result
# 1. so basically this is from chatGPT, I had somewhat the same idea and gave it a broken code and it returned the corrected working version of it
# 2. So what is happening is, we first find the range of houses to the left and then decrement the value of i and do the same to find the range to the right
# 3. The thing is I have idea for the problem but cannot implement on my own,its wierd and sad.