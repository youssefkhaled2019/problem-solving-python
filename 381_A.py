"""
contest=https://codeforces.com/contest/381/problem/A
date= Tuesday, December 19, 2023
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split(" ")))

s,d=0,0
id_l,id_r=0,n-1

for i in range(0,n):

    if(i%2==0):

        if (l[id_r]>l[id_l]):
            s+=l[id_r]
            id_r-=1
        else:
            s+=l[id_l]
            id_l+=1

             
    else:   

        if (l[id_r]>l[id_l]):
            d+=l[id_r]
            id_r-=1
        else:
            d+=l[id_l]
            id_l+=1






print(s,d)