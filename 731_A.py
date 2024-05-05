"""
contest=  https://codeforces.com/contest/731/problem/A
date= Thursday, December 21, 2023
Verdict = Accepted
"""
w='a'+input()
x=0
for i in range(len(w)-1):
    tem_1= abs((ord(w[i])%ord('a') ) -(ord(w[i+1])%ord('a') ))
    tem_2= abs(tem_1-26)
    x+= min (tem_1 , tem_2 )
print(x)
-----------------------------------------
word=list(input())

pointer="a"
sum_=0
for i in range(len(word)):
    
   v1=abs(ord(pointer)-ord(word[i]) ) 
   v2=abs(abs(ord(pointer)-ord(word[i]) ) -26)
   if v1<v2:
       sum_+=v1
   else:
       sum_+=v2
   pointer=word[i]
       
   


print(sum_)