## Check Strict Superset
## https://www.hackerrank.com/challenges/py-check-strict-superset/problem
A=set(map(int,input().split()))
N=int(input())
B=set(map(int,input().split()))
C=set(map(int,input().split()))
print(A.issuperset(B) and A.issuperset(C))

