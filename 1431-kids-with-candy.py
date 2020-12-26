"""

Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: 
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]


Constraints:

2 <= candies.length <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50

Solution:

1. Identify the greatest number of candies, store in a variable
2. add the extraCandies to each num of candies in the array 
3. check if extraCandies + numCandies for each child is greater than or equal to the greatest num of candies variable
4. store result for each loop in array of true false booleans

 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
"""

candies = [2, 3, 5, 1, 3]
extraCandies = 3
# expected Output: [true,true,true,false,true]

# candies = [4, 2, 1, 1, 2]
# extraCandies = 1

# candies = [12, 1, 12]
# extraCandies = 10

from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    # create empty boolean list to return
    lst = []

    # loop through list and find greatest candy number
    highestNum = max(candies)

    for i in range(len(candies)):
        # if (candies[i] + extraCandies) >= highestNum:
        #     lst.append(True)
        # else:
        #     lst.append(False)

        # short discussion solution:
        lst.append((candies[i] + extraCandies) >= highestNum)

    return lst


print(kidsWithCandies(candies, extraCandies))