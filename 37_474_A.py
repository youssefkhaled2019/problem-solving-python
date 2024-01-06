"""
contest= https://codeforces.com/contest/474 
date=  Saturday, January 6, 2024 
Verdict=Accepted
"""

  
p= -1 if input() =='R'  else 1 #position 
m=input()#message
k="qwertyuiopasdfghjkl;zxcvbnm,./"
output=""
for i in m:
    if (i!="q" and i!='/'):
        output+=k[k.index(i)+p]
    elif(i=="q"):
        output+='w' if p==1 else '/'
    elif(i=="/"):
        output+='q' if p==1 else '.'



print(output)
