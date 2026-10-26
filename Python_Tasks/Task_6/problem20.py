## Validating the Phone Number
## https://www.hackerrank.com/challenges/validating-the-phone-number/problem
n=int(input())
for i in range(n):
    A=input()
    if(A.startswith("7") or A.startswith("8") or A.startswith("9")) and (A.isdigit()==True) and len(A)==10:
        print("YES")
    else:
        print("NO")     

