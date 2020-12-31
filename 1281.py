"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5

find product of digits, then find the sum of the digits, then subtract sum from the product

"""


def subtractProductAndSum(n):
    temp = n
    product = 1
    while temp != 0:
        # return the last most digit, multiply and store the result into the variable product.
        product = product * (temp % 10)
        # Remove that last digit from temp with FLOORED division
        temp = temp // 10

    Sum = 0
    temp = n
    while temp > 0:
        # get last digit and add to the sum
        Sum = Sum + (temp % 10)
        # Remove that last digit from temp with FLOORED division
        temp = temp // 10

    return product - Sum


n = 234
# output = 15
# n = 4421
print(subtractProductAndSum(n))


# product: https://studyfied.com/program/python-basic/find-product-of-digits-of-a-number/
# sum: https://www.tutorialgateway.org/python-program-to-find-sum-of-digits-of-a-number/


# completed at the buzzer!