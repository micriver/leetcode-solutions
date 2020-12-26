"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100

Loop through the given array. for each index, loop through the array again and make a count for each number that isn't the same as the current index and is less than it. Store each result in an array to return

"""
from typing import List


# nums = [8, 1, 2, 2, 3]
nums = [6, 5, 4, 8]
# nums = [7, 7, 7, 7]


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    res = []  # create empty array to return
    smlrNums = 0

    for i in range(len(nums)):
        for j in range(len(nums)):
            # j = 0
            if nums[j] != nums[i] and nums[j] < nums[i]:
                smlrNums += 1
        res.append(smlrNums)
        smlrNums = 0
    return res


print(smallerNumbersThanCurrent(nums))

# solution 13 minutes 34 seconds