def numPaths(r,c):
    if r==1 and c==1:
        return 1
    if r==0 or c==0:
        return 0
    if r==2 and c==1:
        return 0
    if r == 2 and c ==3:
        return 0

    return numPaths(r,c-1)+numPaths(r-1,c)
#print(numPaths(3,3))
arr=1,2,3
def getSubsets(arr):
    if len(arr)==0:       #if len(arr)==1:
        return[[]]
        #return [[],[arr[0]]]
    result=[]
    elem=arr[0]
    ssList = getSubsets(arr[1:])         # sslist is 2d list
    for ss in ssList:
        ss2 =list(ss)
        ss2.append(elem)
        result.append(ss)
        result.append(ss2)
    return result

#print(getSubsets(arr))       complexity 2^n

