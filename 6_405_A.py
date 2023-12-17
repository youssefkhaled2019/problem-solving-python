"""
contest=  https://codeforces.com/contest/405/problem/A
date= Sunday, December 17, 2023 
Verdict  = Accepted
"""
n =int(input())
ls=sorted(map(int,input().split(" ")))
print(*ls)



----------------------
n=int (input())
w=list(map(int,input().split(" ")))
w.sort()
print(*w)


#input();print(*sorted(input().split(),key=int))