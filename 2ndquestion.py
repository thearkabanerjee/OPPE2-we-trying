# function that checks if a number is a palindrome

def palindrome_checker (words : int):
    wordsletters = str (words)
    reverseofword = wordsletters[::-1]
    if (wordsletters == reverseofword):
        return (f'{words} is a palindrome')
    else:
        return (f'{words} is not a palindrome')

print  (palindrome_checker (input ('Enter the number you want : ')))
