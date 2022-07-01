import re

text = "The agent's phone number is 408-555-1234. Call soon!"
pattern = 'phone'
print(re.search(pattern, text))  # returns the first match within an object
text1 = 'my phone once, my phone twice'
print(re.findall('phone', text1))  # finds all the matches within an object
for match in re.finditer('phone', text1):  # returns all the matches within an object
    print(match)
text2 = 'My phone number is 408-555-1234'
print(re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text2))  # \d is used to search for digits
print(re.search(r'\d{3}-\d{3}-\d{4}', text2))  # returns the same as above
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(phone_pattern, text2)
print(result.group(1))
print(re.search(r'cat|dog', 'The dog is here.'))  # The symbol | stands for OR in this expression
print(re.findall(r'.at', 'The cat in the hat sat there'))  # The symbol . stands for a wildcard in this expression
print(re.findall(r'^\d', '1 is a number'))  # The symbol ^ stands for 'starts with a number' and this is meant for the whole object/string
print(re.findall(r'\d$', 'a number is 2'))  # The symbol $ stands for 'ends with a number' and this is meant for the whole object/string
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern1 = r'[^\d]'  # The symbol ^ also stands for exclude. In this case, it returns any character that isn't a digit.
pattern2 = r'[^\d]+'  # The symbol + puts the words together
print(re.findall(pattern1, phrase))
print(re.findall(pattern2, phrase))
