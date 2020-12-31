"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.

Count the number of strings where the allowed characters are consistent
if words[i][j] DOES NOT EQUAL ab[i] * n then do not increase the count to return
"""

allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
# Output: 2


def countConsistentStrings(allowed, words):
    # count = 0

    # loop through words
    # for i in range(len(words)):
    #     for j in range(len(words[i])):
    #         print(words[i][j])

    # for i in range(len(words)):
    #     for j in range(len(words[i])):
    #         # for x in range(len(allowed)):
    #         x = 0
    #         while x in range(len(allowed)):
    #             if words[i][j] == allowed[x]:
    #                 x += 1
    #                 if j == len(words[i]) - 1:
    #                     count += 1
    #             else:
    #                 i += 1
    # return count

    count = 0
    allowed = set(allowed)

    for word in words:
        for letter in word:
            if letter not in allowed:
                count += 1
                break
    # return the number of consistent strings
    return len(words) - count


# couldn't figure out a solution so decided to go with: https://leetcode.com/problems/count-the-number-of-consistent-strings/discuss/971323/Python-3-solution-100-faster-than-any-other-codes
# what is set(): https://www.geeksforgeeks.org/python-set-method/

# countConsistentStrings(allowed, words)
print(countConsistentStrings(allowed, words))