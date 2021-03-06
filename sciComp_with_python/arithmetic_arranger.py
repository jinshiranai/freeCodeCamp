#!usr/bin/python3
# FCC Scientific Computing with Python Project 1: Arithmetic Arranger.

def arithmetic_arranger(problems, solution=False):
    top_line_nums = []
    operators = []
    mid_line_nums = []
    mid_lines = []
    lines = []
    answers = []
    
    # If more than 5 problems, return error.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Break the strings into 3 parts.
    for problem in problems:
        split_problem = problem.split()

        # If operand length is greater than 4, return size error.
        if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            # Convert string numbers to int values.
            # Return error if text instead of digits.
            try:
                int(split_problem[0])
                int(split_problem[2])
            except ValueError:
                return "Error: Numbers must only contain digits."
            else:
                top_line_nums.append(split_problem[0])
                mid_line_nums.append(split_problem[2])

        # Check operators, return error if not + or -.
        if split_problem[1] == '+' or split_problem[1] == '-':
            operators.append(split_problem[1])
        else:
            return "Error: Operator must be '+' or '-'."
        
        # Get the answers.
        if split_problem[1] == '+':
            answers.append(str(int(split_problem[0]) + int(split_problem[2])))
        else:
            answers.append(str(int(split_problem[0]) - int(split_problem[2])))

    # Concatenate operators and bottom operands.
    for value in range(len(operators)):
        mid_lines.append(operators[value] + ' ' + str(mid_line_nums[value]))

    # Compare top line and bottom line length.
    # Adjust smaller with white space until equal with larger.
    for value in range(len(top_line_nums)):
        #while len(top_line_nums[value]) != len(mid_lines[value]):
        if len(top_line_nums[value])+1 == len(mid_lines[value]):
            while len(top_line_nums[value]) != len(mid_lines[value]):
                top_line_nums[value] = '  ' + top_line_nums[value]
                mid_lines[value] = (mid_lines[value][0] + ' ' *
                    (len(top_line_nums[value]) - 1 - len(mid_lines[value][2:]))
                    + mid_lines[value][2:])
        elif len(top_line_nums[value]) < len(mid_lines[value]):
            while len(top_line_nums[value]) != len(mid_lines[value]):
                top_line_nums[value] = ' ' + top_line_nums[value]
        elif len(top_line_nums[value]) > len(mid_lines[value]):
            while len(top_line_nums[value]) != len(mid_lines[value]):
                top_line_nums[value] = '  ' + top_line_nums[value]
                mid_lines[value] = (mid_lines[value][0] + ' ' *
                    (len(top_line_nums[value]) - 1 - len(mid_lines[value][2:]))
                    + mid_lines[value][2:])
            
        # Format answers.
        if solution:
            while len(top_line_nums[value]) != len(answers[value]):
                answers[value] = ' ' + answers[value]

        # Create dashed line equal to problem length.
        lines.append('-' * len(top_line_nums[value]))
    
    # Format arranged problems for return.
    top_line = ''
    mid_line = ''
    line_line = ''
    answer_line = ''

    for item in top_line_nums:
        top_line = top_line + '    ' + item
    top_line = top_line[4:]

    for item in mid_lines:
        mid_line = mid_line + '    ' + item
    mid_line = mid_line.strip()

    for item in lines:
        line_line = line_line + '    ' + item
    line_line = line_line.strip()

    if solution:
        for item in answers:
            answer_line = answer_line + '    ' + item
        answer_line = answer_line[4:]

    arranged_problems = top_line + '\n' + mid_line + '\n' + line_line
    if solution:
        arranged_problems = arranged_problems + '\n' + answer_line

    return arranged_problems

problems = ['50 - 34', '2345 + 6', '70 + 1001', '420 + 69', '42 - 0']

print(arithmetic_arranger(problems, True))