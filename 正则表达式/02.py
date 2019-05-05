import re

str_ = r'historrt,hi,him'

r = re.split(r'\bhi\b',str_)
print(r)