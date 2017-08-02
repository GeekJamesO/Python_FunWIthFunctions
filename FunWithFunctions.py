# Assignment: Fun with Functions
# Create a series of functions based on the below descriptions.
#
# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop
# executes have your program print the number of that iteration and specify
# whether it's an odd or even number.
#
# Your program output should look like below:
#
# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.
def OddEven(length = 2000):
    for x in range(1, length + 1):
        oddness = "odd"
        if ((x % 2) == 0):
            oddness = "even"
        print ("Number is {0}.  This is an {1} number.".format(x, oddness))

print "Function OddEven"
OddEven()
print " "

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list
# (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been
# multiplied by 5.
#
# The function should multiply each value in the list by the second argument.
# For example, let's say:
# a = [2,4,10,16]
# Then:
# b = multiply(a, 5)
# print b
# Should print [10, 20, 50, 80 ].

def multiply (array, m=5):
    for i in range(0, len(array) ):
        array[i] *= m
    return array

print "Function Multiply"
result = multiply ([2,4,10,16], 5)
print result
print " "

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your
# new function should return the multiplied list as a two-dimensional list.
# Each internal list should contain the 1's times the number in the original
# list. Here's an example:
#
# def layered_multiples(arr):
#   # your code here
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
def layered_multiples(array):
    answer = []
    for x in array:
        thisword = []
        for i in range(0,x):
            thisword.append(1)
        answer.append(thisword)
    return answer


print "Function layered_multiples"
x = layered_multiples(multiply([2,4,5],3))
print x
