#Set .add()
#https://www.hackerrank.com/challenges/py-set-add/problem
n=int(input())
l=[]
d=[]
s=[]
for i in range(n):
    country=input()
    l.append(country)
for i in l:
    if i not in d:
        d.append(i)
    else:
        s.append(i)
print(len(d))            
        
    
