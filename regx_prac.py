# ''''''
# import re

# dataset = "My name is Geek and my mail address is geek@4geeksacademy.com";
# regex = r"\b[\w.!#$%&’*+\/=?^`{|}~-]+@[\w-]+(?:\.[\w-]+)*\b"

# def findEmail(term, text):
#     match = re.search(term, text)
#     return match

# print(findEmail(regex, dataset))
# #Output -> <re.Match object; span=(39, 61), match='geek@4geeksacademy.com'>'''



# import re

# # Phone Number Validator
# def validate_phone_number(phone):
#     phone_pattern = r'^(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'
#     if re.match(phone_pattern, phone):
#         return True
#     return False

# # Email Validator
# def validate_email(email):
#     email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(email_pattern, email):
#         return True
#     return False

# # Postal Code Validator
# def validate_postal_code(postal_code):
#     postal_pattern = r'^\d{5}(-\d{4})?$'
#     if re.match(postal_pattern, postal_code):
#         return True
#     return False

# def main():
#     print("Please enter your contact information:")

#     # Example phone numbers:
#     phone_examples = [
#         "(123) 456-7890", "123-456-7890", "123.456.7890",   # Valid
#         "123 456 7890", "12345-6789", "1234567890",           # Invalid
#     ]
    
#     # Example emails:
#     email_examples = [
#         "example@domain.com", "user123@xyz.org",              # Valid
#         "plainaddress.com", "@domain.com", "example@domain@com", # Invalid
#     ]
    
#     # Example postal codes:
#     postal_code_examples = [
#         "12345", "12345-6789",                                # Valid
#         "123456", "ABCDE", "1234A",                            # Invalid
#     ]
    
#     # Validate phone numbers
#     print("\nPhone Number Validation Results:")
#     for phone in phone_examples:
#         if validate_phone_number(phone):
#             print(f"{phone} is a valid phone number.")
#         else:
#             print(f"{phone} is an invalid phone number.")

#     # Validate emails
#     print("\nEmail Address Validation Results:")
#     for email in email_examples:
#         if validate_email(email):
#             print(f"{email} is a valid email address.")
#         else:
#             print(f"{email} is an invalid email address.")

#     # Validate postal codes
#     print("\nPostal Code Validation Results:")
#     for postal_code in postal_code_examples:
#         if validate_postal_code(postal_code):
#             print(f"{postal_code} is a valid postal code.")
#         else:
#             print(f"{postal_code} is an invalid postal code.")

# if __name__ == "__main__":
#     main()
 

# import re
  
# long_string = """Lorem ipsum dolor sit am__et, consectetur adipiscing elit. Proin mollis, quam vitae dapibus tincidunt, 
# libero risus egestas magna, eget auctor felis felis ac purus. 
# Vestibulum et justo nec nisi 8dictum feugiat ac ac neque. 
# Morbi tristique, sapien et luctus tristique, 
# lectus ante ullamcorper augue, ac fermentum n9unc est at ligula. 
# Aenean vitae orci 55ligula. Donec auctor, enim eget hendrerit l
# acinia, ligula dui gravida risus, nec fermentum orci libero in 
# nisi. Nunc feugiat est urna, id convallis ante auctor eget. 
# Aliquam ut orci id augue tincidunt aliquet. Nulla facilisi. 
# Nulla in enim vitae dolor cursus fermentum et sit amet metus."""

# pattern = r'\b[aA]\w*'
# r = re.findall(pattern,long_string)
# print(r)

# '''
# pattern = r'\b\w{9}\b'
# matches = re.findall(pattern, long_string)
# print(matches)
# '''

# pattern = r'[aeiouAEIOU]'
# vowels = re.findall(pattern, long_string)
# print(len(vowels))

# '''
# pattern = r'\bfermentum\b'
# matches = re.findall(pattern, long_string)
# print(matches)'''



# modified_string = re.sub(r'\bLorem\b', 'Sample', long_string)
# print(modified_string)

# # pattern = r'\b\w*\d\w*\b'
# pattern = r'\d+'
# matches = re.findall(pattern, long_string)
# print(matches)

'''

import re

unformatted_paragraph = """The quick brown fox jumped over the lazy dog. 
The fox was quick and clever, but the dog was lazy and slow. 
However, the dog knew that the fox would tire after a while. 
In the end, the fox gave up and the dog remained resting under the tree. 
Despite the fox's energetic attempts, the dog was content with its rest. 
The fox tried again, but it didn't get far. The dog was unbothered, and the fox, 
realizing the futility of its chase, sat down beside the dog. After a while, the fox and 
dog both dozed off under the shade of the tree, content in their own ways."""



pattern = r'\b\w{3}\b'
matches = re.findall(pattern, unformatted_paragraph)
print(matches)


pattern = r'\b\w+ed\b'
matches = re.findall(pattern, unformatted_paragraph)
print(matches)

pattern = r'\bfox\b'
matches = re.findall(pattern, unformatted_paragraph, re.IGNORECASE)
print(len(matches))

pattern = r'\b\w*o\w*\b'
matches = re.findall(pattern, unformatted_paragraph)
print(matches)

modified_paragraph = re.sub(r'\bdog\b', 'cat', unformatted_paragraph)
print(modified_paragraph)


'''

'''
import re
data_list = [
    "apple", 123, 45.67, "banana", True, {"key1": "value1", "key2": "value2"},
    [1, 2, 3], "orange", "grape", None, [45.67, "pie"], 89, "watermelon", False
]


# Tasks for List:
# Find all strings in the list that contain the letter "e".
# Extract all numeric values from the list, including integers and floats.
# Count how many times the word "apple" appears in the list.
# Find all boolean values (True or False) in the list.

match = r'\b[e]\b'

data = re.findall(match, data_list)
print(data)

'''
'''import re

data_list = [
    "apple", 123, 45.67, "banana", True, {"key1": "value1", "key2": "value2"},
    [1, 2, 3], "orange", "grape", None, [45.67, "pie"], 89, "watermelon", False
]

# Matching all strings that contain the letter 'e'
match = r'\b\w*e\w*\b'

# Use list comprehension to extract only strings (we ignore non-string types)
data = [item for item in data_list if isinstance(item, str) and re.search(match, item)]


print(data)

'''

import re

data_list = [
    "apple", 123, 45.67, "banana", True, {"key1": "value1", "key2": "value2"},
    [1, 2, 3], "orange", "grape", None, [45.67, "pie"], 89, "watermelon", False
]

# Task 1: Find all strings that contain the letter 'e'
match = r'\b\w*e\w*\b'
strings_with_e = [item for item in data_list if isinstance(item, str) and re.search(match, item)]
print("Strings with 'e':", strings_with_e)

# Task 2: Extract all numeric values (integers and floats)
numeric_pattern = r'\b\d+(\.\d+)?\b'
numeric_values = [item for item in data_list if isinstance(item, (int, float)) or re.match(numeric_pattern, str(item))]
print("Numeric values:", numeric_values)

# Task 3: Count how many times the word 'apple' appears in the list
apple_pattern = r'\bapple\b'
apple_count = sum(1 for item in data_list if isinstance(item, str) and re.search(apple_pattern, item))
print("Count of 'apple':", apple_count)

# Task 4: Find all boolean values (True or False)
boolean_pattern = r'\b(True|False)\b'
boolean_values = [item for item in data_list if isinstance(item, bool) or re.match(boolean_pattern, str(item))]
print("Boolean values:", boolean_values)


