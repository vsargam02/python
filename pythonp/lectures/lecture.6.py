#tuple
#t1=(1,2,3,4)
#print(t1)
#print(t1[::-1])
#t1[0]=100  error will come cz tuple is also immutable

#t0=(100) it printing the vlue not the tuple bcoz it take it as a mod mass to resolve this we put a comma
#t0=(100,)
#print(t0)

# a=(1,2)
# b=a
# c=(1,2)
# d=tuple(a)
# e=a[:]
# print(a is e)
# we consider the tuples over list bcoz it require less memory

# def foo():
#     return 10,20
#
# x=foo()   tuple is packing
# print(x)

def foo():
    return 10,20
x,y=foo()     #tuple is unpacking
#print(x)

#print((1,2)+(3,4))
#print(300 in [1,2,3,4])   to check number is exit or not

t1=(10,20,30,40)
for i,v in enumerate(t1):
#    print(i,v)
#    print(f"the value at {i} is {v}")



#DICTIONARY
 phonebook ={
    'Anne':1234,
    'anjali':4456,
    'cathy':7869
}
# print(phonebook['anjali'])
# print(phonebook)
# phonebook['anjali']=78997
# phonebook['hemi']=9999
# print(phonebook['anjali'])

#GUI.API,CLI

person={
    'name':'bill',
    'age':20,
    'address':{                      #nesting
        'city':'delhi',
        'zip': 110001
    },
    'friends' : ['a','b','c']
}

#for x in person:
    #print(x)
   # print(person[x])
   # print(x,person[x])
# print(person['name'])
# print(person['address'])
# print(person['friends'])

person={}
#person['name']=input('enter the nam')
# person['name']='anne'
# person['address']={}
# person['address']['city']='delhi'
# print(person)

#d={x:x**2 for x in range(1,6)}# dictionary comprehension
#print(d)

#SETS

#s1={1,2,3}
# print(s1)
# print(type(s1))
#s2=set() #empty set

# s2.add(1)
# s2.add(2)
# s2.add(3)
# s2.add(3)
# s2.add(3)
# print(s2)
# s2.remove(3)
# print(s2)

s3=set([1,2,3,3,3,3,3])
#print(s3)

#print(s3[0])
# cannot use range for loop bcz it does not have indev bcoz the have no order
#so we use enhacee fro loop

# for x in s3:
#     print(x)
s1={1,2,3,4}
s2={2,4}
s3={1,3,5,7}
# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# print(s1.union(s3))
# print(s1.intersection(s3))
# print(s1.difference(s3))
# print(s1.symmetric_difference(s3))

# sentence='the tallest tree is also the oldest tree'
# print(list(set(sentence.split())))




























































































