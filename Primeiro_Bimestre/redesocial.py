# Teoria dos Grafos e endorelação

print("REDE SOCIAL")

seguindo = {
    'Aline': {'Joao', 'Maria'},   
    'Joao': {'Aline'},             
    'Maria': {'Joao'}           
}

usuario_1 = 'Aline'
usuario_2 = 'Joao'

print(f"Analisando a relação entre {usuario_1} e {usuario_2}...")

if usuario_2 in seguindo[usuario_1]:
    print(f"-> {usuario_1} segue {usuario_2}.")
else:
    print(f"-> {usuario_1} NÃO segue {usuario_2}.")

if usuario_1 in seguindo[usuario_2]:
    print(f"<- {usuario_2} segue {usuario_1}.")
else:
    print(f"<- {usuario_2} NÃO segue {usuario_1}.")