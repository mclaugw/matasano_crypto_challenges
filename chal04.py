#!/usr/bin/env python

import chal03

strings = [line.rstrip('\n') for line in open('chal04_input.txt')]
all_results = []

for line in strings:
    line.strip()
    if len(line) != 60:
        strings.remove(line)

for line in strings:
    top = chal03.get_top_x_scores(line, 3)
    if(len(top) > 0):
        all_results.append([line, top])
        print "string: " + line
        print "most likely keys:"
        for i in range(len(top)):
                print " " + top[i][0] + ": ", top[i][1].strip()
        print ""
