"""
1221. Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

take the given balanced string and create BALANCED substrings with equal number Ls and Rs, return the number of substrings as an integer

count the Ls and then the Rs, once their sum is divisible by 2, add that substring to the count

"""
# s = "RLRRLLRLRL"
# Output: 4
# s = "RLLLLRRRLR"
# # Output: 3
# s = "LLLLRRRR"
# Output: 1
s = "RLRRRLLRLL"
Output: 2


def balancedStringSplit(s):
    res = 0
    lCount = 0
    rCount = 0
    for letter in s:
        if lCount == rCount:
            res += 1
        if letter == "L":
            lCount += 1
        elif letter == "R":
            rCount += 1
        # elif rCount == lCount + 2 or lCount == rCount + 2:
        #     lCount = 0
        #     rCount = 0
        #     res += 1

    return res
    # res = s.count("RL")


print(balancedStringSplit(s))

# luckily figured it out right at the buzzer