vdl = float(input("Olá! Informe quanto foi essa larica aí tua: "))
qpd = int(input("Caralho, tá podendo gastar ein? E em quantos vagabundos tu vão pagar? "))
vpp = vdl // qpd
print (f"O valor por pessoa é {vpp} reais")
troco = vdl % qpd
troco = troco // 1
if troco >= 0.01:
    print(f"E o troco deu {troco}!")