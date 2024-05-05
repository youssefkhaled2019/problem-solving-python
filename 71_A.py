"""
contest=  https://codeforces.com/contest/71/problem/A 
date=  Sunday, December 24, 2023
Verdict =Accepted
"""
x=int(input())
for i in range(x):
    w=input()
    if (len(w)<=10):
        print(w)
    else:
        print(w[0]+str(len(w)-2)+w[-1])



