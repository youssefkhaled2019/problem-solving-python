"""
contest= https://codeforces.com/contest/263/problem/A
date=  Sunday, December 17, 2023 
Verdict  = Accepted
"""
# "000".find("1")
for _i in range (5):
    a=list(map(int,input().split(" ")))
    if (1 in a):
        i=_i
        j=a.index(1)
        break

print(abs(2-i)+abs(2-j)) 


--------------------------------


i,j=0,0

for _ in range(5):
    list_of_number=list(map(int,input().split()))  # map(int, xs)
    if (1 in list_of_number):
        i,j=_,list_of_number.index(1)
      
             
move=abs(2-i)+abs(2-j)    
print(move )
