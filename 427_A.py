"""
contest=https://codeforces.com/contest/427/status
date= Wednesday, December 20, 2023
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split(" ")))
s,o=0,0

for i in range(n):

    if (l[i]!=-1):
        s+=l[i]
    else:
        if(s>=1):
            s-=1
        else:
            o+=1    
print(o)



--------------------------
n =int(input())   
seqense =list(map(int,input().split()))
untreated=0
available=0
for i in seqense :
    if i >0:
        available+=i
    else :
        if (available> 0):
            available-=1
        else:
            untreated+=1
            
print(untreated)            
            