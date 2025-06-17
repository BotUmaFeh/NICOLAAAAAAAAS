dist = float(input("Informe a distância da viagem em km: "))
cmg = float(input("informe o consumo médio do carro em km/l: "))
pg = float(input("Informe o preço da gasolina: "))
print (f"Serão necessários {dist // cmg} litros de gasolina, gastando {(dist // cmg) * pg} reais.")