# problem link: https://www.hackerrank.com/challenges/strong-password/problem


# my solution:
def minimumNumber(n, password):
    requiredCriteria = 0

    if not any(char.isdigit() for char in password):
        requiredCriteria += 1
    if not any(char.islower() for char in password):
        requiredCriteria += 1
    if not any(char.isupper() for char in password):
        requiredCriteria += 1
    if not any(char in "!@#$%^&*()-+" for char in password):
        requiredCriteria += 1

    missingLength = max(6 - n, 0)

    return max(requiredCriteria, missingLength)