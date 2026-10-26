## Set .difference() Operation
## https://www.hackerrank.com/challenges/py-set-difference-operation/problem
n=int(input())
A=set(map(int,input().split()))
N=int(input())
B=set(map(int,input().split()))
print(len(A.difference(B)))
