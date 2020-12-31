"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
Example 2:

Input: nums = [1,1,2,3]
Output: [1,3,3]

return a concatenated list of all the pairs' values in their frequencies

"""
# nums = [1, 1, 2, 3]
nums = [1, 2, 3, 4]

# def decompressRLElist(nums):
#     # concatenated list to return
#     res = []
#     freq = 0
#     val = 0
#     i = 0
#     # loop through the list
#     for i in range(len(nums)) and nums[2 * i] < len(nums):
#         # identify freq and val
#         # if nums[2 * i] == len(nums):
#         #     break
#         # elif nums[2 * i] != len(nums):
#         freq = nums[2 * i]
#         val = nums[2 * i + 1]
#         print("frequency is: ", freq)
#         print("value is: ", val)

# couldn't get past error of going over list, learned more about the range function in python3
# https://ssiddique.info/indexerror-list-index-out-of-range-python.html


def decompressRLElist(nums):
    res = []  # empty list to return
    for i in range(
        0, len(nums), 2
    ):  # iterate from 1st number in nums to the last number by two at a time
        res += [nums[i + 1]] * nums[i]  # add value times the frequency to the list
    return res


print(decompressRLElist(nums))