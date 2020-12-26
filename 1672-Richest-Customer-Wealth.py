"""

find the wealthiest customer by adding all the wealth from all their bank accounts

find sum of customers in given 2d array of accounts

"""

from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    wealth = 0
    # loop through the account of each customer
    for i in range(len(accounts)):
        # when on a customer, find sum of their integer array (their accounts)
        if sum(accounts[i]) >= wealth:
            wealth = sum(accounts[i])
    return wealth


accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
# accounts = [[1, 5], [7, 3], [3, 5]]
# accounts = [[1, 2, 3], [3, 2, 1]]

print(maximumWealth(accounts))

# solution 17 minutes 38 seconds