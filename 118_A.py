

"""
contest=https://codeforces.com/contest/118/problem/A
date=  Monday, February 26, 2024 
Verdict =Accepted
"""
word=list(input().lower())
vowels=["a", "o", "y", "e", "u", "i"]
res=""
for i in range(len(word)):
    if (word[i] in vowels):
        continue
    else:
        res+='.'+word[i]
print(res)
