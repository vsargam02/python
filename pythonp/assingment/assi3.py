#1.prime number
# num=145
# isPrime= True
# for i in range(2,int(num*0.5)+1):
#    # print(i)
#     if num%i==0:
#         isPrime= False
#         break
# if isPrime:
#     print("prime")
# else:
#     print("not prime")

#2. all prime upto 2 and N
# start=1
# end=100
# for num in range(start,end):
#     for i in range(2,num):
#         if num%i==0:
#             break
#         print(num)

#3reverse number
# num=7645
# result=0
# while num>0:
#     d=num%10
#     num=num//10
#     result =result*10
#     result=result+d
# print(result)

#4sum of odd places and even places
# num= 1234
# even=0
# odd=0
# i=1
# while num >0:
#         if i%2==0:
#                 even = even +num%10
#                 num=num//10
#                 i = i+1
#         else:
#                 odd=odd+num%10
#                 num=num//10
#                 i = i+1
# print('even number',even)
# print('odd number',odd)



#5. fibonacci series
# a=0
# b=1
# c=a+b
# N=15
# print(0)
# print(1)
# while c<N:
#     print(c)
#     a=b
#     b=c
#     c=a+b

#6.print nth fibonacci number

# a=0
# b=1
# c=a+b
# N=7
# for i in range(N-2):
#     a=b
#     b=c
#     c=a+b
# print(c)

#7.pattern floyd's triangle
row=5
space=3
num=1
for row in range(len(row)):
    s=""
    for c in range(row):
        s= s+str(num)
        num=num+1
    print(s)

# 8.pattern
# row=5
#
# for row in range(1,len(row)):
#     s=""
#     for c in range(row):
#         if c==0 or c==r-1:
#             s+=str(row)
#         else:
#             s+="0"
#         print(s)

#9.pattern
# row=6
#
# for row in range(1,row+1):
#     s=""
#     for c in range(row):


#10.fibonacci pattern
# row=4
# s+=f(counter)


#11.pattern
# row=5
# space=4
# star=1
# for r in range(1,row+1):
#     s=""
#     for sp in range(space):
#         s+=" "
#     for st in range(star):
#         s+="*"
#     print(s)
#
#     if r<=row//2:
#         space -=1
#         star +=2
#     else:
#         space +=1
#         star -=2





