"""
contest= https://codeforces.com/contest/266/problem/A   
date= Wednesday, December 20, 2023
Verdict =Accepted
"""


n=int(input())
c=list(input())
neighbor=0
for i in range(len(c)-1):
    if (c[i]==c[i+1]):
        neighbor+=1
print(neighbor)  