# Maps parsed tokens into machine code

class AInstruction:
    def __init__(self, addr):
        self.address = addr

    def __str__(self):
        return str.format('@{}', self.address)

class CInstruction:
    def __init__(self, dest, comp, jump):
        self.dest = dest
        self.comp = comp
        self.jump = jump

    def __str__(self):
        text = self.comp
        if self.dest:
            text = self.dest + '=' + text
        if self.jump:
            text = text + ';' + self.jump
        return text


C_DEST = {
    'null' : '000',
    'M' : '001',
    'D': '010',
    'MD' : '011',
    'A' : '100',
    'AM' : '101',
    'AD' : '110',
    'AMD' : '111'
}

C_COMP = {
    '0' : '0101010',
    '1' : '0111111',
    '-1' : '0111010',
    'D' : '0001100',
    'A' : '0110000',
    'M' : '1110000',
    '!D' : '0001101',
    '!A' : '0110001',
    '!M' : '1110001',
    '-D' : '0001111',
    '-A' : '0110011',
    '-M' : '1110011',
    'D+1' : '0011111',
    'A+1' : '0110111',
    'M+1' : '1110111',
    'D-1' : '0001110',
    'A-1' : '0110010',
    'M-1' : '1110010',
    'D+A' : '0000010',
    'D+M' : '1000010',
    'D-A' : '0010011',
    'D-M' : '1010011',
    'A-D' : '0000111',
    'M-D' : '1000111',
    'D&A' : '0000000',
    'D&M' : '1000000',
    'D|A' : '0010101',
    'D|M' : '1010101'
}

C_JUMP = {
    'null' : '000',
    'JGT' : '001',
    'JEQ': '010',
    'JGE' : '011',
    'JLT' : '100',
    'JNE' : '101',
    'JLE' : '110',
    'JMP' : '111',
}

MAX_BITS = 16

def __convert_a(i):
    binary = str(bin(i.address))[2:]
    return binary.zfill(16)

def __convert_c(i):
    comp = C_COMP[i.comp]
    dest = C_DEST[i.dest] if i.dest else C_DEST['null']
    jump = C_JUMP[i.jump] if i.jump else C_JUMP['null']
    return str.format('111{}{}{}', comp, dest, jump)

def to_binary(instructions):
    result = []
    for i in instructions:
        if type(i) is AInstruction:
            result.append(__convert_a(i))
        elif type(i) is CInstruction:
            result.append(__convert_c(i))
    return result
