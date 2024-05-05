"""
contest=https://codeforces.com/contest/268/problem/A
date=Thursday, December 21, 2023
Verdict =Accepted
"""
n=int(input())
l1=[]
l2=[]
s=0
for i in range(n):
    a,b=list(map(int,input().split()))
    l1.extend([a])
    l2.extend([b])
 
for i in range(n):
    for j in range(n):
        if (l1[i]==l2[j]):
            s+=1
print(s)  