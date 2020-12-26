"""

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
	at first index, add the lone index, at second index, add the last two indexs, at the third index, add the first 3 indexes
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

length of the array will always be at least 1 but less than or equal to 1000
1 <= nums.length <= 1000
note: the numbers in the array will never be below the intmin or higher than intmax
-10^6 <= nums[i] <= 10^6

PROTOTYPE:
var runningSum = function(nums) {
    
};

Questions to ask after looking at the example input:
Can the array have negative numbers inside?

"""


nums = [3, 1, 2, 10, 1]
# Output: [3, 4, 6, 16, 17]

# https://docs.python.org/3/library/typing.html
# https://medium.com/analytics-vidhya/type-annotations-in-python-3-8-3b401384403d
from typing import List


def runningSum(
    nums: List[int],
) -> List[int]:
    sum = 0  # number to add to new list
    lst = []  # empty list to return

    for i in range(len(nums)):
        sum += nums[i]
        lst.append(sum)

    return lst


print(runningSum(nums))