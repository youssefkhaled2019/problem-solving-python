"""
contest=  https://codeforces.com/contest/791/problem/A
date= Saturday, December 16, 2023
Verdict  = Accepted
"""
a,b=map(int,input().split(" "))
c=0
while(True):
    a*=3
    b*=2
    c+=1

    if(a>b):
        break
print(c)    
