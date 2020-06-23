#iteger answer
def log(x,b):
    result = 0
    while x > 1:
        x /= b
        result += 1
    return result
#print(log(8,2))

#lists
x=[10,20,30,40,30,50]
# print(x[0])
# print(x[1])
# print(x[3])
# print(x[4])
# print(x[-4])
# print(x[-5])

# print(x[1:4:2])
# print(x[1:])
# print(x[:])
# print(x[:4])
#
# x[1:3]=[200]
# print(x)
# x[1:3]=[200,300,100]
# print(x)

# print(x[4:0:-1])
# print(x[::-1])    reversing a list
# x.append(60)   #add at the end
# print(x)
# x.insert(0,100)   insert in between
# print(x)
# x.pop(3)   opp of append(pass index
#print(x)
# x.remove(30)
# print(x)     pass value

#print(x.count(30))
#
# print(x.index(30))
# print(x)
# print(x.index(30,3))
# print(x)
# print(len(x))
# print(sum(x))
# print(max(x))
# print(min(x))

# print([1,2]+[4,5])
# print([1,2]*3)

#for i in range(len(x)):
#    print(x[i])
 #   print(i)

# for v in x:
#     print(v)

# def total(arr):
#     return sum(arr)
# print(total([10,20,30]))
# def total(arr):
#     result=0
#     for v in arr:
#         result+=v
#         return result
# print(total([10,20,30]))

# def total(list):
#     x=0
#     for i in range(len(list)):
#         x+=list[i]
#         return x
# print(total([10,20,30]))


# def maximum(arr):
#     result=arr[0]
#     for v in arr:
#         if v >result:
#             result=v
#     return result
# print(maximum([10,20,30,40]))

# def linearSearch(arr,num):
#
#     for i in range(len(arr)):
#         if num==arr[i]:
#             return i
#     return None
#
# myList = [10,20,30]
# print(linearSearch(myList,20))
# print(linearSearch(myList,200))

# a=[1,2,3]
# b=a
#
# a[0]=100
# print(a)
# print(b)

a=[1,2,3]
b=a
c=[1,2,3]
d=list(a)
e=a[:]
#print(id(a))
#print(id(b))

# print(a==b)      values compare
# print(a is b)     address compare
# print(a==c)
# print(a is c)

# print(a==d)
# print(a is d)

# print(a==e)
# print(a is e)

# a=4
# b=5
# print(a,b)
# temp=a
# a=b
# b=temp
# print(a,b)

# a=a+b
# b= a-b
# a=a-b
# print(a,b)

# a,b=b,a
# print(a,b)

# def swap(x,y):
#     x,y=y,x
#
# swap(a,b)
# print(a,b)
arr=[10,20,30]
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

# swap(arr,0,1)
# print(arr)

#binary search
arr=[1,2,4,5,7,8,9,10,12,15,20,30,40,50]
def binarySearch(sortedList, num):
    left=0
    right=len(sortedList)-1
    mid=(left+right)//2
    while left<=right:
        if sortedList[mid]==num:
            return mid
        elif sortedList[mid]<num:
            left= mid+1
        else:
            right= mid-1
        mid = (left + right) // 2
    return None

# print(binarySearch(arr,50))
# print(binarySearch(arr,10))
# print(binarySearch(arr,300))

#sorting
# o(n2)                 O(nlogn)                       O(n)
# bubble                 quick                         bucket
# selection              merge                         radix
# insertion              heap                         lexicographical
#if range defined then bucket sort and radix
# not fixed range quick and merge

#bubble sort
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
    

def bubbleSort(arr):
    n=len(arr)
    for j in range(1,n):
        for i in range(n-j):
            if arr[i]>arr[i+1]:
                swap(arr,i,i+1)

arr=[9,8,7,6,5,4]
print(arr)
bubbleSort(arr)
print(arr)

def reverse(arr):
    left=0
    right=len(arr)-1
    while right >left:
        swap(arr,left,right)
        left+=1
        right-=1


myList=[1,2,3,4]
reverse(myList)
#print(myList)


#list comprehesion

a=[x**2 for x in range(1,5) if x>2]
#print(a)

b=[x**2 for x in range(100,201) if x%13==0]
#print(b)
# c=[[i] i for i in range(1,5)]
# print(c)
d=['hello' for i in range(1,5)]
#print(d)

#2-D list
a=[[1,2],
   [3,4],
   [5,6,7]]
# print(a)
# print(a[0])
# print(len(a))
# print([0][0])

#print(a[0][1])

def total(mat):
    # ressult=0
    # for row in mat:
    #     for col in row:
    #         result +=col
    # return result

    #     or
    result=0
    rows= len(mat)
    for r in range(rows):
        cols = len(mat[r])
        for c in range(cols):
            result +=mat[r][c]
    return result

matrix=[[1,2],
        [3,4],
        [5,6]]
#print(total(matrix))

mat=[[1,2],[3,4]]
#print(mat*2)

