# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
a=max(arr)
num=[]    
for i in arr:
    if i!=a:
        num.append(i)   
print(max(num))             
