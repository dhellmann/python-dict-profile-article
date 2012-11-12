#!/usr/bin/env python

import sys
import timeit

reps = 5
iterations = 1000000

for input in sys.argv[1:]:
    src = open(input, 'r').readlines()
    if len(src) > 1:
        setup = src[0]
        to_time = ''.join(src[1:])
    else:
        setup = ''
        to_time = src[0]
    t = timeit.Timer(to_time, setup)
    print to_time
    print sum(t.repeat(reps, iterations)) / reps
    print
