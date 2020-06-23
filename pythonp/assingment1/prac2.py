# num= 7
# fact=1
# for i in range(7,1,-1):
#     fact=fact*i
#     print(fact)
#
#
# num=7
# for i in range(2,num):
#     if num%i == 0:
#         print('not prime')
#
# import math
# num = 4
# isPrime= True
# for i in range(2,int(math.sqrt(num))):
#     print(i)
#     if num%i==0:
#         isPrime= False
#         break
# if isPrime==True:
#     print('prime')
# else:
#     print('not prime')
#
# for i in range(1,6):
#     print('@'*i
#
# # counter=1
# # for r in range(1,5):
# #     s=''
# #     for i in range(counter):
# #         s=s+str(counter)
# #         counter=counter+1
# #     print(s)
#
# i=1
# while i <=5:
#
#     print(i)
#     i=i+1


# rows=5
# space=4
# star=1
#
# for r in range(1,rows+1):
#     s=""
#     for sp in range(space):
#         s +=" "
#     for st in range(star):
#             s+='*'
#     print(s)
#     space -=1
#     star +=2

# rows = 5
# spaces=4
# stars =1
#
# for r in range(1,rows+1):
#     s=""
#     for sp in range (spaces) :
#         s +=" "
#     for st in range(stars):
#         s +="*"
#     print(s)
#
#     if r<=rows//2:
#         spaces -=1
#         stars +=2
#     else:
#         spaces +=1
#         stars -=2

#reverse
# num =3247
# result= 0
# while num!= 0:
#     digit = num % 10
#     num = num//10
#     result = result * 10
#     result = result + digit
# print(result)

# ch="A"
# print(ord(ch))

# for r in range(1,6):
#     s=""
#     for c in range(r):
#         if c==0 or c==r-1:
#             s+=str(r)
#         else:
#             s+='0'
#
#     print(s)

# a=0
# b=1
# c=a+b
# N=7
# print(0)
# print(1)
# while c<N:
#     print(c)
#     a=b
#     b=c
#     c=a+b

# for i in range(N-2):
#     a=b
#     b=c
#     c=a+b
# print(c)

# for i in range(N-1):
#     c=a+b
#     a=b
#     b=c
# print(c)

# rows=5
# stars =rows//2
# spaces=1
#
# for i in range(1,rows+1):
#       s=""
#       for st in range(stars+1):
#           s+="*"
#       for sp in range(spaces):
#            s+=" "
#       for st in range(stars+1):
#           s+="*"
#       print(s)
#
#       if i<=rows//2:
#           stars -=1
#           spaces +=2
#       else:
#           stars +=1
#           spaces -=2
spaces =3
for r in range(1,5):
    s=""
    numCols = 2*r-1
    counter=r
    for sp in range(spaces):
        s +=" "
    for c in range(2*r-1):
        s +=str(counter)

        if c<numCols//2:
            counter = counter+1
        else:
            counter -=1
    print(s)
    spaces -=1




