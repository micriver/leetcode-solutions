"""
1662. Check If Two String Arrays are Equivalent
Easy

122

20

Add to List

Share
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.

concatanate the items in the given word lists and then compare those strings returning a boolean

"""

# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
# word1 = ["a", "cb"]
# word2 = ["ab", "c"]
word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]

from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    # ORIGINAL SUBMISSION
    # w1 = "".join(word1)
    # w2 = "".join(word2)
    # return w1 == w2

    # again, you do not need to declar variables, optimize the code
    return "".join(word1) == "".join(word2)


print(arrayStringsAreEqual(word1, word2))

# took 6:49
# https://reactgo.com/python-concatenate-list/