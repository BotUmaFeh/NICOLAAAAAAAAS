print ("POR FAVOR RESPONDA A PERGUNTA COM 'S' PARA 'SIM' E 'N' PARA 'NÃO'. APERTE ENTER PARA CONTINUAR")
perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? "]
respostas = []
conts = 0
for pergunta in perguntas:
    resposta = input(pergunta).lower()
    respostas.append(resposta)
    if resposta == "s":
        conts = conts + 1
if conts == 4:
    print ("VOCÊ É UM ASSASSINO, CARA!")
elif conts == 3:
    print ("HMMMM, ME PARECE QUE VOCÊ É CUMPLICE DISSO AÍ EIN!")
elif conts == 2:
    print ("IIIIIIH TÁ SUSPEITO EIN, CHEGADO!")
else:
    print ("VOCÊ É INOCENTE! MAS POR QUANTO TEMPO?")