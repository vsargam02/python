#1.print natural number from 1 to 25

# for i in range(1,26):
#     print(i)

#2.reverse natural number from 30 to 1
# for i in range(30,0,-1):
#     print(i)

#3.print odd number
# for i in range(1,101,2):
#     print(i)

#4.sum of natural numbers 1 to 50
# sum = 0
# for i in range(1,51):
#     sum= sum+i
# print(sum)

#5.sum of even numbers
# sum=0
# for i in range(2,51,2):
#     sum=sum+i
# print(sum)

#6.factorial
# num= 7
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

#7.power
# a=2
# b=3
# result=1
# for i in range(b):
#     result *=a
# print(result)

#8.multiplication table
# num=3
# for i in range(1,11):
#     print(i*3)

#9.check number is prime or not
# num=2
# isPrime= True
# for i in range(2,int(num*0.5)+1):
#     print(i)
#     if num%i==0:
#         isPrime = False
#         break
# if isPrime:
#      print('prime')
# else:
#      print('not prime')

#10.print prime number from 1 to 100
# start=1
# end=100
#
# for num in range(start,end+1):
#     isPrime = True
#     for n in range(2,int(num**0.5)+1):
#         if num%n==0:
#             isPrime= False
#     if isPrime:
#         print(num)



#11. enter a command
# cmd = input("input command:")
# while cmd!= "x":
#     print(cmd)
#     cmd=input("input command:")

#12. print triangle
# for i in range(1,6):
#     print("*"*i)
#
# #or
# for row in range(1,6):
#     s=''
#     for i in range(row):
#         s+='*'
#     print(s)

#triangle
space=4
star=1
for row in range(1,5):
    s=''
    for i in range(space):
        s=' '
    for i in range(star):
        s+='*'
    print(s)

    space -= 1
    star+=1

#13.triangle
# rows=5
# spaces=4
# star=1
# for r in range(1,rows+1):
#     s=''
#     for i in range(spaces):
#         s+=' '
#     for n in range(star):
#         s+='*'
#     print(s)
# 
#     spaces -=1
#     star +=2
# 




