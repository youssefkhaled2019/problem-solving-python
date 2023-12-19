"""
contest=  https://codeforces.com/contest/59/problem/A
date= Tuesday, December 19, 2023
Verdict  = Accepted
"""
s=input()
l,u=0,0 #l=lower,upper
for i in s :
    if ("A"<=i<="Z"):
        u+=1
    else:
         l+=1

if(l<u):
  print(s.upper())  
else:
  print(s.lower())
  

---------------------------------------

#word=list(input())
#a,l=0,0
#for i in range(len(word)):                  #65 A   -   90 Z 
#   if ( ord(word[i])<ord("a")):             #a=97  - z =122
#       a+=1
#   else:
#       l+=1
#    
#if (a>l ):
#    
#    print("".join(word).upper()  )
#else:
#    print("".join(word).lower()  )
#
#


#s=input();print([s.lower(),s.upper()][sum(x<'['for x in s)*2>len(s)])
