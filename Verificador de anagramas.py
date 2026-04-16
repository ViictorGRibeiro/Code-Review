def sao_anagramas(string1, string2):
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    
    string1 = string1.lower()
    string2 = string2.lower()
    
    lista1 = list(string1)
    lista2 = list(string2)
    
    lista1.sort()
    lista2.sort()
    
    if lista1 == lista2:
        return True
    else:
        return False


print(sao_anagramas("feio", "bunito"))
print(sao_anagramas("bota ", "toba"))
print(sao_anagramas("tijolo", "Lojito"))