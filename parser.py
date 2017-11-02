# Parses Hack assembly text

import core, code
import symbol_table as symbols
from core import AInstruction, CInstruction, ParseError

STARTING_VAR_ADDR = 16

def __parse_a(line_number, line, var_addr):
    _,  symbol = line.split('@')

    addr = 0
    if symbol in symbols.PREDEFINED_SYMBOLS:
        addr = symbols.PREDEFINED_SYMBOLS[symbol]
    elif symbol in symbols.USER_SYMBOLS:
        addr = symbols.USER_SYMBOLS[symbol]
    elif symbol.isdigit():
        addr = int(symbol)
    else:
        addr = var_addr
        symbols.USER_SYMBOLS[symbol] = var_addr
        var_addr += 1

    #TODO: check for upper address limit
    return var_addr, AInstruction(addr)

def __parse_c(line_number, line):
    line = ''.join(line.split()) #remove all whitespace

    comp = line
    dest = None
    if '=' in comp:
        dest, comp = line.split('=')
        if dest not in code.C_DEST.keys():
            raise ParseError(core.format_error(line_number, 'is not a valid destination', dest))

    jmp = None
    if ';' in comp:
        comp, jmp = comp.split(';')
        if jmp not in code.C_JUMP.keys():
            raise ParseError(core.format_error(line_number, 'is not a valid jump operation', jump))

    if comp not in code.C_COMP.keys():
        raise ParseError(core.format_error(line_number, 'is not a valid operation', comp))

    return CInstruction(dest, comp, jmp)

def __clean_and_add_labels(text):
    instructions = []
    line_number = 0
    prog_cnt = 0

    for line in text:
        line_number += 1
        line = line.strip()
        if not line:
            continue
        elif line.startswith('//'):
            continue
        else:
            if '//' in line:
                line, comment = line.split('//')

            line = line.strip()
            # TODO: error check for mismatched parens
            if line.startswith('(') and line.endswith(')'):
                label = line[line.index('(') + 1:line.rindex(')')]
                symbols.add_label(prog_cnt, label)
            else:
                instructions.append((line_number,line))
                prog_cnt += 1
    return instructions

def __create_instructions(lines):
    instructions = []
    var_addr = STARTING_VAR_ADDR
    for line_no, line in lines:
        if line.startswith('@'):
            var_addr, ins = __parse_a(line_no, line, var_addr)
            instructions.append(ins)
        else:
            instructions.append(__parse_c(line_no, line))
    return instructions

def parse(text):
    line_number = 0

    pass1 = __clean_and_add_labels(text)
    pass2 = __create_instructions(pass1)

    return pass2
