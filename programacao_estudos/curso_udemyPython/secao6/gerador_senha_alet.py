import string as s 
from secrets import SystemRandom as Sr

while True:
    try:
        total_caracteres = int(input("Digite o total de caractéres para sua senha:"))
        break
    except:
        print("ERRO! Digite um número inteiro")

senha_alet = ''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k= total_caracteres))

print('-='*30)
print(f"Sua senha é:  {senha_alet}")
