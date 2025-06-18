print ("POR FAVOR RESPONDA A PERGUNTA COM 'S' PARA 'SIM' E 'N' PARA 'NÃO'. APERTE ENTER PARA CONTINUAR")
perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? "]
respostas = []
conts = 0
for pergunta in perguntas:
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in ['s', 'n']:
            respostas.append(resposta)
            if resposta == "s":
                conts += 1
            break
        else:
            print("Por favor, responda apenas com 'S' para 'Sim' ou 'N' para 'Não'.")
if conts == 4:
    print ("VOCÊ É UM ASSASSINO, CARA!")
elif conts == 3:
    print ("HMMMM, ME PARECE QUE VOCÊ É CUMPLICE DISSO AÍ EIN!")
elif conts == 2:
    print ("IIIIIIH TÁ SUSPEITO EIN, CHEGADO!")
else:
    print ("VOCÊ É INOCENTE! MAS POR QUANTO TEMPO?")