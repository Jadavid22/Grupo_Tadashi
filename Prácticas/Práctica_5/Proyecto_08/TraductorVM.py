def traductorVM(archivo):
    nombre_archivo = archivo.strip(".vm")
    nuevo_archivo = open(nombre_archivo + ".asm", "x")

    k = 0

    with open(archivo) as archivo_vm:
        for linea in archivo_vm.readlines():
            linea = linea.strip(" ")
            linea = linea.rstrip("\n")

            if linea.startswith("push"):
                partes = linea.split(" ")
                segmento = partes[1]
                valor = int(partes[2])

                if segmento == "constant":
                    nuevo_archivo.write("\n@" + str(valor))
                    nuevo_archivo.write("\nD=A")
                    nuevo_archivo.write("\n@SP")
                    nuevo_archivo.write("\nA=M")
                    nuevo_archivo.write("\nM=D")
                    nuevo_archivo.write("\n@SP")
                    nuevo_archivo.write("\nM=M+1")
                elif segmento == "pointer":
                    if valor == 0:
                        nuevo_archivo.write("\n@THIS")
                    elif valor == 1:
                        nuevo_archivo.write("\n@THAT")
                    nuevo_archivo.write("\nD=M")
                    nuevo_archivo.write("\n@SP")
                    nuevo_archivo.write("\nA=M")
                    nuevo_archivo.write("\nM=D")
                    nuevo_archivo.write("\n@SP")
                    nuevo_archivo.write("\nM=M+1")
                else:
                    if segmento == "local":
                        nuevo_archivo.write("\n@LCL")
                    elif segmento == "argument":
                        nuevo_archivo.write("\n@ARG")
                    elif segmento == "this":
                        nuevo_archivo.write("\n@THIS")
                    elif segmento == "that":
                        nuevo_archivo.write("\n@THAT")
                    elif segmento == "static":
                        nuevo_archivo.write("\n@" + str(valor))
                    elif segmento == "temp":
                        nuevo_archivo.write("\n@" + str(valor + 5))
                    nuevo_archivo.write("\nD=M")
                    if segmento == "static":
                        nuevo_archivo.write("\n@" + str(16 + valor))
                    elif segmento == "temp":
                        nuevo_archivo.write("\n@" + str(valor + 5))
                    else:
                        nuevo_archivo.write("\n@" + str(valor))
                    nuevo_archivo.write("\nA=D+A")
                    nuevo_archivo.write("\nD=M")
                    nuevo_archivo.write("\n@SP")
                    nuevo_archivo.write("\nA=M")
                    nuevo_archivo.write("\nM=D")
                    nuevo_archivo.write("\n@SP")
                    nuevo_archivo.write("\nM=M+1")

            if linea.startswith("pop"):
                partes = linea.split(" ")
                segmento = partes[1]
                valor = int(partes[2])

                if segmento == "local":
                    nuevo_archivo.write("\n@LCL")
                elif segmento == "argument":
                    nuevo_archivo.write("\n@ARG")
                elif segmento == "this":
                    nuevo_archivo.write("\n@THIS")
                elif segmento == "that":
                    nuevo_archivo.write("\n@THAT")
                elif segmento == "static":
                    nuevo_archivo.write("\n@" + str(valor))
                elif segmento == "temp":
                    nuevo_archivo.write("\n@" + str(valor + 5))
                elif segmento == "pointer":
                    if valor == 0:
                        nuevo_archivo.write("\n@THIS")
                    elif valor == 1:
                        nuevo_archivo.write("\n@THAT")
                nuevo_archivo.write("\nD=M")
                if segmento == "static":
                    nuevo_archivo.write("\n@" + str(16 + valor))
                elif segmento == "temp":
                    nuevo_archivo.write("\n@" + str(valor + 5))
                elif segmento == "pointer":
                    if valor == 0:
                        nuevo_archivo.write("\n@3")
                    elif valor == 1:
                        nuevo_archivo.write("\n@4")
                else:
                    nuevo_archivo.write("\n@" + str(valor))
                nuevo_archivo.write("\nD=D+A")
                nuevo_archivo.write("\n@R13")
                nuevo_archivo.write("\nM=D")
                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nAM=M-1")
                nuevo_archivo.write("\nD=M")
                nuevo_archivo.write("\n@R13")
                nuevo_archivo.write("\nA=M")
                nuevo_archivo.write("\nM=D")

            if linea.startswith("add") or linea.startswith("sub"):
                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nAM=M-1")
                nuevo_archivo.write("\nD=M")
                nuevo_archivo.write("\nA=A-1")
                if linea.startswith("add"):
                    nuevo_archivo.write("\nM=D+M")
                elif linea.startswith("sub"):
                    nuevo_archivo.write("\nM=M-D")

            if linea.startswith("neg"):
                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nA=M")
                nuevo_archivo.write("\nA=A-1")
                nuevo_archivo.write("\nM=-M")

            if linea.startswith("eq") or linea.startswith("gt") or linea.startswith("lt"):
                k += 1
                i = str(k)

                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nAM=M-1")
                nuevo_archivo.write("\nD=M")
                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nAM=M-1")
                nuevo_archivo.write("\nD=M-D")
                nuevo_archivo.write("\n@True" + i)
                if linea.startswith("eq"):
                    nuevo_archivo.write("\nD;JEQ")
                elif linea.startswith("gt"):
                    nuevo_archivo.write("\nD;JGT")
                elif linea.startswith("lt"):
                    nuevo_archivo.write("\nD;JLT")
                nuevo_archivo.write("\nD=0")
                nuevo_archivo.write("\n@False" + i)
                nuevo_archivo.write("\n0;JMP")
                nuevo_archivo.write("\n(True" + i + ")")
                nuevo_archivo.write("\nD=-1")
                nuevo_archivo.write("\n(False" + i + ")")
                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nA=M")
                nuevo_archivo.write("\nM=D")
                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nM=M+1")

            if linea.startswith("and") or linea.startswith("or"):
                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nAM=M-1")
                nuevo_archivo.write("\nD=M")
                nuevo_archivo.write("\nA=A-1")
                if linea.startswith("and"):
                    nuevo_archivo.write("\nM=D&M")
                elif linea.startswith("or"):
                    nuevo_archivo.write("\nM=D|M")

            if linea.startswith("not"):
                nuevo_archivo.write("\n@SP")
                nuevo_archivo.write("\nA=M")
                nuevo_archivo.write("\nA=A-1")
                nuevo_archivo.write("\nM=!M")
    

#Traducir los archivos VM a ASM.
traductorVM("Main.vm")
#traductorVM("Sys.vm")
#traductorVM("Class1.vm")
#traductorVM("Class2.vm")
#traductorVM("SimpleFunction.vm")
#traductorVM("FibonacciSeries.vm")
