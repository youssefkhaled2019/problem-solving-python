"""
contest=  https://codeforces.com/contest/294/problem/A 
date=Saturday, December 23, 2023
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split(" ")))
r=int(input())
for i in range(r):
    x,y=list(map(int,input().split(" ")))
    x-=1
    if (x==0 and n!=1): #left
        l[x+1]+=abs(y-l[x])
        l[x]=0
    elif(x+1==n and n!=1): #rigth
        l[x-1]+=abs(1-y)
        l[x]=0
    elif(1<=x<=n-1):
         l[x-1]+=abs(1-y)
         l[x+1]+=abs(y-l[x])
         l[x]=0
    else:
      l[x]=0     
for i in l:
    print (i)

----------------------------------
totla_box=int(input())
box=list(map(int ,input().split()))
n=int(input())

for i in range(n):
   n_box,i_box=list(map(int ,input().split()))
   n_box-=1
   
   if (n_box != 0):
       box[n_box-1]+=i_box-1
   if (n_box!= totla_box-1):
       box[n_box+1]+=box[n_box]-i_box
   
   box[n_box]=0


for i in  box:
    print (i)
    
       
       

    