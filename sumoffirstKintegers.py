x,y=input().split()
N=int(x)
K=int(y)
L=input().split()
s=0
for i in range(0,K,1):
  s=s+int(L[i])
print(s)
