class Assembler:
    def __init__(self):
        self.symbol_table = {}
        self.intermediate_code = []

    def first_pass(self, source_code):
        location_counter = None

        for line in source_code:
            tokens = line.split()
            if tokens[0] == 'START':
                location_counter = int(tokens[1])
            elif tokens[0] == 'DS':
                self.symbol_table[tokens[1]] = location_counter
                location_counter += 1
            elif tokens[0] == 'END':
                break
            else:
                self.symbol_table[tokens[0]] = location_counter
                location_counter += 1

    def second_pass(self, source_code):
        for line in source_code:
            tokens = line.split()
            if tokens[0] == 'START':
                continue
            elif tokens[0] == 'READ':
                self.intermediate_code.append(f'READ {tokens[1]}')
            elif tokens[0] == 'MOVER':
                self.intermediate_code.append(f'MOVR {tokens[1]}, {tokens[2]}')
            elif tokens[0] == 'SUB':
                self.intermediate_code.append(f'SUB {tokens[1]}, {tokens[2]}')
            elif tokens[0] == 'STOP':
                self.intermediate_code.append('STOP')
            elif tokens[0] == 'DS' or tokens[0] == 'END':
                continue
            else:
                self.intermediate_code.append(f'L {tokens[0]}')

    def generate_intermediate_code(self, source_code):
        self.first_pass(source_code)
        self.second_pass(source_code)
        return self.intermediate_code


source_code = [
    "START 100",
    "READ A",
    "READ B",
    "		MOVER AREG, A",
    " 	SUB AREG, B",
    "STOP",
    "A		DS	1",
    "B		DS	1",
    "		END"
]

assembler = Assembler()
intermediate_code = assembler.generate_intermediate_code(source_code)

for line in intermediate_code:
    print(line)
