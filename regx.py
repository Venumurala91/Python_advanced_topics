''' '
''import re

string = """Hello my Number 89 and
          my friend's number is 987654321"""
regex = '\d+'

match = re.findall(regex, string)
print(match)
'''
'''
import re

s = 'GeeksforGeeks: A computer science portal for geeks'

match = re.search(r'portal', s)
print(s.index('portal'))
print('Start Index:', match.start())
print('End Index:', match.end())
'''
'''
import re

# Example 2: Check for a digit in the string
pattern = r"\d"
text = "My phone number is 1234"
match = re.search(pattern, text)


if match:
    print("Digit found!")
else:
    print("No digit found!")'''

'''import re

pattern = r"\d{3}"
text = "My code is 12345"
match = re.search(pattern, text)

if match:
    print("3 digits found:", match.group())
else:
    print("No match found!")

'''

'''
re.split(pattern, string, maxsplit=0, flags=0)


import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

'''

'''# Example 4: Match "cat" or "dog"
pattern = r"cat|dog"
text = "I have a dog"
match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found!")

'''




'''
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)


print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))
'''''
'''
import re

def is_allowed_specific_char(string):
    # Check if the string contains any non-alphanumeric character
    if re.search(r'[^a-zA-Z0-9]', string):
        return False  # Return False if there's any non-alphanumeric character
    return True  # Return True if all characters are alphanumeric

# Test cases
print(is_allowed_specific_char("ABCDEFabcdef123450"))  # Should return True
print(is_allowed_specific_char("*&%@#!}{"))  # Should return False

'''
'''
import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))

import re
def text_match(text):
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("abbb"))
print(text_match("aabbbbbc"))
'''
'''
import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))

''''''

import re

sample_text = "The quick brown fox jumps over the lazy dog"
x = re.search("quick",sample_text)
print(type(x))
if x:
    print(True)
else:
    print(False)
    
    '''






