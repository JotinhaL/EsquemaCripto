import random

def GEN(seed):
    # O tamanho da chave deve ser 4x o tamanho da semente
    tamanho_chave = len(seed) * 4
    
    # Define a semente para o gerador ser determinístico
    random.seed(seed)
    
    # Gera uma lista de 0s e 1s
    chave = [random.randint(0, 1) for _ in range(tamanho_chave)]
    print("Chave gerada: ", chave)
    return chave


def ENC(K, M):
    # Verificação de segurança: K e M devem ter o mesmo tamanho
    if len(K) != len(M):
        raise ValueError("A chave e a mensagem precisam ter o mesmo tamanho! Mensagem tem que ser 4x maior que a seed.")
    
    # Lógica de XOR entre a chave K e a mensagem M
    cifra = []
    for i in range(len(K)):
        bit_cifra = K[i] ^ M[i] # Operação XOR
        cifra.append(bit_cifra)

    print("Mensagem cifrada: ", cifra)
    return cifra


def DEC(K, C):

    # Verificação de segurança: K e C devem ter o mesmo tamanho
    if len(K) != len(C):
        raise ValueError("A chave e a mensagem cifrada precisam ter o mesmo tamanho! Mensagem tem que ser 4x maior que a seed.")
    
    # Lógica de XOR entre a chave K e a mensagem C
    decifra = []
    for i in range(len(K)):
        bit_decifra = K[i] ^ C[i] # Operação XOR
        decifra.append(bit_decifra)

    print("Mensagem decifrada: ", decifra)
    return decifra

chave = GEN("seed")
msg = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0] 
msg_cripto = ENC(chave, msg)
msg_decifrada = DEC(chave, msg_cripto)

