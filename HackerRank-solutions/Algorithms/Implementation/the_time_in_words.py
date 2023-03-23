# problem link: https://www.hackerrank.com/challenges/the-time-in-words/problem


# my solution: 
def timeInWords(h, m):
    numbers_to_words = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
        23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
        26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
        29: 'twenty nine', 30: 'half'
    }

    if m == 0:
        return numbers_to_words[h] + " o' clock"
    elif m == 1:
        return numbers_to_words[m] + ' minute past ' + numbers_to_words[h]
    elif m == 15 or m == 30:
        return numbers_to_words[m] + ' past ' + numbers_to_words[h]
    elif m < 30:
        return numbers_to_words[m] + ' minutes past ' + numbers_to_words[h]
    elif m == 45:
        return 'quarter to ' + numbers_to_words[h + 1]
    else:
        return numbers_to_words[60 - m] + ' minutes to ' + numbers_to_words[h + 1]
