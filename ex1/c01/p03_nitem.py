#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: collections.deque example
"""
from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li,previous_lines
        previous_lines.append(li)

if __name__ == "__main__":
    with open(r'../../cookbook/somefile.txt') as f:
        for pline, prevlines in search(f,'Python',5):
            print(pline,end='')
        print(pline,end='')
        print('-'*20)

