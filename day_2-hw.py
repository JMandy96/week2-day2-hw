#Exercise 1

#Given a list as a parameter, write a function that returns a list of 
# numbers that are less than ten

#For example: Say your input parameter to the function is 
# [1, 11, 14, 5, 8, 9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

def less_than_ten(alist):
    less = []
    for num in alist:
        if num < 10:
            less.append(num)
        else:
            continue

    return less

print(less_than_ten(l_1))


#Exercise 2

#Write a function that takes in two lists and returns the two lists 
# merged together and sorted

#HINT: YOU CAN USE THE .SORT() METHOD

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def combine(l1,l2):
    l3 = []
    if l1 and l2:
        l3 = l1 + l2

    l3.sort()
    return l3
    
print(combine(l_1,l_2))
