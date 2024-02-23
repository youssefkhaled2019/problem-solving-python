"""
contest=  https://codeforces.com/contest/282/problem/A 
date=  Friday, February 23, 2024 
Verdict =Accepted
"""
        
n=int(input())
c=0
for i in range(n):
    w=input()
    if ("++"in w):
        c+=1
    elif ("--"in w): 
        c-=1

print(c)


