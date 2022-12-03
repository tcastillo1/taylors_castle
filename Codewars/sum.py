# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer.
# If the array does not contain any numbers then you should return 0.

def sum_num(num):
    if len(num) == 0:
        return 0
    else:
        return sum(x for x in num)


print(sum_num([1, 0, 3.2]))
print(sum_num([]))
