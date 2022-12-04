# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer.
# If the array does not contain any numbers then you should return 0.

def sum_num(num):
    return sum(num)


print(sum_num([1, 0, 3.2]))

# interesting that the sum function returns 0 if the list is empty. Why is that?
print(sum_num([]))
