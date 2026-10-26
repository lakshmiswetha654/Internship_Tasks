## Set .discard(), .remove() & .pop()
## https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n=int(input())
s=set(map(int,input().split()))
a=int(input())
for i in range(a):
    command=input().split()
    comand_part=command[0]
    if comand_part=="pop":
        s.pop()
    elif comand_part=="remove":
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass
    elif comand_part=="discard":
        s.discard(int(command[1]))
print(sum(s))
