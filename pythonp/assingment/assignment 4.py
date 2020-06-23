#1 fahrenheit
def toCelsious(fahrenheit):
    y = (fahrenheit-32)/1.8
#    print(y)

#toCelsious(99)

#2 upper case
#ch= input('enter the character')
#print(ch.isupper())

#3

def power(x,n):
    result=1
    for i in range(n):
        result *=x
    return result

a= power(2,5)
#print(a)

#4prime
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
#print(isPrime(5))

#5 log base
def log(x,b):
    result=0
    while x>1:
        x/=b
        result +=1
    return result
#print(log(8,2))

#6 square root (newton method)
# def sqrt(num):
#     left=0
#     right=num
#     mid=(left+right)/2
#     sq=mid*mid
#     while abs(sq-num)> 1e-10:
#         if sq<num:
#             left=mid
#         else:
#             right=mid
#         mid=(left+right)/2
#         sq=mid*mid
#     return mid
#print(sqrt(100))

#7sqrt
#def sqrt(num))

#8 occurence of digits
def countoccurrence(number,digit):
    counter=0
    while number >0:
        last= number%10
        number=number//10
        if last == digit:
            counter+=1
    return counter
#print(countoccurrence(245674,4))

#9 ARMSTRONG NUMBER
#10 ARMSTRONG NUM IN RANGE
#11 HCF
# by using euclidean method
def hcf(a,b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    else:
        return a
# print(hcf(15,12))
# print(hcf(15,60))

#12 LCM
def lcm(a,b):
    return (a*b)/hcf(a,b)
#print(lcm(12,15))

#CALCULATOR


def cal():
    a= int(input('enter the first number'))
    b= int(input('enter the second number'))
    ch= input('select the operation to be performed:\n')

    while ch!='x':

        if ch =='+':
            print(a+b)
            return 0

        elif ch == '-':
            print(a-b)
            return 0

        elif ch == '*':
            print(a*b)
            return 0

        elif ch == '/':
            print(a/b)
            return 0
        elif ch =='%':
            print(a%b)
            return 0

    if ch=='x':
        return 0
cal()




#12
def isDecInc():
    prev = float('inf')         #to make positive infinity
    state='dec'
    n= int(input('enter the number of terms:'))
    for i in range(n):
        a=int(input('enter the term:'))
        if state == 'dec':
            if prev>a:
                prev=a
            else:
                state='inc'
                prev=a
        else:
            if prev<a:
                prev = a
            else:
                return False
    return True

#print(isDecInc())

#INVERSE
#make the stirng so we can use the indexx and then inverse the number
#no- 4567
#place=1234
#inverse= index value replaced by interger
def inverse(num):
    numStr= str(num)
    n= len(numStr)
    result=[None]*n
    for i in range(len(numStr)):
        d= int(numStr[i])
        p=i+1

        result[d-1]=p
    return result

#print(inverse(54123))

#
arr1=[8,3,7,9]
arr2=[4,1,6,9]
n1= len(arr1)
n2=len(arr2)
n=max(n1,n2)+1
arr3=[None]*n

c= 0         #carry over
for i in range(1,n+1):
    a=arr1[-i] if -i>=-n1 else 0
    b=arr2[-i] if -i>=-n2 else 0
    s =a+b+c

    c=s//10
    arr3[-i] = s%10
#print(arr3)

#ASSINGNMENT 5
# stock=[2,4,6,8,1,9]
# min=stock[0]
# max= 0
# p=stock[0]
# s=stock[0]
# for i in range(len(stock)):
#     v=stock[i]
#     if v-min >max:
#         max= v-min
#         p=min
#         s=v
#     if v<min:
#         min = v
# print(max,p,s)