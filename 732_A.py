"""
contest=https://codeforces.com/contest/732/problem/A
date=Friday, December 22, 2023
Verdict =Accepted
"""

x,y=list(map(int,input().split(" ")))
i=1

while(1):
    if (((i*x)%10==0) or (((i*x)%10)-y==0)):
        print (i)
        break
    else:
        i+=1

