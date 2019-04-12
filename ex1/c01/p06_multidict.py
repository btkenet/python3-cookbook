#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from collections import defaultdict

def mul_dict():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)

    d = {} # A regular dictionary
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)


    return d


if __name__ == "__main__":
    print(mul_dict())


