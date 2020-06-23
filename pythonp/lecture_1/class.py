#LOOPS
# for i in range(1,5):
#     print(i)

# for i in range(1,5):
#     print(i*i)
#
# for  i in range(1,10,1):
#     print(i)

# for i in range(20,9,-1):
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(2,10,2):
#     print(i)

# for i in range(200,301):
#     if i%13==0:
#         print(i)

# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)

# num=7
# result=1
# for i in range(1,num+1):    (num,0,-1)
#     result *=i
# print(result)

# a=2
# b=5
# result=1
# for i in range(b):     #(1,b+1)
#     result*= a
# print(result)

#INPUT

# name=input("enter your name: ")
# print(name)

# a= int(input("enter the first num: "))
# b= int(4
# input("enter the seconf nun: "))
# print(a+b)

#WHILE LOOP

# cmd= input("enter command:")
# while cmd!= 'quit':
#     print(cmd)
#     cmd = input('enter command:')



# num =169
# isPrime = True
# for i in range (2,int(num**0.5)+1):         math.sqrt(num)
# #    print(i)
#     if num%i==0:
#         isPrime= False
#         break
# if isPrime:              #isPrime==True
#      print("prime")
# else:
#      print(' not prime')

# import math
#print (math.sqrt)


#n=8
# if all(n%i for i in range(2, int(n**0.5)+1)
#    print("prime")
#    else:
# print('not prime')

# pattern
# for row in range(1,6):
#     print('*'*row)

# for row  in range(1,6):
#     for i in range(row):
#         print('*',end='')
#     print()

# for row in range(1,6):
#     s = ''
#     for i in range(row):
#         s += '*'
#     print(s)

# spaces = 4
# stars=1
# for row in range(1,6):
#     s= ''
#     for i in range(spaces):
#         s+=' '
#     for i in range(stars):
#             s +='*'
#     print(s)
#     spaces -= 1
#     stars +=2

#for row in range(1,6):
#     s= ''
#     for i in range(5-row):
#         s+=' '
#     for i in range(2*row-1):
#             s +='*'
#     print(s)


# spaces=4
# stars=1
# for row in range(1,6):
#     print(' '*spaces + '*'*stars)
#     spaces-=1
#     stars +=2

# for row in range(1,6):
#     print(' '*(5-row)+ '*'*(2*row-1))

cmd = input('enter command')
while cmd!='quiet' and cmd!='exit':
    print(cmd)
    cmd = input('enter command:')




