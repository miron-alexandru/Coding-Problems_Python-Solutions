def arithmetic_arranger(problems, solved=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    l1 = l2 = l3 = l4 = ""
    for problem in problems:
        try:
            [operand1, operator, operand2] = problem.split()
        except ValueError:
            return "Error: Malformed problem"

        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator in "+":
            answer = str(int(operand1) + int(operand2))
        elif operator in "-":
            answer = str(int(operand1) - int(operand2))
        else:
            return "Error: unknown operator (this is a bug)"

        width = max(len(operand1), len(operand2))
        l1 += "  " + " " * (width - len(operand1)) + operand1 + "    "
        l2 += operator + " " + " " * (width - len(operand2)) + operand2 + "    "
        l3 += "-" * (width + 2) + "    "
        l4 += " " * ((width + 2) - len(answer)) + answer + "    "

    arranged_problems = l1.rstrip() + "\n" + l2.rstrip() + "\n" + l3.rstrip()

    if solved:
        arranged_problems += "\n" + l4.rstrip()

    return arranged_problems
