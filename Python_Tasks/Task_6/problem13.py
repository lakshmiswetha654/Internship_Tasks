## Set .union() Operation
## https://www.hackerrank.com/challenges/py-set-union/problem
n=int(input())
A=set(map(int,input().split()))
N=int(input())
B=set(map(int,input().split()))
print(len(A.union (B)))
