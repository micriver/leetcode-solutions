"""
You're given strings 'jewels' representing the types of stones that are jewels, and 'stones' representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

find the jewels in the given stones string, count how many are stones 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""

# jewels = "aA"
# stones = "aAAbbbb"
# Output: 3

jewels = "z"
stones = "ZZ"
# Output: 0


def numJewelsInStones(jewels, stones):
    # counter to return number of jewels
    count = 0
    # loop through jewels one letter at a time
    for i in range(len(jewels)):
        # loop through stones one letter at a time, counting how many times the current char in jewel appears in stones
        for j in range(len(stones)):
            if jewels[i] == stones[j]:
                count += 1

    return count


print(numJewelsInStones(jewels, stones))

# passed 10 minutes	43 seconds