nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")#imprima o texto 
print(texto.strip() + ".") #tira o espaço
print(texto.rstrip() + ".")# tira o  espaço para direita
print(texto.lstrip() + ".")# tira o  espaço para esquerda

menu = "Python"

print("####" + menu + "####")
print(menu.center(14)) # deixa no centro 
print(menu.center(14, "#")) # deixa em python entre os sinais 
print("-".join(menu)) # o join juntas 