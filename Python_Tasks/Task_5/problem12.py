#Capitalize!
#https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    if (s.isalpha() == True) or (s.isalnum()==True):
        return s.title()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
