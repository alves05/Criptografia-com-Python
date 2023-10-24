def codificar_cesar(mensagem, chave, ordem="direta"):
    """
    Aplica o método da Cifra de Cesar na codificação.
    ----------------------
    ENTRADA:
        - mensagem, ```str```: Texto que irá ser criptografado.
        - chave, ```str```: Senha alfanumérica que irá definir a offset do texto.
        - ordem, ```str```: Assume dois valores: ```direta``` e ```inversa```.
                            Ordem ```direta``` irá criptografar a mensagem.
                            Ordem ```inversa``` irá descriptografar a mensagem.
    ----------------------
    SAÍDA:
        _ mensagem_transformada, ```str```: Mensagem criptografada, em ordem direta, ou mensagem
                                            descriptografada, se ordem inversa.
    """
    ordem = ordem.lower()
    mensagem_transformada = ""
        
    if ordem not in ("direta", "inversa"):
        raise Exception("Valor de `ordem` inválido. Escolha entre `direta` ou `inversa`.")

    if ordem == "direta":
        for caractere in mensagem:
            mensagem_transformada += chr(ord(caractere) + chave)
    
    if ordem == "inversa":
        for caractere in mensagem:
            mensagem_transformada += chr(ord(caractere) - chave)

    return mensagem_transformada

def transforma_chave(chave):
    chave = str(chave)
    chave_numerica = 0

    for caractere in str(chave):
        chave_numerica += ord(caractere)
    
    return chave_numerica

def codificar(mensagem, chave, metodo="cesar"):
    """
    Função que escolhe qual método de criptografia será utilizado. Suporta os métodos:
        - Cifra de César

    ----------------------
    ENTRADAS:
        - mensagem, ```str```: String da mensagem que será codificada.
        - chave, ```str```: String contendo a chave secreta para codificação que será utilizada.
        - metodo, ```str```: String que define o algoritmo de codificação que será utilizado. Default = Cifra de Cesar.
    ----------------------
    SAÍDAS:
        - cifra, ```str```: String com o resultado das operações de codificação aplicadas.
    """
    chave_numerica = transforma_chave(chave)
    cifra = globals()[f'codificar_{metodo}'](mensagem, chave_numerica)
    return cifra

def decodificar(mensagem_codificada, chave, metodo="cesar"):
    """
    Função que recupera uma mensagem codificada previamente.
    ----------------------
    ENTRADA:
        - mensagem_codificada, ```str```: Mensagem criptografada utilizando ````chave``` e ```método```
        - chave, ```str```: Chave secreta para descriptografia. Precisa ser igual à chave utilizada na criptografia.
        - metodo, ```str```: Método de descriptografia a ser utilizado. Precisa ser o mesmo utilizado para a criptografia.
    ----------------------
    SAÍDA:
        - mensagem, ```str```: Mensagem original.
    
    """
    chave_numerica = transforma_chave(chave)
    mensagem = globals()[f'codificar_{metodo}'](mensagem_codificada, chave_numerica, ordem="inversa")
    return mensagem

# print(codificar("olá mundo", 5))
# print(codificar("ola mundo", 5))
# print(codificar("olá mundo!", 5))
# print(codificar("olá mundo?!", 5))
# print(codificar("olá mundo, Aqui é Adam", 5))
# print(codificar("a", 5))
# print(codificar("A", 5))
# print(codificar("á", 5))
# print(codificar("Á", 5))
# print(codificar("à", 5))
# print(codificar("À", 5))
# print(codificar("ã", 5))
# print(codificar("Ã", 5))
# print(codificar("â", 5))
# print(codificar("Â", 5))
# print(codificar("ä", 5))
# print(codificar("Ä", 5))
# print(codificar("a", "pao"))

# print(decodificar("¤¡ĖU¢ª£¤", 5))
# print(decodificar("¤¡U¢ª£¤", 5))
# print(decodificar("¤¡ĖU¢ª£¤V", 5))
# print(decodificar("¤¡ĖU¢ª£¤tV", 5))
# print(decodificar("¤¡ĖU¢ª£¤aUv¦ªUĞUv¢", 5))
# print(decodificar("", 5))
# print(decodificar("v", 5))
# print(decodificar("Ė", 5))
# print(decodificar("ö", 5))
# print(decodificar("ĕ", 5))
# print(decodificar("õ", 5))
# print(decodificar("Ę", 5))
# print(decodificar("ø", 5))
# print(decodificar("ė", 5))
# print(decodificar("÷", 5))
# print(decodificar("ę", 5))
# print(decodificar("ù", 5))
# print(decodificar("ơ", "pao"))

# Função principal que interage com o usuário
def main():
    while True:
        # Pergunta ao usuário se ele deseja codificar, decodificar ou sair
        modo = input("Você deseja codificar, decodificar ou sair? ")
        if modo.lower() not in ['codificar', 'decodificar', 'sair']:
            print("Modo inválido. Tente novamente.")
            continue
        if modo.lower() == 'sair':
            break
        # Pede ao usuário para inserir a mensagem e a chave
        mensagem = input("Insira a mensagem: ")
        chave = input("Insira a chave: ")
        # Codifica ou decodifica a mensagem com base na escolha do usuário e exibe o resultado
        if modo.lower() == 'codificar':
            print("Mensagem codificada:", codificar(mensagem, chave))
        else:
            print("Mensagem decodificada:", decodificar(mensagem, chave))

# Garante que a função principal será executada apenas se este script for executado diretamente (não quando importado como um módulo)
if __name__ == "__main__":
    main()
