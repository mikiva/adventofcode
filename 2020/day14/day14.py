from itertools import product

def read_input(filename):
    data = open(filename).read().split("\n")
    return data

def value_plus_mask(val, mask):
    val = [x for x in str(val)]
    for idx, m in enumerate(mask):
        if m != "X":
            val[idx] = m
    val = "".join(val)

    return val

def count_program(program):
    count = 0
    for v, k in program.items():
        count += int(k, 2)
    return count

def set_address_value(prog, bit_address,p, value):
    bits = bit_address.copy()
    idx = 0
    for i in range(len(bit_address)):
        if bits[i] == "X":
            bits[i] = p[idx]
            idx += 1
    addr = int("".join(bits), 2)
    prog[addr] = value

def run_program(program, part2=False):
    prog = {}
    mask = ""
    for line in program:
        p = line.split()
        if line.startswith("mask"):
            mask = p[2]
        elif line.startswith("mem") and part2:
            assert(mask != "")
            address = int(p[0][p[0].index("[") + 1:p[0].index("]")])
            value = "%036d" % int(bin(int(p[2]))[2:])
            bit_address = list("%036d" % int(bin(address)[2:]))
            xcount = 0
            for i in range(len(bit_address)):
                if mask[i] == "1":
                    bit_address[i] = mask[i]
                elif mask[i] == "X":
                    bit_address[i] = mask[i]
                    xcount += 1
            permutations = product(("1", "0"), repeat=xcount)
            for p in permutations:  
                set_address_value(prog, bit_address,p, value)
        else:
            assert(mask != "")
            key, value = line.replace(" ", "").split("=")
            value = "%036d" % int(bin(int(value))[2:])
            value = value_plus_mask(value, mask)
            prog[key] = value


    return prog

def solve(filename):
    program = read_input(filename)
    print(f'A: {count_program(run_program(program))}')
    print(f'B: {count_program(run_program(program,True))}')

if __name__ == "__main__":
    solve("input.txt")
