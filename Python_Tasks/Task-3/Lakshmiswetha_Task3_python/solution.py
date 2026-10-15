## Q1. Find the Frequency of Each Word in a Sentence
def frequency_count(a):
    a=a.lower()
    a=a.split()
    
    dict={}
    l1=[]
    l2=[]
    for i in a:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)

    for i in l1:
        dict[i]=a.count(i)
    return dict 
    
## Q2. Find the Frequency of Each Character in a Word
def character_frequency(a):
    a=a.lower()
    l1=[]
    l2=[]
    dict={}
    for i in range(len(a)):
        if a[i] not in l1:
            l1.append(a[i])
        else:
            l2.append(a[i])
    for i in l1:
        dict[i]=a.count(i) 
    return dict
              
## Q3. Find the First Non-Repeating Character in a Word
def non_repeating_character(a):
    a=a.lower()
    l1=[]
    l2=[]
    for i in range(len(a)):
        if a[i] not in l1:
            l1.append(a[i])
        else:
            l2.append(a[i])
    for i in l1:
        if a.count(i)==1:
            return i
            break
               

## Q4. Check Whether Two Strings Are Anagrams
def is_anagram(a,b):
    a=a.lower()
    b=b.lower()
    if sorted(a)==sorted(b):
        return("True")
    else:
        return("False")

##  Q5. Find the First Repeating Character in a String
def first_repeating_character(a):
    a=a.lower()
    l1=[]
    l2=[]
    for i in range(len(a)):
        if a[i] not in l1:
            l1.append(a[i])
        else:
            l2.append(a[i])
    if len(l2)==0:
        return "None"
    else:
        return l2[0]

## Q6. Move All Zeros to the End of a List
def zeros_shifting(a):
    num=[]
    z=[]
    for i in a:
        if i==0:
            z.append(i)
        else:
            num.append(i)
    num.extend(z)
    return num

##  Q7. Find the Second Highest Distinct Number in a List
def second_highest(nums):
    unique_numbers = []
    for number in nums:
        if number not in unique_numbers:
            unique_numbers.append(number)
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]
 ## Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(a):
    l1=[]
    l2=[]
    for i in a:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)
    return l1
                      
 ## Find the Missing Number from 1 to N
def missing_value(a):
    for i in range(1,a[-1]+1):
        if i not in a:
            return i
 
## Q10. Find Two Numbers Whose Sum Equals a Target
def add(a):
    target=9
    num=[]
    for i in a:
        for j in range(1,len(a)):
            if a[j]+i==target:
                num.extend([i,a[j]])
    return num

## Q11. Find the Number Closest to Zero

def near_zero(a):
    nearest=a[0]
    for i in a :
        if abs(i)<abs(nearest):
            nearest=i
        elif abs(i)==abs(nearest):
            if i<0:
                continue
            else:
                neareast=i
    return nearest           
        
 ## Q12. Find Common Elements Between Two Lists
def common_element(a,b):
    common=[]
    for i in a:
        if i in b:
            common.append(i)
    return common
  
## Q13. Rotate a List to the Right by K Positions
def reverse(a):
    K=2
    first=a[:K]
    next=a[K:]
    return first+next[::-1]
               
## Q14. Find the Maximum Sum of Two Consecutive Elements

def maximum_sum(a):
    max_sum=0
    for i in range(len(a)-1):
        if a[i]+a[i+1]>max_sum:
            max_sum=a[i]+a[i+1]
    return( max_sum )
 
## Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def add(a):
    target=9
    num=[]
    nums=[]
    for i in a:
        for j in range(len(a)):
            if a[j]+i==target:
                num.append([i,a[j]])
    for i in range (len(num)):
        if num[i][::] not in nums and num[i][::-1] not in nums:
            nums.append(sorted(num[i]))
    
    return sorted(nums)        
 
    
                    
    
                                