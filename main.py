#!/usr/bin/env python3

import sys
import parser

with open(sys.argv[1]) as f:
    instructions = parser.parse(f)
    for i in instructions:
        print(i)
