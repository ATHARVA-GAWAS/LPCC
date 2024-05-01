def generate_symbol_table(assembly_code):
    symbol_table = {}
    location_counter = None

    # First Pass
    for line in assembly_code:
        parts = line.split()
        if len(parts) == 2:
            if parts[0] == "START":
                location_counter = int(parts[1])
            elif parts[0] == "DS":
                symbol_table[parts[1]] = location_counter
                location_counter += 1
            else:
                symbol_table[parts[0]] = location_counter
                location_counter += 1
        elif len(parts) > 2:
            if parts[1] == "START":
                location_counter = int(parts[2])
            elif parts[1] == "DS":
                symbol_table[parts[0]] = location_counter
                location_counter += int(parts[2])

    # Second Pass
    location_counter = None
    for line in assembly_code:
        parts = line.split()
        if len(parts) > 1:
            if parts[0] == "START":
                location_counter = int(parts[1])
            elif parts[1] == "DS":
                location_counter += int(parts[2])
            else:
                location_counter += 1

    return symbol_table

assembly_code = [
    "START 180",
    "READ M",
    "READ N",
    "LOOP MOVER AREG, M",
    "MOVER BREG, N",
    "COMP BREG, ='200'",
    "BC GT, LOOP",
    "BACK SUB AREG, M",
    "COMP AREG, ='500'",
    "BC LT, BACK",
    "STOP",
    "M DS 1",
    "N DS 1",
    "END"
]

symbol_table = generate_symbol_table(assembly_code)
print("Symbol Table:")
for symbol, location in symbol_table.items():
    print(symbol, ":", location)