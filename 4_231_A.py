"""
contest=https://codeforces.com/contest/231/problem/A
date=  Sunday, December 17, 2023 
Verdict  = Accepted
"""
n=int(input())
s=0
for i in range(n):
    a,b,c=map(int,input().split(" "))
    if (a+b+c>=2):
        s+=1
print(s)        



----------------------------------------------
n=int(input())
cont=0
for i in range(n):
    sum_=sum(map(int,input().split()))  # map(int, xs)
    if (sum_>=2):cont+=1  
    
print(cont)
