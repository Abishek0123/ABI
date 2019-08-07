ab,cd=map(int,input().split())
ef=list(map(int,input().split()))
ab=[]
ef.insert(0,0)
for a in range(cd):
     v=[]
     s=0
     y,x=map(int,input().split())
     for b in range(y,x+1):         
         s^=ef[b]     
     ab.append(s)
for c in ab:
    print(c)
