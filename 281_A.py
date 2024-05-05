"""
contest=  https://codeforces.com/contest/281/problem/A  
date=  Thursday, February 22, 2024 
Verdict =Accepted
"""

s=input() 
if("A"<=s[0]<="Z"):
    print(s)
else:    
    f=chr(ord('A')+(ord(s[0])%ord('a')))
    print(f+s[1:])    