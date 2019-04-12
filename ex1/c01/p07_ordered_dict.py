#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['c'] = 2
d['b'] = 3
d['d'] = 4

for key in d:
    print(key,d[key])
