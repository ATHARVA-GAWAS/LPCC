def generate_literal_table(source_code):
    literal_table = {}
    literal_count = 0
    lines = source_code.split('\n')

    for line in lines:
        if line.strip() == '' or line.strip().startswith('//'):
            continue
        tokens = line.split()
        if len(tokens) >= 3:
            if tokens[1] == 'DS' or tokens[1] == 'DC':
                continue
            if tokens[2].startswith('='):
                literal = tokens[2][2:-1]  # Remove leading = and trailing '
                if literal not in literal_table.values():
                    literal_table[f'L{literal_count}'] = literal
                    literal_count += 1

    return literal_table

source_code = """
    START 100
READ A
    READ B
MOVER AREG, ='50'
    MOVER BREG, ='60'
        ADD AREG, BREG
LOOP    MOVER CREG, A
    ADD CREG, ='10'
COMP CREG, B
    BC LT, LOOP
NEXT    SUB AREG, ='10'
COMP AREG, B
BC GT, NEXT
STOP
A        DS 1
B        DS 1
END
"""

literal_table = generate_literal_table(source_code)
print("Literal Table:")
print("Literal\tValue")
for literal, value in literal_table.items():
    print(f"{literal}\t{value}")
