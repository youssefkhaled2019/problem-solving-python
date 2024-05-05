"""
contest=https://codeforces.com/contest/431/problem/A
date=Wednesday, December 20, 2023
Verdict =Accepted
"""
s=list(map(int,input().split()))
move=list(map(int,input()))
sum_=0
for i in move:
   sum_+=s[i-1] 
print(sum_)