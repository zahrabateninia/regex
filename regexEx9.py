#!/usr/bin/env python3
import re

even_a_regex = r'(b*ab*a)*'
odd_b_regex = r'a*ba*(ba*ba*)*'

combined_regex = f'({even_a_regex})|({odd_b_regex})'

def check_string(s):

    if re.fullmatch(combined_regex, s):
        return True
    return False

# Test cases
test_strings = [
    "aab",   # Even number of 'a'
    "bbb",   # Odd number of 'b'
    "aaabb", # Even number of 'a', odd number of 'b'
    "bba",   # Odd number of 'b'
    "abab",  # Neither condition met
    ""       # Empty string (satisfies both conditions)
]

for test in test_strings:
    result = check_string(test)
    print(f"String '{test}' matches the condition: {result}")


# Note to myself:
#  Since we are using an OR operator (|) in the regular expression,
#  a string that satisfies either condition will match, but if a string satisfies both conditions (like 'aabbb'), it will still match. 