#Nested Lists
#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    scores=[]
    for i in students:
        scores.append(i[1])
    s=min(scores)
    a=[]
    for i in scores:
        if i!=s:
            a.append(i)
    names=[]       
    for i in students:
        if i[1]==min(a):
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)                     

