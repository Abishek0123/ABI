ch,sa=map(int,input().split())
gb=list(map(int,input().split()))
ch=[]
gb.insert(0,0)
for a in range(as):
     a=[]
     c=0
     y,x=map(int,input().split())
     for b in range(y,x+1):         
         c^=ls[b]     
     ch.append(c)
for e in ch:
    print(e)
