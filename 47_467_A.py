"""
contest= https://codeforces.com/contest/467/problem/A
date= Wednesday, February 28, 2024 
Verdict =Accepted
"""




n=int(input())
available=0
for  i in  range(n):
    p,q=list(map(int,input().split()))   #p =people living in
    if(p+2<=q):available+=1              #q  =capacity room
print(available) 