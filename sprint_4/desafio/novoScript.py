import hashlib

while True:
    entrada = input("Digite uma string qualquer para gerar o hash: ")
        
    hash_obj = hashlib.sha1(entrada.encode())
        
    print("Hash SHA-1 gerado:", hash_obj.hexdigest())

    sair = input("Deseja continuar? [s]im ou [n]ao: ").lower()

    if sair == 'n':
        break
    else:
        continue