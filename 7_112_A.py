"""
contest=  https://codeforces.com/contest/112/problem/A
date= Monday, December 18, 2023
Verdict  = Accepted
"""
a=input().lower()
b=input().lower()
if (a==b):
    print(0)
elif(a<b):
     print(-1)
elif(a>b):
    print(1)





------------------------------old ---------------------------------

a,b=input().lower(),input().lower()
if (a==b):
    print(0)
elif(a<b):
    print(-1)
else:    
    print(1)
