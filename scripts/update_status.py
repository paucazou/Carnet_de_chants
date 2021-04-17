#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende


def update_status(filename,is_finished):
    """Update status of filename"""
    with open("finished") as f:
        content = f.read().split('\n')
    if is_finished and filename not in content:
        content.append(filename)
    elif not is_finished and filename in content:
        content.remove(filename)

    with open("finished",'w') as f:
        f.write("\n".join(content))
