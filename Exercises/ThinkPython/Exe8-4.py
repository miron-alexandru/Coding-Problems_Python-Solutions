def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


print(any_lowercase1("Banana"))  # Returns False only when first letter is uppercase.


def any_lowercase2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"


print(any_lowercase2("banana"))  # Always returns  True (also True is str not bool)


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


print(any_lowercase3("bananA"))  # Returns false only when last letter is uppercase.


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


print(any_lowercase4("BANANA"))  # Returns false only when whole word is in uppercase.


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


print(any_lowercase5("banana"))  # Returns flase when any letter is uppercase.
