"""
contest=  https://codeforces.com/contest/556/problem/A 
date= Saturday, February 24, 2024 
Verdict =Accepted
"""
n=int(input())
s=input()
c_0=s.count("0")
c_1=s.count("1")
print(len(s)-min(c_0,c_1)*2)