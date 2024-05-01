class MacroProcessor:
    def __init__(self):
        self.macro_definitions = {}

    def first_pass(self, input_code):
        lines = input_code.split('\n')
        for line in lines:
            if line.startswith('MACRO'):
                macro_name = line.split()[1]
                macro_definition = []
                line = lines.pop(0)
                while not line.startswith('MEND'):
                    macro_definition.append(line)
                    line = lines.pop(0)
                self.macro_definitions[macro_name] = macro_definition

    def second_pass(self, input_code):
        intermediate_code = []
        lines = input_code.split('\n')
        for line in lines:
            if line.startswith('MACRO'):
                continue
            elif line.startswith('END'):
                break
            else:
                macro_used = False
                for macro_name, macro_definition in self.macro_definitions.items():
                    if macro_name in line:
                        macro_used = True
                        for macro_line in macro_definition:
                            expanded_line = macro_line.replace('ARG', line.split()[-1])
                            intermediate_code.append(expanded_line)
                if not macro_used:
                    intermediate_code.append(line)
        return '\n'.join(intermediate_code)


input_code = """
LOAD A
MACRO ABC
LOAD p
SUB q
MEND
STORE B
MULT D
MACRO ADD1 ARG
LOAD X
STORE ARG
MEND
LOAD B
MACRO ADD5 A1, A2, A3
STORE A2
ADD1 5
ADD1 10
LOAD A1
LOAD A3
MEND
ADD1 t
ABC
ADD5 D1, D2, D3
END
"""

processor = MacroProcessor()
processor.first_pass(input_code)
intermediate_code = processor.second_pass(input_code)
print(intermediate_code)
