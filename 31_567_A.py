"""
contest=https://codeforces.com/contest/567/problem/A
date=  Friday, December 29, 2023 
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split(" ")))
for i in range(n):
    if (i==0):
        mn,mx=abs(l[i]-l[1]),abs(l[i]-l[-1])
        print(mn,mx)
    elif(0<i<n-1):
        mn=min(abs(l[i]-l[i+1]) ,abs(l[i]-l[i-1]))         
        mx=max(abs(l[i]-l[0]) ,abs(l[i]-l[-1])) 
        print(mn,mx)
    else:
        mn,mx=abs(l[i]-l[i-1]),abs(l[i]-l[0])
        print(mn,mx)





#=========================solution 1 ==================================
n=int (input())
l=list(map(int, input().split()))
for i in range(n):
    
    if (i==0):#  first
        a,b=abs(l[0]-l[1]),abs(l[0]-l[-1])
        print(min(a,b),max(a,b))
    elif(i!=n-1):  
        a,b,c,d=abs(l[i]-l[0]),abs(l[i]-l[i-1]),abs(l[i]-l[i+1]),abs(l[i]-l[-1])
        
        print(min(a,min(b,min(c,d))),max(a,max(b,max(c,d))))
    elif(i==n-1):
         a,b=abs(l[i]-l[0]),abs(l[i]-l[-2])
         print(min(a,b),max(a,b))
         
     
     
            
#============================solution 2===============================  #TIME_LIMIT_EXCEEDED
#n=int (input())
#l=list(map(int, input().split()))
#for i in l:
#    tep=[]
#    for j in l :
#        if i!=j:
#            tep.extend([abs(i-j)])
#         
#    print(min(tep),max(tep))    