#3
a=[[11,12,13,14],
   [21,22,23,24],
   [31,32,33,34],
   [41,42,43,44]]

def spiralPrint(mat):
  numRows=len(mat)
  numCols = len(mat[0])
  left = 0
  right =numCols-1
  top=0
  bottom =numRows-1
  while left<=right and top<=bottom:
    for r in range(top,bottom+1 ):
      print(mat[r][left])       #left index common and rows are changing
    left +=1

    for c in range(left,right+1):
      print(mat[bottom][c])
    bottom-=1
    for r in range(bottom,top-1,-1):
      print(mat[r][right])
    right -=1
    for c in range(right,left-1,-1):
      print(mat[top][c])
    top+=1

#spiralPrint(a)

#2
# mat=[[11,12,13,14],
#      [21,22,23,24],
#      [31,32,34,35],
#      [41,42,43,44]]
#
# numRows=len(mat)
# numCols=len(mat[0])
# for col in range(numCols):
#   if col%2==0:
#     for row in range(numRows):
#       print(mat[row][col])
#   else:
#       for row in range(numRows-1,-1,-1):
#         print(mat[row][col])


#1
# mat=[[11,12,13,14],
#      [21,22,23,24],
#      [31,32,34,35],
#      [41,42,43,44]]
# numRows=len(mat[0])
# numCols=len(mat)
# for row in range(numRows):
#   if row%2==0:
#     for col in range(numCols):
#       print(mat[row][col])
#   else:
#       for col in range(numCols-1,-1,-1):
#         print(mat[row][col])

#4
a=[[11,12,13,14],
   [21,22,23,24],
   [31,32,33,34],
   [41,42,43,44]]

  numCols=len(mat)
  numRows= len(mat[0])
  right= 0
  left =numRows-1
  bottom=0
  top =numCols-1
  while left<=right and top<=bottom:
    for r in range(top,bottom+1 ):
      print(mat[r][right])       #left index common and rows are changing
    right +=1

    for c in range(right,left+1):
      print(mat[bottom][c])
    bottom-=1
    for r in range(bottom,top-1,-1):
      print(mat[r][right])
    right -=1
    for c in range(right,left-1,-1):
      print(mat[top][c])
    top+=1