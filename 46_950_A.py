"""
contest=https://codeforces.com/contest/950/problem/A
date= Wednesday, February 28, 2024 
Verdict =Accepted
"""




a,b,c=map(int,input().split());
print(2*min(a+c,b+c,(a+b+c)//2))


"""
l,r,a=map(int,input().split(" "))

for i in range(a):
    if(l<r):
        l+=1
    elif(r<l):
         r+=1
    else:
        l+=1
       
print(min(l,r)*2)

"""