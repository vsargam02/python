#Strings

# s='hello world'
# print(s[-1])
# print(s[0])
# print(s[2:7])
# print(s[::-1])

# IMMUTABLE
#s[0]='Y'
# fname='jasmine'
# lname='awatramani'
# fullname= fname+lname
#print(fullname)

# fname='jasmine !'
#print(fname)

# a='hello'
# b=a
# c='hello'
# d=str(a)
# e=a[:]
# print(a is e)
# print(a is c)
# print(a is d)
# f='hel'+ 'l' + 'o'
# g='hel'[:]+ 'lll'[0] + 'o'
# print(a==f)
# print(a is f)
# print(a==g)
# print(a is g)
# string cannot change so it can point to various variable and the process called interning

#s= s +'!!'
#print(s)
#s= print(s.upper())
#print(s+'!!')
#print(s)

#print(s.index('ll'))
#print(s.count('ll'))
#print(s.startswith('he'))
#print(s)

# url='http://www.'
#url.lower().startswith("http")

#print(s)
# print(s.split())
#print(s.split('l'))
# print(s.split('o'))

#print(''.join(['a','b','c']))
#print('-'.join(['a','b','c']))
#print('l'.join(['he', '', 'o wor', 'd'])
# can be used for removing characters

sentence='the tallest tree is also the oldest tree'
words=sentence.split()
#print(words)
#print(len(words))

# lengths = [len(w) for w in words if len(w)>2]
#print(lengths)

# def isPalindrome(s):
#     #return s==s[::-1]
#     left =0
#     right=len(s)-1
#     while left<right:
#         if s[left]!= s[right]:
#             return False
#         left+=1
#         right-=1
#     return True

#print(isPalindrome('level'))
#print(isPalindrome('lever'))

# def printSubstrings(s):
#     n =len(s)
#     for start in range(n):
#         for end in range(start,n):
#             print(s[start:end+1])

#printSubstrings('hello World')

# def getSubstrings(s):
#     result=[]
#     n =len(s)
#     for start in range(n):
#         for end in range(start,n):
#             result.append(s[start:end+1])
#         return result
# #print(getSubstrings('hello world'))
#
#
# def printPallindromicsubStrings(s):
#     ssList=getSubstrings(s)
#     for ss in ssList:
#         if isPalindrome(ss):
#             print(ss)
#
# printPallindromicsubStrings('level')
#

#template string
# l=4
# b=5
# s=f"the rect with length {l} and breadth {b} has area{l*b}"
# #print(s)

#ternary

#x= 5 if COND else 0

# color='green'
# signal='stop' if color=='red' else 'go'
# #print(signal)
# ch='f'
# if 'A'<= ch <='Z':
#     print('upper')
# elif  'a'<= ch <='z':
#     print('lower')
# else:
#     print('symbol')

# 'C'- 'A'+ 'a - 'c'
# chr(ord('A')+ 32)-'a'
# chr(ord('a')-32)-'A'
#
# def toggleCase(str):
#     result =[]
#     for ch in str:
#         if ch.isupper():
#             result.append(ch.lower())
#         elif ch.islower():
#             result.append(ch.upper())
#         else:
#             result.append(ch)
#
#     return ''.join(result)
#
# print(toggleCase('Hello World'))



for i in range(1,8):
    x =i**3
    print(x)



























































