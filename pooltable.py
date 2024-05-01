def generate_pool_table(source_code):
    pool_table = []

    # Split the source code into lines
    lines = source_code.split('\n')

    # Initialize the location counter
    location_counter = None

    # Iterate through each line of code
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue

        # Split the line into tokens
        tokens = line.split()

        # Check if the line starts with a label
        if tokens[0][-1] == ':':
            label = tokens[0][:-1]
            tokens = tokens[1:]
        else:
            label = None

        # If START directive is found, set the location counter
        if tokens[0] == 'START':
            location_counter = int(tokens[1])
            pool_table.append((location_counter, None, None, None, None))

        # If LTORG or END directive is found, stop processing
        elif tokens[0] in ['LTORG', 'END']:
            break

        # If the line contains an instruction
        elif len(tokens) >= 2:
            opcode = tokens[0]
            operand = tokens[1]

            # If the instruction contains a constant, remove '='
            if operand.startswith("='"):
                operand = operand[2:-1]

            # Add the line to the pool table
            pool_table.append((location_counter, label, opcode, operand, ' '.join(tokens[2:])))

            # Increment the location counter
            location_counter += 1

    return pool_table

# Example usage
source_code = """
START 100
READ A
    MOVER AREG, ='1'
    MOVEM AREG, B
MOVER BREG, ='6'
    ADD AREG, BREG
    COMP AREG, A
    BC GT, LAST
    LTORG 
NEXT    SUB AREG, ='1'
        MOVER CREG, B  
        ADD   CREG, ='8'
        MOVEM CREG, B  
        PRINT B
LAST    STOP
A   DS  1
B   DS  1
        END
"""

pool_table = generate_pool_table(source_code)
print("Location\tLabel\tOpcode\tOperand\tComment")
for entry in pool_table:
    print(f"{entry[0]}\t\t{entry[1]}\t{entry[2]}\t{entry[3]}\t{entry[4]}")
