
def minSwaps(arr):
    n = len(arr)
     
    # Create two arrays and use 
    # as pairs where first array 
    # is element and second array
    # is position of first element

    #associates the index with the value.. ie [(0,2),(1,1)...]
    arrpos = [*enumerate(arr)]
    print(arrpos)
     
    # Sort the array by array element 
    # values to get right position of 
    # every element as the elements 
    # of second array.

    #sorts associated list by value.. ie [(1,1),(0,2)...]
    arrpos.sort(key = lambda it : it[1])
    print(arrpos)
     
    # To keep track of visited elements. 
    # Initialize all elements as not 
    # visited or false.

    #dict that tracks the indices visited.. ie {0: True, 1: False...} 
    vis = {k : False for k in range(n)}
    print(vis)
     
    # Initialize result
    # sums up the cycle size
    ans = 0
    for i in range(n):
         
        # skip this iteration if:
        # already swapped OR at correct position
        if vis[i] or arrpos[i][0] == i:
            continue
             
        # find number of nodes 
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
         
        while not vis[j]:
             
            # mark node as visited
            vis[j] = True
             
            # move to next node
            j = arrpos[j][0]
            cycle_size += 1
             
        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
             
    # return answer
    return ans

#arr = [1, 5, 4, 3, 2]
arr = [1,3,5,2,4,6,7]
#arr = [4,3,1,2]
#arr = [2,3,4,1,5]
arr = [3,7,6,9,1,8,10,4,2,5]
print(minSwaps(arr))

##list = [1,2,3,4,5]
##squaredList = map(lambda x: x*x, list)
##print(squaredList)
##
##f = lambda x : 2 * x
##print (f(3))

##def main():
##    count=[]
##    count.append(0)
##
##    
##    #print(arr)
##    res = quick_sort(arr,count)
##    print(count[0])
##
##main()


