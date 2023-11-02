import re

# Sample text with email addresses
text = """
Hello, please contact support@example.com for assistance.
You can also reach out to john.doe@emaildomain.com or jane.smith@anotherdomain.org.
"""

# Define a pattern to match email addresses
pattern = r'[\w\.-]+@[\w\.-]+'
def mask_email(match):
    email = match.group()
    username, domain = email.split('@')
    masked_username = '*' * len(username)
    return f'{masked_username}@{domain}'

# Perform the substitution using re.sub() with a custom function
masked_text = re.sub(pattern, mask_email, text)

print("\nMasked text:")
print(masked_text)
