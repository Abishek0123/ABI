ch=int(input())
ar=[int(i) for i in input().split()]
d=0
for i in range(ch):
   for j in range(i):
      if ar[j]<ar[i]:
         d+=ar[j]
print(d)
