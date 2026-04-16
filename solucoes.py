def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

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

    print("o meu chafe é gay")
    return resultado

def encontrar_maior_palavara(frase):
    # TODO: Implementar a lógica
    pass

