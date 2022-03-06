
#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" read imap
https://www.thepythoncode.com/article/reading-emails-in-python

author: pengfei
copyright: Copyright 2022.03.06
email: pengfeigao2021@163.com
"""
import os
import argparse
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import re
import pdb
import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# account credentials
username = os.getenv('EUSER')
password = os.getenv('EPASS')
print(username)
print(password)

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='imap server', default='imap.qiye.aliyun.com')
    return parser.parse_args()

def read_mail(server, username, password):
    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL(server)
    # authenticate
    imap.login(username, password)

    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 3
    # total number of emails
    messages = int(messages[0])
    return messages
    

def main():
    args = parse_args()
    read_mail(args.i)
    print('done.')

if __name__ == '__main__':
    main()