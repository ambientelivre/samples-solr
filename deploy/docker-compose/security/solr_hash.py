import os
import hashlib
import base64

def generate_solr_password_hash(password: str):
    # Gera um salt aleatório de 16 bytes
    salt = os.urandom(16)
    # Decodifica o salt para base64 para mostrar
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    # Concatena salt + senha
    salted_pass = salt + password.encode('utf-8')
    # Primeiro hash sha256
    first_hash = hashlib.sha256(salted_pass).digest()
    # Segundo hash sha256 (do primeiro hash)
    second_hash = hashlib.sha256(first_hash).digest()
    # Codifica o hash final em base64
    hash_b64 = base64.b64encode(second_hash).decode('utf-8')
    # Retorna no formato esperado: "hash salt"
    return f"{hash_b64} {salt_b64}"

if __name__ == "__main__":
    senha = input("Digite a senha para gerar hash: ")
    resultado = generate_solr_password_hash(senha)
    print("Hash para usar no security.json:")
    print(resultado)
