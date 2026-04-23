# Tabelas-Verdade e Conectivos Lógicos

print("O ENIGMA DAS PORTAS")

tem_chave_ouro = True
tem_chave_prata = False

print("\nVocê está diante da PORTA DO DRAGÃO (Exige Ouro E Prata)")
#Regra do E 
if tem_chave_ouro and tem_chave_prata:
    print("A porta abriu! Você passou.")
else:
    print("A porta continua trancada. Faltam chaves!")

print("\nVocê está diante da PORTA DO DUENDE (Exige Ouro OU Prata)")
# Regra do OU
if tem_chave_ouro or tem_chave_prata:
    print("A porta abriu! Você passou.")
else:
    print("A porta continua trancada. Você não tem nenhuma chave!")