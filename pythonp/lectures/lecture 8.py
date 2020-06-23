#Recursion
def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)     #recursive case
#print(fact(5))
#memoization
memory =[None]*1000
def fib(i):
    if memory[i]!= None:
        return memory[i]
    if i==0 or i==1:
        return i
    result = fib(i-1)+fib(i-2)         # complexity 2^n
    memory[i]= result
    return result

#print(fib(24))

# def pow(a,b):
#     if b==0:
#         return 1
#     return a*pow(a,b-1)
# #print(pow(2,5))

def pow(a,b):
    if b==0:
        return 1
    if b<0:
         return 1/pow(a,-b)
    partial = pow(a, b // 2)
    if b%2==0:

        return partial*partial
    else:
        return a*partial*partial

#print(pow(2,-4))




def hcf(a,b):
    if a==0 or b==0:
        return a+b
    if a>b:
        return hcf(a%b,b)
    else:
        return hcf(a,b%a)

#print(hcf(12,15))
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#print(fact(3))

#

#
