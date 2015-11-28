#!/usr/bin/python

import re
import operator
import sys

if len(sys.argv) != 4:
  print 'Usage: edgelist2adjlist.py [infile] [outfile] [num_nodes]'
  sys.exit(-1)

infile = sys.argv[1]
outfile = sys.argv[2]
num_nodes = int(sys.argv[3])

print 'Reading ' + infile
print 'Writing ' + outfile
print 'Expecting ' + str(num_nodes) + ' nodes, consecutively numbered starting from 0'

nodes = {}
with open(infile) as fp:
  for line in fp:
    if line.startswith('#'):
      continue
    arr = re.split('\s+', line.rstrip())
    src = int(arr[0])
    dest = int(arr[1])
    #print src, dest
    if nodes.has_key(src):
      nodes[src].append(dest)
    else:
      nodes[src] = [dest]

with open(outfile, 'w') as f:
  for i in range(0, num_nodes):
    if nodes.has_key(i):
      f.write(str(i) + '\t' + '\t'.join(str(n) for n in nodes[i]) + "\n")
    else:
      f.write(str(i) + '\n')
