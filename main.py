#!/usr/bin/env python3

import sys, os, parser, code

filename, ext = os.path.splitext(sys.argv[1])

if ext != '.asm':
    sys.exit('Input file must use the .asm extension')

out_filename = filename + '.hack'

with open(sys.argv[1]) as inp, open(out_filename, 'w') as out:
    instructions = parser.parse(inp)
    binary = code.to_binary(instructions)
    for b in binary:
        out.write(b + '\n')
