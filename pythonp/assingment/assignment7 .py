#recursion
#factorial
def factorial(n):
    if n<=1:
        return 1
    return n* factorial(n-1)

#print(factorial(5))

#2
def hcf(a,b):
    if a==0 or b==0:
        return a+b
    if a>b:
        return hcf(a%b,b)
    if a<b:
        return hcf(b%a,a)
#print(hcf(12,15))

#3 palindrome
a=[1,2,1]
# def ispalindrome(a):
#     if len(a)<=1:
#         return True
#     else:
#         return a[0]==a[-1] and ispalindrome(a[1:-1])
#print(ispalindrome(a))
           #or

def isPalindrome(arr):
    original=arr
    new_arr =arr[::-1]
    if new_arr == original:
        return True
    return False
#print(isPalindrome([1,2,3,4,5,5,5]))

#4
arrr= [1,2]
def reverse(arr):
    if len(arr)== 1 or len(arr)==0:
        return arr
    else:
        return reverse(arr[1:])+[arr[0]]

#print(reverse(arrr))

#5 power
def pow(a,b):
    if b==0:
        return 1
    if b<0:
        return 1/pow(a,-b)
    partial = pow(a,b//2)
    if b%2==0:
        return partial*partial
    else:
        return a*partial*partial
#print(pow(2,3))

#6 fibonacci
fibMemory = [-1]*1000
def fib(n):
    if fibMemory[n]!=-1:
        return fibMemory[n]
    if n==0 or n==1:
        return n
    result = fib(n-1)+fib(n-2)
    fibMemory[n] = result
    return result

#print(fib(8))

#7 pattern

# def pattern(num,char):
#     if num>0:
#         pattern(num-1,char)
#         print(num*char)
# print(pattern(5,'*'))

 #or
# def pattern(n):
#     if n<1:
#         return
#     pattern(n-1)
#     print('*'*n)
#
# print(pattern(5))

#8
def pattern(n):
    if n<1 :
        return
    pattern(n
            )
    print('*'*n)

print(pattern(5))