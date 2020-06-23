#1 MAXIMUM IN LIST
# list=[2,4,5,6,78,99]
# def max(list):
#     max=0
#     for i in range(0,len(list)):
#         if list[i]>max:
#             max=list[i]
#
#     return max
#print(max(list))

#2
# marks=[40,60,70,80,50]
# def search(list,num):
#     for i in range(0,len(list)):
#         if list[i] == num:
#             return i
#
#     return -1
#print(search(marks,80))
#print(search(marks,200))

#3 IF THE LIST IS SORTED
marks=[20,30,40,50,60,70]
def binarySearch(sortedlist,num):
    left=0
    right=len(sortedlist)-1
    mid= (left+right)//2
    while left<=right:

        if sortedlist[mid]== num:
            return mid
        elif sortedlist[mid]<num:
            left= mid+1
        else:
            right = mid-1
        mid=(left+right)//2
    return None

#print(binarySearch(marks,50))


#4 REVERSE THE LIST
#marks=[2,5,6,7,8,9]
# def reverse(marks,start,end):
#     while start<end:
#         marks[start],marks[end]=marks[end],marks[start]
#         start+=1
#         end -=1
# print(marks)
# print(reverse(marks,0,5))

#5a BUBBLE SORT
arr= [2,4,6,1,3,8]
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def bubblesort(arr):
    n=len(arr)
    for j in range(1,n):
        for i  in range(n-j):
            if arr[i]>arr[i+1]:
                swap(arr,i,i+1)

#print(arr)
bubblesort(arr)
#print(arr)

# b SELECTION SORT

list=[2,4,5,7,9,1]
def swap(list,i,j):
    list[i],list[j]=list[j],list[i]

def selectionSort(list):

    pos=0
    n= len(list)
    while pos<n-1:
        for i in range(pos+1,n):
            if list[pos] > list[i]:
                swap(list,pos,i)
        pos=pos+1

# print(list)
# selectionSort(list)
# print(list)

#c INSERTION SORT
list= [8,4,6,3,1,2,9]
def swap(list,i,j):
    list[i],list[j]=list[j],list[i]

def insertionSort(list):
    start=1
    n=len(list)
    while start < n:
        for i in range(start,0,-1):
            if list[i]<list[i-1]:
                swap(list,i,i-1)
        start+=1

# print(list)
# insertionSort(list)
# print(list)

#6
stock=[2,4,6,8,1,9]
min=stock[0]
max= 0
p=stock[0]
s=stock[0]
for i in range(len(stock)):
    v=stock[i]
    if v-min >max:
        max= v-min
        p=min
        s=v
    if v<min:
        min = v
#print(max,p,s)

#7intersection array
A=[2,3,3,5,7,11]
B=[33,7,15,31]


# def intersect_sortedarr(A,B):
#     i=0
#     j=0
#     intersection =[]
#     while i<len(A) and j <len(B):
#         if A[i]==B[j]:
#             if i==0 and A[i]!=A[i-1]:
#                 print (A[i])
#             i+=1
#             j+=1
#         elif A[i]<B[j]:
#             i+=1
#         else:
#             j+=1
#     return intersection
#
# print(intersect_sortedarr(A,B))
# def intersection(a,b):
#          return

#8
# A=[-2,1,3,5,6,8,9]
# target =4
# def two_sum(A,target):
#     for i in range(len(A)-1):
#         for j in range(i+1,len(A)):
#             if A[i]+A[j]== target:
#                 print(A[i],A[j])
#                 return True
#     return False
#
# print(two_sum(A,target))
#8
num=[2,3,5,7,8,1,9]

# def two_sum(num,target):
#     for i in range(len(num)-1):
#         for j in range(i+1,len(num)):
#             if A[i]+A[j]== target:
#                 return A[i],A[j]
#
# print(two_sum(num,5))

#9
def three_sum(num,target):
    for i in range(len(num)-2):
        for j in range(i+1,len(num)-1):
            for k in range(i+len(num)):
                if A[i]+A[j]+A[k]== target:
                    return A[i],A[j],A[k]
#print(three_sum(num,10))

#10 sum of arr

# arr1=[8,3,7,9]
# arr2=[4,1,6,9]
# n1= len(arr1)
# n2=len(arr2)
# n= max(n1,n2)+1
# arr3=[None]*n
#
# c= 0         #carry over
# for i in range(1,n+1):
#     a=arr1[-i] if -i>=-n1 else 0
#     b=arr2[-i] if -i>=-n2 else 0
#     s =a+b+c
#
#     c=s//10
#     arr3[-i] = s%10
#print(arr3)


#11
def inverse(num):
    numStr= str(num)
    n= len(numStr)
    result=[None]*n
    for i in range(len(numStr)):
        d= int(numStr[i])
        p=i+1

        result[d-1]=p
    return result

print(inverse(54123))

#12
