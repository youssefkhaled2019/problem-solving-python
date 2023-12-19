"""
contest=  https://codeforces.com/contest/344/problem/A
date= Tuesday, December 19, 2023
Verdict =Accepted
"""

n=int(input())-1
a,b,c=0,0,1
a=int(input())
for i in range(n):
    b=int(input())
    if(a!=b):
        a=b
        c+=1
print(c)        


------------------------------------
n =int(input())
s=""
for i in range(n):
    s+=input()
print(s.count("00")+s.count("11")+1)  


