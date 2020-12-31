"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

 

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
Example 3:

Input: nums = [1], index = [0]
Output: [1]
 

Constraints:

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i

the index array provides the indexes that the values from the num array have to take in the returning target array

"""
nums = [1]
index = [0]
# nums = [0, 1, 2, 3, 4]
# index = [0, 1, 2, 2, 1]
# nums = [1, 2, 3, 4, 0]
# index = [0, 1, 2, 3, 0]


def createTargetArray(nums, index):
    target = []  # empty list of ints to return

    # NO NEED TO ASSIGN VARIABLES
    # for i in range(len(nums)):
    #         val = nums[i]
    #         x = index[i]
    #         # for value in nums:
    #         #     for i in index:
    #         target.insert(x, val)

    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target


print(createTargetArray(nums, index))

# took 15:44
# https://www.tutorialspoint.com/python3/list_insert.html