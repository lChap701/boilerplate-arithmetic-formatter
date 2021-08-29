import re


def arithmetic_arranger(problems, answer=False):
    """
    Rearranges expression and solves them (based on the value of the second argument)

    Args:
        problems (list):         Represents a list of Math problems.
        answer (bool, optional): Determines if the answer to the problem should be displayed.

    Returns:
        str: Returns the formatted version of the problem with the answer (if applicable)
    """
    first = []
    second = []
    third = []
    fourth = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for pb in problems:
        nums = re.split("\D+", pb)
        op = re.split("\s?\d+\s?", pb)[1]
        leng = 0
        secStr = ""

        if len(str(nums[1])) > len(str(nums[0])):
            leng = len(op + " " + nums[1])
            secStr = op + " " + nums[1]
        elif len(str(nums[0])) > len(str(nums[1])):
            leng = len(str(nums[0])) + 2
            
            if (len(str(nums[0])) - 2) > 1:
                secStr = op + " "*(len(str(nums[0]))) + nums[1]
            else:
                secStr = op + "  " + nums[1]
        else:
            leng = len(str(nums[0])) + 2
            secStr = op + " " + nums[1]
        if op != "-" and op != "+":
            return "Error: Operator must be '+' or '-'."

        if len(str(nums[1])) > 4 or len(str(nums[0])) > 4:
            return "Error: Numbers cannot be more than four digits."

        if re.search("[A-Za-z]", pb):
            return "Error: Numbers must only contain digits."

        first.append(str(nums[0]).rjust(leng, " "))
        second.append(secStr.rjust(leng, " "))
        third.append(("-"*leng).rjust(leng, " "))

        if answer:
            ans = str(eval(pb))
            fourth.append(ans.rjust(leng, " "))

    prob = str.join(" "*4, first) + "\n" + str.join(" "*4,
                                                    second) + "\n" + str.join(" "*4, third)

    if answer:
        return prob + "\n" + str.join(" "*4, fourth)

    return prob
