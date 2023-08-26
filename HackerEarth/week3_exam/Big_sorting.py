#https://www.youtube.com/watch?v=UOUN2zRvsWo
#logic: given a list of string we need to return a list of sorted string which are actually integers
#using the normal method of convertin to int and using the .sort() method wont work as the number of digits in each integer are very high->time exceeded
#so use the method of sorting the strings by length first and then then sorting those individual groups

def bigSorting(unsorted):
    unsorted.sort(key = lambda x: (len(unsorted),x))
    return unsorted

#sort() can have two parameters -1. reverse and -2. key
# here the key value is a tuple of len() of each character and the integer or string itself
# first the sorting is based on len(string) and then the string of equal length