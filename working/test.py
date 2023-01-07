import re
q = "abc1ac2"
a = re.split("[0-9]", q)
print(a)
for letter in a:
    ab = re.search(".+", letter)
    print(ab)