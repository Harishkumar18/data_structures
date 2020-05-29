"""
Regex to find the email id
"""
import re


def find_all_mails():
    my_str = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com"
    emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)
    for email in emails:
        print(email)


res = find_all_mails()
