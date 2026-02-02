import random

def GEN(seed):
    # O tamanho da chave deve ser 4 * o tamanho da semente
    # Se a semente for string, usamos o comprimento dela
    tamanho_chave = len(seed) * 4
    
    # Define a semente para o gerador ser "determinístico"
    # Isso garante que a mesma semente gere a mesma chave
    random.seed(seed)
    
    # Gera uma lista de 0s e 1s
    chave = [random.randint(0, 1) for _ in range(tamanho_chave)]
    print("Chave gerada:", chave)
    return chave

print(GEN("seed"))
