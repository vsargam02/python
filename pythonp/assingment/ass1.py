#1 max of two numbers
a=10
b=20
if a>b:
    print(a)
else:
    print(b)

#2 max of three numbers
a=40
b=70
c=60
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)

#3 check number is positive,negative or zero
n=5
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")

#4 print yes if divisible by 5 and 11
p=110
if p%5==0 and p%11==0:
    print("yes")
else:
    print("no")

#5 check whether a year is leap year or not

yr= 1900
if (yr%4==0 and yr%100==0) or yr%400==0:
    print("leap year")
else:
    print("not a leap year")

#6 check whether a upper case or lower case

st = 'A'
if st>='A' and st<='Z':
    print("U")
else:
    print('L')

#7 number of days in a month
month=2
if month==2:
    print("no of days: 28 days")
elif month ==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("no. of days: 31 days")
elif month ==2 or month==4 or month==6 or month==9 or month==11:
    print("no. of days: 30 days")
else:
    print("wrong month")

#8print minimum number of rupees
x = 50
two_th= x//2000
a = x%2000
print('required 2000 notes',two_th)

five_h = a//500
b = a%500
print('required 500 notes',five_h)

hundred= b//100
c = b%100
print('required 100 notes',hundred)

fifty = c//50
d = c%50
print('required 50 notes',fifty)
print(two_th+ five_h + hundred +fifty )





#9check triamgle is formed

i=3
j=4
k=5
if i+j>k and j+k>i and k+i>j:
    print("triagle is formed")
else:
    print("triangle is not formed")

#10 check whether the triangle is equilateral,isosceles or scalene
a=10
b=20
c=30

if a==b and b==c:
    print("equilateral")
elif a==b or b==c or c==a:
    print("isosceles")
else:
    print("scalene")



