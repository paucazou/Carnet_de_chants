#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

"""Add non breaking space when necessary
"""
import re

def add_non_breaking_space_for(file_name):
    with open(file_name) as f:
        content = f.read()

    content = add_non_breaking_space(content)
    with open(file_name,'w') as f:
        f.write(content)

def add_non_breaking_space(data: str) -> str:
    """
    data = re.sub(r'(?<! ):',' :',data)
    data = re.sub(r'(?<! )!',' !',data)
    data = re.sub(r'(?<! )\?',' ?',data)
    data = re.sub(r'(?<! );',' ;',data)
    return data
    """

    chars = "! \? ; :".split()
    for c in chars:
        regex = r'(?<! )'+c
        replacement = r' '+c
        data = re.sub(regex, replacement, data)

    return data


