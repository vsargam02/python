#functions
def f(x):
    y= 2*x
    print(y)


#f(5)           #fuction calling
#f(2)
#f(10)

def area(l,b): # parameters
    y=l*b
    print(y)

# area(4,5)        #arguments
# area(20,100)

def area(l,b):
    y=l*b
    return y
# a1= area(4,5)
# a2= area(3,6)
# print(a1,a2)
# print(a1+a2)
# print(a1+a2 >30)

def hello(name):
    print('hello ' + name)

# hello('a')
# hello('b')

def hello(num):
    print('hello'*num)

# hello(4)

def toCelsious(faherenheit):
    y = (faherenheit-32)/1.8
    print(y)

# toCelsious(77)
# toCelsious(100)

def power(a,b):
    result=1
    for i in range(b):
        result *=a
    return result

x= power(2,5)
print(x)

# def isEven(num):
#     if num%2==0:
#         return True
#     else:
#         return False


# print(isEven(4))
# print(isEven(7))

def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

# print(isPrime(97))
# print(isPrime(100))
def printPrime(start,end):
    for i in range(start,end+1):
        if isPrime(i):
            print(i)
# printPrime(1,100)
#
# printPrime(2,100)

def hcf(a,b):
   while a!=0 and b!=0 :
       if a>b:
           a= a%b
       else:
           b= b%a
   return a+b

# print(hcf(12,15))
# print(hcf(60,15))
# print(hcf(100,1))

def lcm(a,b):
    return (a*b)/hcf(a,b)

# print(lcm(12,15))
# print(lcm(60,15))


def reverse(num):
    result=0
    while num>0:
        d= num%10
        num//=10
        result*=10
        result+= d
    return result


# print(reverse(3714))
# print(reverse(3714)+1)

def isArmstrong(num):
    result=0
    original = num
    while num!=0:
        d=num%10
        num//=10
        result += d**3
    return result == original


# print(isArmstrong(371))
# print(isArmstrong(100))

def log(x,base):
    result=0
    while x>1:
        x/=base
        result +=1
    return result
# print(log(8,2))
# print(log(81,3))

def sqrt(num):
    left =0
    right=num        # right=num+1 for range of 0.5....
    mid = (left+right)/2
    sq=mid*mid
    while abs(sq-num)> 1e-10:
        if sq< num:
            left=mid
        else:
            right=mid
        mid =(left+right)/2
        sq=mid*mid
    return mid

# print(sqrt(100))
# print(sqrt(25.6))
# print(sqrt(102))
# print(102**0.5)

def log(x,b):

    left=0
    right=x
    mid=(left+right)/2
    est=b**mid
    while abs(est-x)> 1e-10:
        if est<x :
            left=mid
        else:
            right=mid
        mid=(left+right)/2
        est=b**mid
    return mid

print(log(81,3))
print(log(100,2))


