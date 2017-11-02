class ParseError(Exception):
    pass

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

def format_error(line_number, message, value):
    return str.format('Line {}: {} {}', line_number, value, message)
