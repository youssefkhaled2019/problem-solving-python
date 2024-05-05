"""
contest=https://codeforces.com/contest/456/problem/A
date=  Monday, February 26, 2024 
Verdict =Accepted
"""
n = int(input())
o="Poor Alex"
for i in range(n):
    a,b =map(int,input().split())
    if b>a:
        o="Happy Alex"
print(o)        
        