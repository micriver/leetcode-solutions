"""

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""

# nums = [1, 2, 3, 1, 1, 3]
nums = [1, 1, 1, 1]
# nums = [1, 2, 3]

from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    pairs = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                pairs += 1
    return pairs


print(numIdenticalPairs(nums))

# 6 minutes	47 seconds after having done the problem once