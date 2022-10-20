# Write a Python function called max_mum() to find the maximum of three numbers

from math import factorial


def max_num(a, b, c):
    return max([a, b, c])


print(max_num(4, 5, 6))
print(max_num(1, 50, 100))
print(max_num(5, 15, 30))

# Write a Python function called mult_list() to multiply all the numbers in a list
# solution-1


def mult_list(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result

# solution-2


def mult_list(lst):
    # if empty list, return 0
    if len(lst) == 0:
        return 0
    # product starts with first element of list
    product = lst[0]

    # go through list elements and multiply then together
    if len(lst) > 1:
        for i in lst[1:]:
            product = product * i
    return product


print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([15]))

# Write a Python function called rev_string() to reverse a string.


def rev_string(my_str):
    return my_str[::-1]  # write without specifying the length of the string


print(rev_string(""))
print(rev_string("apple"))
print(rev_string("my string"))

# Write a Python function called num_within() to check whether a number falls in a given range


def num_within(x, a, b):
    # The function accepts the number, beginning of range, and end of range (inclusive) as arguments
    return x in range(a, b+1)


print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# Method 1: Using nCr formula i.e. n!/(n-r)!r!
# After using nCr formula, the pictorial representation becomes:
#           0C0
#        1C0   1C1
#     2C0   2C1   2C2
#  3C0   3C1   3C2    3C3


# write a number of rows to be printed, assume it to be n
n = 5
# make outer iteration i from 0 to n times to print the rows
for i in range(n):
    for j in range(n-i+1): # make inner iteration for j from 0 to (N-1)

        # for left spacing // print single blank space // close inner loop(j loop)
        print(end=" ")

    for j in range(i+1): # make inner iteration for j from 0 to i

        # nCr = n!/(n-r)! * r!) // Print nCr of i and j and close inner loop
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    # for new line after each inner iteration
    print()


