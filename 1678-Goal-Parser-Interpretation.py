"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.

"""

# command = "(al)G(al)()()G"
# Output: "alGalooG"
command = "G()()()()(al)"
# Output: "Gooooal"
# command = "G()(al)"
# Output: "Goal"


def interpret(str):
    res = ""  # was returning a list instead of a string
    for i in range(len(command)):
        if command[i] == "G":
            res += "G"
        elif command[i] == "(" and command[i + 1] == ")":
            res += "o"
            i += 2
        elif command[i] == "a" and command[i + 1] == "l":
            res += "al"
            i += 2
    return res


print(interpret(command))

# managed to figure out my bug at 20:00 minutes

"""
BETTER SOLUTION

REPLACE METHOD

return command.replace('()','o').replace('(al)','al')

loop through the string and literally replace the char sequences with the chars to be returned. Really easy to just use replace
"""