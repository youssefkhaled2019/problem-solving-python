"""
contest=  https://codeforces.com/contest/490/problem/A 
date=Tuesday, December 26, 2023
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split(" ")))
l_1,l_2,l_3=[],[],[]
for i in range(n):
    if (l[i]==1):
         l_1.extend([i+1])
    elif (l[i]==2):
         l_2.extend([i+1])
    elif (l[i]==3):
         l_3.extend([i+1])  
s_1,s_2,s_3=len(l_1),len(l_2),len(l_3)                 
print(min(s_1,min(s_2,s_3)))
for i,j,k in zip(l_1,l_2,l_3):
    print(i,j,k)




------------------------------------------------------------
#https://www.youtube.com/watch?v=uc5HeMl4poA
#---------------python-----------------------------
n=int(input())
number=[[],[],[]]
for indx,v in enumerate(input().split(),1):number[int(v)-1]+=[indx]
print(min(map(len,number)))#[[1, 3, 6], [5, 7], [2, 4]] ->[3,2,2]->2 
for i in zip(*number):print(*i)
    
"""
for i in zip(number):print(i)
([1, 3, 6],)
([5, 7],)
([2, 4],)
for i in zip(*number):print(i)
(1, 5, 2)
(3, 7, 4)
for i in zip(number):print(*i)
[1, 3, 6]
[5, 7]
[2, 4]
for i in zip(*number):print(*i)
1 5 2
3 7 4

-----------------------

1) x, y =            [1, 2, 3] ['a', 'b', 'c', 'd']
2) zip(x, y) =       [(1, 'a'), (2, 'b'), (3, 'c')]
3) *zip(x, y) =       (1, 'a')  (2, 'b')  (3, 'c')
4) zip(*zip(x,y)) =  [(1, 2, 3), ('a', 'b', 'c')]
"""
#=========================================================================================
#-----------------c++----------------------------
##include <iostream>
#using namespace std;
#int a, b, mas[4][5001], ma[4], ans;
#int main() {
#    cin >> a;
#    for (int i = 1; i <= a; i++) {
#        cin >> b;
#        mas[b][ma[b]++] = i;
#    }
#    ans = min(ma[1], min(ma[2], ma[3]));
#    cout << ans << endl;
#    for (int i = 0; i < ans; i++) {
#        cout << mas[1][i] << " " << mas[2][i] << " " << mas[3][i] << endl;
#    }
#}
#=========================================================================================
