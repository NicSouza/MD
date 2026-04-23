# Matrizes

tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def mostrar_tabuleiro():
    print("\n  0   1   2  (Colunas)")
    linha_num = 0
    for linha in tabuleiro:
        print(f"{linha_num} | {linha[0]} | {linha[1]} | {linha[2]} |")
        print("  -------------")
        linha_num += 1

def verificar_vitoria(jogador):
    for l in range(3):
        if tabuleiro[l][0] == jogador and tabuleiro[l][1] == jogador and tabuleiro[l][2] == jogador:
            return True
            
    for c in range(3):
        if tabuleiro[0][c] == jogador and tabuleiro[1][c] == jogador and tabuleiro[2][c] == jogador:
            return True
            
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
        
    return False

print("JOGO DA VELHA")
print("Você é o 'X'. Para jogar, digite o número da linha e depois da coluna")

jogadas = 0
jogo_acabou = False

while jogadas < 9 and not jogo_acabou:
    mostrar_tabuleiro()
    
    print("\n--- SUA VEZ! ---")
    linha = int(input("Escolha a LINHA (0, 1 ou 2): "))
    coluna = int(input("Escolha a COLUNA (0, 1 ou 2): "))
    
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = 'X'
        jogadas += 1
        
        if verificar_vitoria('X'):
            mostrar_tabuleiro()
            print("\nParabéns, você venceu!")
            jogo_acabou = True
            break 
            
        if jogadas < 9 and not jogo_acabou:
            jogou_o = False
            for l in range(3):
                for c in range(3):
                    if tabuleiro[l][c] == ' ' and not jogou_o:
                        tabuleiro[l][c] = 'O'
                        jogou_o = True
                        jogadas += 1
                        
            if verificar_vitoria('O'):
                mostrar_tabuleiro()
                print("\nO Computador venceu!")
                jogo_acabou = True
                break
    else:
        print("Esse espaço já está ocupado. Tente de novo.")

if jogadas == 9 and not jogo_acabou:
    mostrar_tabuleiro()
    print("\nDeu empate.")