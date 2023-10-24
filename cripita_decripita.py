#%%
def codificar_cesar(mensagem, chave):
    """
    Aplica o método da Cifra de Cesar na codificação de ```mensagem``` utilizando o valor de ```chave```.
    """

    mensagem_codificada = ""
    for caractere in mensagem:
        # Verifica se o caractere é uma letra
        if caractere.isalpha():
            # Define o deslocamento ASCII com base em se a letra é maiúscula ou minúscula
            ascii_offset = 65 if caractere.isupper() else 97
            # Codifica o caractere deslocando-o 'chave' posições no alfabeto
            mensagem_codificada += chr((ord(caractere) - ascii_offset + chave) % 26 + ascii_offset)
        else:
            # Se o caractere não for uma letra, ele é adicionado à mensagem codificada sem alterações
            mensagem_codificada += caractere

    return mensagem_codificada

codificar_cesar("olá mundo",5)
#%%

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
    
    cifra = globals()[f'codificar_{metodo}'](mensagem, chave)
    print(cifra)
    return cifra

#%%
# Função para decodificar a mensagem
def decodificar(mensagem_codificada, chave, metodo="cesar"):
    # A decodificação é feita codificando a mensagem com a chave complementar (26 - chave)
    return codificar(mensagem_codificada, 26 - chave, metodo)

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
        chave = int(input("Insira a chave (número): "))
        # Codifica ou decodifica a mensagem com base na escolha do usuário e exibe o resultado
        if modo.lower() == 'codificar':
            print("Mensagem codificada:", codificar(mensagem, chave))
        else:
            print("Mensagem decodificada:", decodificar(mensagem, chave))

# Garante que a função principal será executada apenas se este script for executado diretamente (não quando importado como um módulo)
if __name__ == "__main__":
    main()