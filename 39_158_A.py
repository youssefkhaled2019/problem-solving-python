"""
contest=https://codeforces.com/contest/158/problem/A 
date= Thursday, February 22, 2024 
Verdict =Accepted
"""
n,k =map(int,input().split())
l=list(map(int,input().split()))
c=len([ i for i in l if i >=l[k-1] and i !=0 ])
print(c)