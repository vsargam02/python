# fibonacci
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)
#print(fib(7))

# fibMemory=[-1]*1000
# def fib(n):
#     if fibMemory[n]!= -1:
#         return fibMemory[n]
#     if n==0 or n==1:
#         return n
#     result =fib(n-1)+fib(n-2)
#     fibMemoryn [n]=result
#     return result
#
# print(fib(15))

#def pow(a,b):


"""list=[1,2,3,4,5]
print(list[1:0]+[list[1]])"""

"""pascal triangle"""


def printPascal(n):
    for line in range(1, n + 1):
        C = 1;  # used to represent C(line, i)
        for i in range(1, line + 1):
            # The first value in a
            # line is always 1
            print(C, end=" ");
            C = int(C * (line - i) / i);
        print("");

n = 5;
printPascal(n); 
