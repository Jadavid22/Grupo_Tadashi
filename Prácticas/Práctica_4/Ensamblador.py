def assembler(file_path):
    # Diccionarios para mapear mnemónicos a códigos binarios
    comp_dict = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "M": "1110000",
        "!D": "0001101",
        "!A": "0110001",
        "!M": "1110001",
        "-D": "0001111",
        "-A": "0110011",
        "-M": "1110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "M+1": "1110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "M-1": "1110010",
        "D+A": "0000010",
        "D+M": "1000010",
        "D-A": "0010011",
        "D-M": "1010011",
        "A-D": "0000111",
        "M-D": "1000111",
        "D&A": "0000000",
        "D&M": "1000000",
        "D|A": "0010101",
        "D|M": "1010101"
    }

    dest_dict = {
        "null": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }

    jump_dict = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }

    symbol_table = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SCREEN": 16384,
        "KBD": 24576
    }

    # Primera pasada para procesar etiquetas y añadir símbolos predefinidos
    with open(file_path, "r") as file:
        rom_address = 0
        for line in file:
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            if line.startswith("("):
                label = line.strip("()")
                symbol_table[label] = rom_address
            else:
                rom_address += 1

    # Segunda pasada para traducir las instrucciones
    with open(file_path, "r") as file:
        ram_address = 16
        with open(file_path.replace(".asm", ".hack"), "w") as output_file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("//") or line.startswith("("):
                    continue
                if line.startswith("@"):
                    symbol = line[1:]
                    try:
                        address = int(symbol)
                    except ValueError:
                        if symbol not in symbol_table:
                            symbol_table[symbol] = ram_address
                            ram_address += 1
                        address = symbol_table[symbol]
                    binary_address = format(address, "016b")
                    output_file.write(binary_address + "\n")
                else:
                    dest_comp_jump = line.split(";")
                    if "=" in dest_comp_jump[0]:
                        dest, comp = dest_comp_jump[0].split("=")
                    else:
                        dest = "null"
                        comp = dest_comp_jump[0]
                    if len(dest_comp_jump) > 1:
                        jump = dest_comp_jump[1]
                    else:
                        jump = "null"
                    comp_binary = comp_dict[comp]
                    dest_binary = dest_dict[dest]
                    jump_binary = jump_dict[jump]
                    binary_instruction = "111" + comp_binary + dest_binary + jump_binary
                    output_file.write(binary_instruction + "\n")


# ==== USAR EN CADA UNO DE LOS ARCHIVOS PROPORCIONADOS EN EL PROYECTO ==== #      
#assembler("\Add.asm")
#assembler("\Max.asm")
#assembler("\MaxL.asm")
#assembler("\Pong.asm")
#assembler("\PongL.asm")
#assembler("\Rect.asm")
#assembler("\RectL.asm")