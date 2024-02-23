"""
contest=https://codeforces.com/contest/69/problem/A
date= Friday, February 23, 2024 
Verdict =Accepted
"""
n=int(input())
i,j,z=0,0,0
for l in  range(n):
    _1,_2,_3=list(map(int,input().split(" ")))
    i+=_1
    j+=_2
    z+=_3


if(i==j==z==0):
    print("YES")
else:
    print("NO")    

