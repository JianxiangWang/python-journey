#!/usr/bin/env python
# encoding: utf-8
import sys, random

# http://had00b.blogspot.com/2013/07/random-subset-in-mapreduce.html
#  for i in {1..100}; do echo $i; done | ./reservoir_sampling.py 3

k = int(sys.argv[1])
s, i = [], 0

for x in sys.stdin:
    if i < k:
        s.append(x)
    else:
        r = random.randint(0, i - 1)
        if r < k:
            s[r] = x
    i += 1

print ''.join(s),