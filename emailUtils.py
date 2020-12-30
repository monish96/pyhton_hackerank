"""
import email.utils

The \w metacharacter is used to find a word character.

A word character is a character from a-z, A-Z, 0-9, including the _ (underscore) character.

wrong regex i was using is '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

correct one '^[a-z0-9][\w\-.]*?[a-z0-9]+[@][a-zA-Z]+[.]([a-zA-Z]{1,3}$)+$'
"""
import email.utils as parser
import re


def find_valid_emails(array):
    regex = '^[a-z0-9][\w\-.]*?[a-z0-9]+[@][a-zA-Z]+[.]([a-zA-Z]{1,3}$)+$'
    for i in array:
        if re.search(regex, i[1]):
            print(parser.formataddr(i))


if __name__ == '__main__':
    emails = []
    for _ in range(0, int(input())):
        email = input()
        emails.append(parser.parseaddr(email))
    find_valid_emails(emails)
