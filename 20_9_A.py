"""
contest=https://codeforces.com/contest/9/problem/A
date=Saturday, December 23, 2023
Verdict =Accepted
"""
a,b=map(int,input().split())
m=6-max(a,b)+1
r=["1/6","1/3","1/2","2/3","5/6","1/1"]
print(r[m-1])