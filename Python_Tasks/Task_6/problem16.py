## Check Subset
## https://www.hackerrank.com/challenges/py-check-subset/problem
n=int(input())
for i in range(n):
    a=int(input())
    A=set(map(int,input().split()))
    b=int(input())
    B=set(map(int,input().split()))
    print(A.issubset(B))

