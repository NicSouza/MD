# Conjuntos

loja_rpg = {'espada', 'escudo', 'pocao', 'mapa', 'bota'}
mochila_heroi = {'espada', 'pocao'}

print("BARRACA DE ITENS DO RPG")
print(f"O que a loja vende: {loja_rpg}")
print(f"O que você já tem: {mochila_heroi}")

print("\nVERIFICANDO O QUE FALTA (Complementar/Diferença)")
itens_para_comprar = loja_rpg - mochila_heroi

print(f"Você ainda precisa comprar: {itens_para_comprar}")

mochila_heroi.remove('espada')
print(f"\nO herói perdeu a espada! Mochila atual: {mochila_heroi}")