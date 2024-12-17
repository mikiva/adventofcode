
def test():
    ex = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

    run(ex)



def run(input: str):

    a,b,c,_,p = input.split("\n")
    
    a = int(a.split(": ")[1])
    b = int(b.split(": ")[1])
    c = int(c.split(": ")[1])
    program = [int(r) for r in p.split(": ")[1].split(",")]
    
    register = Register(a,b,c)
    
    part1(program, register)
    print("1: ", ",".join([str(o) for o in register.Output]))

class Register:
    A: int
    B: int
    C: int
    Instruction: int = 0
    Output: list = []
    def __init__(self, a, b , c):
        self.A = a
        self.B = b
        self.C = c
        self.Output = []
        self.Instruction = 0

    def __str__(self):
        return 'A: {self.A}\nB: {self.B}\nC: {self.C}'

    def get_value(self, operand):
        match operand:
            case 4: value = self.A
            case 5: value = self.B
            case 6: value = self.C
            case _: value = operand

        return value

def adv(operand, register: Register):
    
    numerator = register.A
    denominator: int = register.get_value(operand)

    result = numerator // (2**denominator)
    register.A = result

def bxl(operand, register: Register):
    b = register.B
    result = operand ^ b
    register.B = result


def bst(operand, register: Register):
    res = register.get_value(operand) % 8
    register.B =res

def jnz(operand, register: Register):
    if register.A == 0:
        return
    return operand

def bxc(_, register: Register):
    b,c = register.B, register.C
    result = b ^ c
    register.B = result

def out(operand, register: Register):
    value = register.get_value(operand) % 8
    register.Output.append(value)

def bdv(operand, register: Register):
    numerator = register.A
    denominator: int = register.get_value(operand)
    result = numerator // (2**denominator)
    register.B = result

def cdv(operand, register: Register):
    numerator = register.A
    denominator: int = register.get_value(operand)
    result = numerator // (2**denominator)
    register.C = result


def part1(program, register: Register):
    operations = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    register.Instruction = 0
    while register.Instruction < len(program):
        opcode = program[register.Instruction]
        operand = program[register.Instruction+1]
        instr = operations[opcode](operand, register)

        if instr is not None:
            register.Instruction = instr
        else:
            register.Instruction += 2
    return register.Output
    