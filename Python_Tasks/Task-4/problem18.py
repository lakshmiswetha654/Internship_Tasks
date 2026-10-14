##Lists
##https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
list=[]
for i in range(N):
    operation=input().split()
    command=operation[0]
    if command=="insert":
        index=int(operation[1])
        value=int(operation[2])
        list.insert(index,value)
    elif command=="print":
        print(list)
    elif command=="remove":
        value=int(operation[1])
        list.remove(value) 
    elif command=="append":
        value=int(operation[1])
        list.append(value)
    elif command=="sort":
        list.sort()
    elif command=="pop":
        list.pop()
    elif command=='reverse':
        list.reverse()           
        
    
    
    

