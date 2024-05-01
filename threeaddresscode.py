def generate_three_address_code(expression):
    tokens = expression.split()
    temp_count = 1
    result = []

    def get_temp():
        nonlocal temp_count
        temp = f"t{temp_count}"
        temp_count += 1
        return temp

    for i in range(len(tokens)):
        if tokens[i] in ['+', '-', '*', '/']:
            op = tokens[i]
            arg1 = tokens[i-1]
            arg2 = tokens[i+1]

            if i == 1:
                temp1 = get_temp()
                result.append((op, arg1, arg2, temp1))
            else:
                temp1 = result[-1][-1]

            if i < len(tokens) - 2:
                temp2 = get_temp()
                result.append((op, temp1, arg2, temp2))
            else:
                result[-1] = (op, temp1, arg2, result[-1][-1])

    return result

expression = "u*u - u*v + v*v"
three_address_code = generate_three_address_code(expression)
for line in three_address_code:
    print(line)

