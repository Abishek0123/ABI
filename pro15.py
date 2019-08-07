c=int(input())
e=list(map(int,input().split()))
l1=[]
for i in e:
  ab=bin(i)
  l1.append(ab)
l2=sorted(l1)
l2.reverse()
for j in l2:
  print(int(j,2))
