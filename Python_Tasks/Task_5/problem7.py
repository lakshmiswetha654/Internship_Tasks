#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem
n=int(input())
set_A=set(map(int,input().split()))
m=int(input())
set_B=set(map(int,input().split()))
sym_diff=set_A.symmetric_difference(set_B)
for i in sorted(sym_diff):
    print(i)
