# arr = [2,3]
# arr2= [1,*arr,4]    # * for unpacking
# print(arr2)

# def foo(*args):    # we can pass multiple arguments
#     for v in args:
#         print(v)

#foo(1,2,3,4)

# def bar(**kwargs):
#     for x in kwargs.items():
#         print(x)

#bar(name='Anne',age=20)

#Annotations

# def fact(n:'int') ->'int':  # to indicate n is integer
#     if n==0:
#         return 1
#     return n* fact(n-1)
#print(fact(6))

#Decorators - change the behavior of function

import time
def bar(original):
    def modified(n):
        s=time.time()
        result =original(n)
        e=time.time()
        print(e-s)
        return result
    return modified



@bar
def foo(n):
    time.sleep(2)
    return 2*n

#print(foo(10000))

#scoping

# a=6
# def foo():
#     a=5
#     print(a)
#
# foo()
# print(a)

#Exception handling

# try:
#     a=int(input('enter first number'))
#     b=int(input('enter second number'))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as e:  # give only on zero division
#     print('cannot divide by zero:',e)
#
# print('hello')
# finally:
#     print('Finally do this!')
#
# try:
#     s1.pop()
#     except
#raise ValueError('Stack is empty')

