"""
contest=https://codeforces.com/contest/443/problem/A 
date=  Wednesday, December 27, 2023 
Verdict =Accepted
"""
s=input()
a={'{':"",
   "}":"",
   ",":"" ,
   " ":""}
for i,j in a.items():
    s=s.replace(i,j)

print(len(set(s)))
