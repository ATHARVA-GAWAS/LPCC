def generate_MDT(input_code):
    mdt = {}
    macro_name = None
    mnt = {}

    for line in input_code:
        if "MACRO" in line:
            macro_name = line.split()[1]
            mnt[macro_name] = len(mdt) + 1
            mdt[mnt[macro_name]] = []
        elif "MEND" in line:
            macro_name = None
        elif macro_name:
            mdt[mnt[macro_name]].append(line.strip())

    return mdt

def main():
    input_code = [
        "LOAD A",
        "STORE B",
        "MACRO ABC",
        "LOAD p",
        "SUB q",
        "MEND",
        "MACRO ADD1 ARG",
        "LOAD X",
        "STORE ARG",
        "MEND",
        "MACRO ADD5 A1, A2, A3",
        "STORE A2",
        "ADD1 5",
        "ADD1 10",
        "LOAD A1",
        "LOAD A3",
        "MEND",
        "ABC",
        "ADD5 D1, D2, D3",
        "END"
    ]

    mdt = generate_MDT(input_code)

    print("Macro Definition Table (MDT):")
    for key, value in mdt.items():
        print(f"{key}: {', '.join(value)}")

if __name__ == "__main__":
    main()