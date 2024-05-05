"""
contest=https://codeforces.com/problemset/problem/686/A
date=  Sunday, December 24, 2023 
Verdict = Accepted
"""

n,x=list(map(int,input().split(" ")))
c=0
for i in range(n):
    d_1,d_2=input().split(" ")
    d_2=int(d_2)
    if(d_1=="-"and x>=d_2):
        x-=d_2
    elif(d_1=="-"and x<d_2):
        c+= 1
    elif(d_1=="+")  :
       x+=d_2
print(x,c)       
     
