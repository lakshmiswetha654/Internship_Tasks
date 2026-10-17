#Word Order
#https://www.hackerrank.com/challenges/word-order/problem
n=int(input())
word=[]
s=[]
a=[]
for i in range(n):
    w=input()
    word.append(w)
for i in word:
    if i not in s:
        s.append(i)
    else:
        a.append(i)
c={}       
for i in s:
    c[i]=word.count(i)
            
print(len(s))
print(*(c.values()))
              
