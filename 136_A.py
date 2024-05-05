"""
contest=https://codeforces.com/contest/136/problem/A 
date=  Friday, December 29, 2023 
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split()))
l_ =[]
ii=1
for i in range(n):
    l_.extend([l.index(i+1)+1])
print(*l_)



------------------------------------
n=int(input())
l=list(map(int,input().split()))
l_ =[]
for i in range(n):
    l_.extend([l.index(i+1)+1])
    
#for i in range(n):
#    print(l_[i],end=" ")

print(" ".join(map(str,l_)))
    
    
"""
input  4
input  2 3 4 1
Output 4 1 2 3
-----------
index  = 1 2 3 4
values = 2 3 4 1


"""

