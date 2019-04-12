#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._queue+=1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


