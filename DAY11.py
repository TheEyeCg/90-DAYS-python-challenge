#!/usr/bin/env python3

import re


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return "Valid email address."
    else:
        return "Invalid email address."

# Test cases
emails = ["example@gmail.com", "user@domain", "test.email@web.net", "invalid@com"]
for email in emails:
    print(f"{email}: {validate_email(email)}")