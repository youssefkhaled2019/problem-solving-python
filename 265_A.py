"""
contest=https://codeforces.com/contest/265/problem/A
date= Saturday, December 23, 2023
Verdict =Accepted
"""

s=list(input())
t=list(input())
m=0
for i in range(len(t)):
    
    if(s[m]==t[i]):
        m+=1

print(m+1)