# Relações binárias

coordenadas_navio = {(1, 1), (1, 2)} 

acertos = set() 

print("BATALHA NAVAL")
print("O mar é uma grade de números. O navio ocupa 2 espaços.")
print("Dica: Você pode digitar números como 0, 1, 2, 3...")

jogo_acabou = False
tentativas = 0

while not jogo_acabou:
    print(f"\n--- PREPARE O CANHÃO (Tentativa {tentativas + 1}) ---")
    chute_x = int(input("Digite a coordenada X (Linha): "))
    chute_y = int(input("Digite a coordenada Y (Coluna): "))
    
    chute = (chute_x, chute_y)
    tentativas += 1
    
    if chute in coordenadas_navio:
        print(f"Você acertou a parte {chute} do navio!")
        
        acertos.add(chute) 
        
        if acertos == coordenadas_navio:
            print(f"\nVocê afundou o navio INTEIRO em {tentativas} tentativas.")
            jogo_acabou = True
        else:
            print("-> Fique atento: O navio ainda não afundou. Falta acertar a outra parte!")
            
    else:
        print("Tiro na água. Tente novamente!")