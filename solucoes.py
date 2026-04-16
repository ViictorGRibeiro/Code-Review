def sao_anagramas(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    return sorted(string1) == sorted(string2)

def cifra_de_cesar(texto, deslocamento):
    resultado = ""

    for char in texto:
        if char.isalpha():  # verifica se é letra
            # define base (maiúscula ou minúscula)
            base = ord('A') if char.isupper() else ord('a')
            
            # aplica o deslocamento
            nova_letra = (ord(char) - base + deslocamento) % 26 + base
            
            resultado += chr(nova_letra)
        else:
            # mantém espaços e símbolos
            resultado += char
    return resultado

def encontrar_maior_palavara(frase):
    palavras = frase.split()
    maior = palavras[0]

    for palavra in palavras:
        if len(palavra) > len(maior):
            maior = palavra

    return maior
