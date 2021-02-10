def partition(array, count, begin, end):
    pivot_idx = begin
    #firstTime = True
    #tempArr = []
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            print('arr: ' + str(i) + ', ' + str(pivot_idx) + str(array))
            if pivot_idx != i:
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
            #if firstTime == True and pivot_idx != i:
            #if pivot_idx != i:
                count[0] += 1
                #tempArr = array.copy()
                print('1: ' + str(i) + str(array))
                #firstTime = False
    
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    print('2: ' + str(pivot_idx) + ', ' + str(begin) + str(array))
    #tempArr = array.copy()
    #print('temp: ' + str(tempArr))
    count[0] += 1
    return pivot_idx

def quick_sort_recursion(array, count, begin, end):
    if begin >= end:
        #print('qsr_return: ' + str(array))
        return
    #print('qsr1: ' + str(array))
    pivot_idx = partition(array, count, begin, end)
    #print('qsr2: ' + str(array))
    #count[0] += 1
    quick_sort_recursion(array, count, begin, pivot_idx-1)
    quick_sort_recursion(array, count, pivot_idx+1, end)

def quick_sort(array, count, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, count, begin, end)


def main():
    count=[]
    count.append(0)

    arr = [1,3,5,2,4,6,7]
    #arr = [4,3,1,2]
    #arr = [2,3,4,1,5]
    #print(arr)
    res = quick_sort(arr,count)
    print(count[0])

main()
