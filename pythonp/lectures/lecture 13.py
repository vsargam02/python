# Function programming
# we treat the data as if it is immutable
#data ad function are mutation


# def twice(x):
#     return 2*x
#map; it double the value,one fucntion  apply on every elements
# a=[1,2,3,4]
# m= list(map(lambda x:2*x, a))
# print(m)
#
# # filter = used to remove the values
#
# f= list(filter(lambda x:x%2==0,a))
# print(f)
#
#
from functools import reduce
# r= reduce(lambda x,y: x+y,a)
# print(r)
#
# print(a)
#imperative vs declarative
# a=[1,2,3,4]
# output=[]
# for i in range(len(a)):
#     x=a[i]
#     output.append(x)
# print(output)

meters =[1,2,3,4.5,-1,0]
# validMeters= list(filter(lambda x:x>0),meters)
# cms =list(map(lambda x: 100*x , validMeters))
# total =reduce(lambda x,y:x+y,cms)
# print(total)
#
# total=sum([m*100 for m in meters if m>0])
# print(total)

# a= [20,30,40,10]
# r= reduce(lambda x,y: x if x>y else y,a)
# print(r)

# a=[1,2,3,4]
# b=[4,6,8,0]
# c=[0,0,3,4]
# m = list(map(lambda x,y,z:x+y+x ,a,b,c))
# print(m)

# a= [1,2,3,4]
# b=[10,20,30,40]
# c=[6,7,8,9]
# z= dict(zip(a,b,))
# print(z)

# a=[20,40,50,10]
# s = sorted(a)
# print(s)
# print(a)
# power = lambda x,y :x**y
# square = lambda x:power(x,2)
# print(square(4))

import time
# print(time.time())

import random
#random.seed (100)
r=random.random()
#print(90+r*10)
print(random.random())
print(random.random())
print(random.random())

# s= 'hello'\
#     'world'
#
# s= """ hello
# world"""          #multiline string
#
# msg= 'coding'
# s= f"""
# <html>
#     <body>
#         {msg}
#     </body>
# </html?
# """
# print(s)


