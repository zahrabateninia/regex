import re
result = re.search(r"^(\w*), (\w*)$", "Bateninia, Zahra")
print(result.groups()) # prints a tuple
print(result)
print(result[0])
print(result[1])
fullname = "{} {}".format(result[2], result[1])
print(fullname)