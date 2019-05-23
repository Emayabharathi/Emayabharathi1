x=int(input())
y=int(input())
z=int(input())
if(x>y and z<x):
  print(x)
elif(y>x and z<y):
  print(y)
elif(z>x and y<z):
  print(z)
else:
  print("Invalid")
