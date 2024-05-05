"""
contest=https://codeforces.com/contest/677/problem/A
date=   Saturday, December 16, 2023 
Verdict =Accepted
"""
n,h=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
s=0
for i in range(n):
    if (l[i]>h):
        s+=2
    else:
        s+=1

print(s)