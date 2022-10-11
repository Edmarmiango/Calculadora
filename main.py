# Função para somar números
def addNum(firstnum, secondnum): print("%s + %s = %s" %(firstnum, secondnum, firstnum + secondnum))

# Função para Subtrair números
def subNum(firstnum, secondnum): print("%s - %s = %s" %(firstnum, secondnum, firstnum - secondnum))

# Função para Multiplicação números
def multNum(firstnum, secondnum): print("%s * %s = %s" %(firstnum, secondnum, firstnum * secondnum))

# Função para Divisão números
def divNum(firstnum, secondnum):print("%s / %s = %s" %(firstnum, secondnum, firstnum / secondnum))


print("Digite o número da operação desejada")
print("1 - ADIÇÃO")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")
opc = int(input("selecione a opção(1/2/3/4):"))
if opc == 1:
    pri = int(input("Digite o primeiro número: "))
    seg = int(input("Digite o segundo número: "))
    addNum(pri, seg)
elif opc == 2:
    pri = int(input("Digite o primeiro número: "))
    seg = int(input("Digite o segundo número: "))
    subNum(pri, seg)
elif opc == 3:
    pri = int(input("Digite o primeiro número: "))
    seg = int(input("Digite o segundo número: "))
    multNum(pri, seg)
elif opc == 4:
    pri = int(input("Digite o primeiro número: "))
    seg = int(input("Digite o segundo número: "))
    divNum(pri, seg)
else:
    print("Opção inválida")



