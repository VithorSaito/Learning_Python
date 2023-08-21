import forca
import advinhação

print("----------------------------------")
print("---------Escolha o jogo!!---------")
print("----------------------------------")

print("(1) Forca (2) Adivinhação")
jogos = int(input("Qual jogo?"))

if(jogos == 1):
    print("jogando Forca")
    forca.jogar()
elif(jogos == 2):
    print("jogando Adivinhação")
    advinhação.jogar()