"""
contest=https://codeforces.com/contest/339/problem/A 
date=Sunday, December 24, 2023
Verdict =Accepted
"""
l=list(map(int,input().split("+")))
print("+".join(map(str,sorted(l))))



#=========================solution 1 ==================================
#n=list(map(int,input().split("+")))
#print("+".join(map(str,sorted(n))))


#=========================solution 1 ==================================
#print('+'.join(sorted(input()[::2])))#1+1+3+1+3 ->['1', '1', '1', '3', '3']
