"""
contest=https://codeforces.com/contest/236/problem/A
date= Monday, December 18, 2023
Verdict =Accepted
"""
if(len(set(input()))%2!=0):
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")




----------------------------
print(["CHAT WITH HER!","IGNORE HIM!"][len({*input()})%2])

