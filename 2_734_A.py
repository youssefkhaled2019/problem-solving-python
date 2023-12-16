"""
contest=https://codeforces.com/contest/734/problem/A
date=  Saturday, December 16, 2023 
Verdict =Accepted
"""
n=int(input())
s=input()
if(s.count("A")>s.count("D")):
    print("Anton")
elif(s.count("A")<s.count("D")):
     print("Danik")
else:   
     print("Friendship")