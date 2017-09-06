print "Odd/Even:"
print "Create a function called odd_even that counts from 1 to 2000. As your loop executes have your "
print "program print the number of that iteration and specify whether it's an odd or even number."
def OddEven():
    for aNum in range (1, 2000 + 1, 1):
        if (aNum % 2 == 0):
            print "Number is {}.  This is an even number.".format(aNum)
        else:
            print "Number is {}.  This is an odd number.".format(aNum)
OddEven()

print "Multiply:"
print "Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) "
print "and returns a list where each value has been multiplied by 5."
print "The function should multiply each value in the list by the second argument. For example, let's say:"
print "a = [2,4,10,16]"
print "Then:"
print "    b = multiply(a, 5)"
print "    print b"
print "Should print [10, 20, 50, 80 ]."
def multiply(list, multiplier):
    for index in range(0, len(list)):
        list[index] *= multiplier
    return list

a = [2,4,10,16]
b = multiply(a, 5)
print "Actual Value", b

" "
print "Hacker Challenge:"
print "Write a function that takes the multiply function call as an argument. "
print "Your new function should return the multiplied list as a two-dimensional list. "
print "Each internal list should contain the 1's times the number in the original list. "

def layered_multiples(arr):
    print "Input array:", arr
    returnList = []
    for anInt in arr:
        templist = [1] * anInt
        returnList.append(templist)
    return returnList

x = layered_multiples(multiply([2,4,5],3))
print "Expected Output: [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]"
print "Actual Output:  ",x
# output
