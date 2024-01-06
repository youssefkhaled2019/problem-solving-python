"""
contest=  https://codeforces.com/contest/520/problem/A
date=  Saturday, January 6, 2024
Verdict =Accepted
"""

n=int(input())
s=input().lower()
if(len(set(s))==26):
    print("YES")
else:
    print("NO")    