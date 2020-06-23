#
# x = 2000
# if x>2000:
#
# two = x//2000
# a = x%2000
# print('required 2000 notes',two)
# elif a>500:
# five = a//500
# b = a%500
# print('required 500 notes',five)
#
# one_h = b//100
# c= b%100
# print('required 100 notes',one_h)
#
# fifty = c//50
# d = c%50
# print('required 50 notes',fifty)
# print(two+five+one_h+fifty)

# num= 4444
# even=0
# odd=0
# position=1
# while num>=0:
#         if position%2==0:
#             even = even+ num%10
#         num=num//10
#         position=position+1
# else:
#         odd = odd +num%10
#         num=num//10
#         position =position+1
# print('odd numb',odd)
# print('even numb',even)
num= 5555
even=0
odd=0
i=1
while num >0:
        if i%2==0:
                even = even +num%10
                num=num//10
                i = i+1
        else:
                odd=odd+num%10
                num=num//10
                i = i+1
#print('even number',even)
#print('odd number',odd)
print(50%2000)
print(2000%50)
print(50/2000)
print(2%5)
print(5%2)
print(7%1)