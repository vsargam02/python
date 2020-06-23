#parttern
#logic - 2*row -1
#   1
#   232
#  34543
# 4567654


# space=3
# for r in range(1,5):
#     s=''
#     numCol=2*r-1
#     counter=r
#     for sp in range(space):
#         s+=' '
#     for c in range(r*2-1):
#         s+= str(counter)
#
#         if c<numCol//2:
#             counter+=1
#         else:
#             counter-=1
#     print(s)
#     space-=1

# for r in range(1,5):
#     s=''
#     counter = 1
#     for c in range(7):
#         if counter > r:
#             s +=' '
#         else:
#             s +=str(counter)
#
#
#         if c<3:
#             counter+=1
#         else:
#             counter-=1
#     print(s)
#

#  def area(l,b):
#     y=l*b
#     print(y)
#
# area(2,4)
def volume(l,b,h):
    y=l*b*h
    print(y)
    return y

volume(4,5,6)























