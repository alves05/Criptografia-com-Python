#%%
def codificar_vigenere(mensagem, chave, ordem="direta"):
    """
    Aplica o método da Cifra de Vigènere na codificação.
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
    mensagem_transformada = ""

    # Garante que a chave e a mensagem tenham o mesmo tamanho
    if len(chave) < len(mensagem):
        while len(chave) < len(mensagem):
            chave += chave
        chave = chave[:len(mensagem)]

    if ordem == "direta":
        for car_chave, car_mensagem in zip(chave, mensagem):
            offset = transforma_chave(car_chave)
            mensagem_transformada += chr(ord(car_mensagem) + offset)
    else:
        for car_chave, car_mensagem in zip(chave[::-1], mensagem):
            offset = transforma_chave(car_chave)
            mensagem_transformada += chr(ord(car_mensagem) - offset)

    
    return mensagem_transformada

def codificar_cesar(mensagem, chave, ordem="direta"):
    """
    Aplica o método da Cifra de Cesar na codificação, usando chave única.
    ----------------------
    ENTRADA:
        - mensagem, ```str```: Texto que irá ser criptografado.
        - chave, ```str```: Senha alfanumérica que irá definir a offset do texto.
    ----------------------
    SAÍDA:
        - mensagem_transformada, ```str```: Mensagem criptografada, em ordem direta, ou mensagem
                                            descriptografada, se ordem inversa.
    """

    chave_numerica = transforma_chave(chave)

    mensagem_transformada = ""
    for caractere in mensagem:
        if ordem == "direta":
            mensagem_transformada += chr(ord(caractere) + chave_numerica)
        else:
            mensagem_transformada += chr(ord(caractere) - chave_numerica)

    return mensagem_transformada

def transforma_chave(chave):
    chave = str(chave)
    chave_numerica = 0

    for caractere in str(chave):
        chave_numerica += ord(caractere)
    
    return chave_numerica

def codificar(mensagem, chave, ordem="direta", metodo="cesar"):
    """
    Função que escolhe qual método de criptografia será utilizado. Suporta os métodos:
        - Cifra de César (cesar)
        - Cifra de Vigènere (vigenere)
    ----------------------
    ENTRADAS:
        - mensagem, ```str```: String da mensagem que será codificada.
        - chave, ```str```: String contendo a chave secreta para codificação que será utilizada.
        - metodo, ```str```: String que define o algoritmo de codificação que será utilizado. Default = Cifra de Cesar.
        - ordem, ```str```: Define se a mensagem será criptografada (ordem direta) ou descriptografada (ordem inversa).
    ----------------------
    SAÍDAS:
        - cifra, ```str```: String com o resultado das operações de codificação aplicadas.
    """

    ordem = ordem.lower()
    if ordem not in ("direta", "inversa"):
        raise Exception("Valor de `ordem` inválido. Escolha entre `direta` ou `inversa`.")

    cifra = globals()[f'codificar_{metodo}'](mensagem, chave, ordem)

    return cifra
#%%
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
            print("Mensagem codificada:", codificar(mensagem, chave, ordem="direta", metodo='vigenere'))
        else:
            print("Mensagem decodificada:", codificar(mensagem, chave, ordem="inversa", metodo='vigenere'))

# Garante que a função principal será executada apenas se este script for executado diretamente (não quando importado como um módulo)
if __name__ == "__main__":
    main()
#%%
# print(codificar("olá mundo", '5',ordem="direta",metodo="vigenere"))
# print(codificar("ola mundo", '5',ordem="direta",metodo="vigenere"))
# print(codificar("olá mundo!", '5',ordem="direta",metodo="vigenere"))
# print(codificar("olá mundo?!", '5',ordem="direta",metodo="vigenere"))
# print(codificar("olá mundo, Aqui é Adam", '5',ordem="direta",metodo="vigenere"))
# print(codificar("a", '5',ordem="direta",metodo="vigenere"))
# print(codificar("A", '5',ordem="direta",metodo="vigenere"))
# print(codificar("á", '5',ordem="direta",metodo="vigenere"))
# print(codificar("Á", '5',ordem="direta",metodo="vigenere"))
# print(codificar("à", '5',ordem="direta",metodo="vigenere"))
# print(codificar("À", '5',ordem="direta",metodo="vigenere"))
# print(codificar("ã", '5',ordem="direta",metodo="vigenere"))
# print(codificar("Ã", '5',ordem="direta",metodo="vigenere"))
# print(codificar("â", '5',ordem="direta",metodo="vigenere"))
# print(codificar("Â", '5',ordem="direta",metodo="vigenere"))
# print(codificar("ä", '5',ordem="direta",metodo="vigenere"))
# print(codificar("Ä", '5',ordem="direta",metodo="vigenere"))
# print(codificar("a", "pao",ordem="direta",metodo="vigenere"))

#%%
# print(codificar("¤¡ĖU¢ª£¤", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("¤¡U¢ª£¤", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("¤¡ĖU¢ª£¤V", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("¤¡ĖU¢ª£¤tV", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("¤¡ĖU¢ª£¤aUv¦ªUĞUv¢", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("v", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("Ė", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("ö", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("ĕ", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("õ", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("Ę", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("ø", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("ė", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("÷", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("ę", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("ù", '5',ordem="inversa",metodo="vigenere"))
# print(codificar("Ñ", "pao",ordem="inversa",metodo="vigenere"))
# %%
