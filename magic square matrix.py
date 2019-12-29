print("MAGIC SQUARE MATRIX:\n")
number=int(input("Enter the number of rows and columns:"))
i=number
j=number
d1=0
d2=0
count=0
count1=0
list1=[[0 for o in range(i)]for m in range(j)]
row=[]
col=[]
for i in range(number):
  for j in range(number):
    list1[i][j]=int(input("\nEnter the matrix element...array[{0}][{1}]:".format(i,j)))
for k in range(number):
  d1=d1+list1[k][k]
for l in range(number-1,-1,-1):
  m=number-l-1
  d2=d2+list1[l][m]
if d1==d2:
 for q in range(number):
  row.append(0)
 for n in range(number):
  for p in range(number):
    row[n]=row[n]+list1[n][p]
 for r in range(number):
  col.append(0)
 for s in range(number):
  for t in range(number):
    col[s]=col[s]+list1[t][s]
 for u in range(1,number,+1):
  if row[0]==row[u]:
    count=count+1
 if count==number-1:
  for v in range(1,number,+1):
     if col[0]==col[v]:
        count1=count1+1
  if count==count1:
    if row[0]==col[0]==d1==d2:
      print("Your matrix is magic square matrix...")
    else:
      print("Your matrix is not a magic matrix...")
  else:
    print("Your matrix is not a magic matrix...")
 else:
  print("Your matrix is not a magic square matrix...")
else:
  print("Your matrix is not a magic matrix...")
