# %%
# Função que criptografar a mensagem.


def codificar(mensagem: str, chave: str):
    mensagem_codificada = ""

    #Garante que a chave e a mensagem tenham o mesmo tamanho.
    if len(chave) < len(mensagem):
        while len(chave) < len(mensagem):
            chave += chave

    chave = chave[:len(mensagem)]

    for car_chave, car_mensagem in zip(chave, mensagem):
        offset = transforma_chave(car_chave)
        mensagem_codificada += chr((ord(car_mensagem) + offset) % ascii_extensao())

    return mensagem_codificada


# Função que descriptografa a mensagem.


def decodificar(mensagem: str, chave: str):
    mensagem_decodificada = ""

    # Garante que a chave e a mensagem tenham o mesmo tamanho.
    if len(chave) < len(mensagem):
        while len(chave) < len(mensagem):
            chave += chave

    chave = chave[:len(mensagem)]

    for car_chave, car_mensagem in zip(chave, mensagem):
        offset = transforma_chave(car_chave)
        mensagem_decodificada += chr((ord(car_mensagem) - offset) % ascii_extensao())

    return mensagem_decodificada


# Função que transforma a chave.


def transforma_chave(chave: str):
    chave = str(chave)
    chave_numerica = 0

    for caractere in str(chave):
        chave_numerica += ord(caractere)

    return chave_numerica % alfabeto_extensao()


# Define o intervalo válido da funação chr().


def ascii_extensao():
    invervalo = 1114112
    return invervalo


# Define o intervalo do alfabeto português-BR.


def alfabeto_extensao():
    extensao = 26
    return extensao


# Função principal que interage com o usuário.


def main():

# lista de variaveis contendo as mensagens que serão exibidas para o usuário

    texto_entrada_opcao = "\nDigite um dos números abaixo para realizar a opção desejada:"
    texto_opcoes = """
[1] para codificar mensagem
[2] para decodificar mensagem
[3] para sair do programa
"""
    texto_pedido_codificada = "\nDigite a mensagem que será codificada: "
    texto_pedido_decodificada = "\nDigite a mensagem que será decodificada: "

    texto_entrada_invalida = "\nVocê inseriu uma opção inválida! Por favor, tente novamente. "

    texto_pedido_chave_codificar = "\nDigite a chave que será usada para codificar a mensagem. "
    texto_pedido_chave_decodificar = "\nDigite a chave que será usada para decodificar a mensagem. "

    texto_lembrete_codificacao = "\nLembre-se que essa mesma chave é necessária para decodificar a mensagem. "
    texto_lembrete_decodificacao = "\nLembre-se que a chave deve ser a mesma que foi utilizada na codificação. "

    texto_sucesso_codificacao = "\nMensagem codificada com sucesso: "
    texto_sucesso_decodificacao = "\nMensagem decodificada com sucesso: "

    texto_encerrado = "\nPrograma encerrado!"


    while True:
        modo = input(f"{texto_entrada_opcao} \n{texto_opcoes}").strip()

        if modo not in ['1', '2', '3']:
            print(texto_entrada_invalida)
            continue

        if modo == '3':
            print(texto_encerrado)
            break

        if modo == '1':
            entrada_mensagem_codificar = input(texto_pedido_codificada)
            entrada_chave_codificar = input(f"{texto_pedido_chave_codificar} {texto_lembrete_codificacao}")

            print(texto_sucesso_codificacao)
            print(codificar(mensagem=entrada_mensagem_codificar, chave=entrada_chave_codificar))

        elif modo == '2':
            entrada_mensagem_decodificar = input(texto_pedido_decodificada)
            entrada_chave_decodificar = input(f"{texto_pedido_chave_decodificar} {texto_lembrete_decodificacao}")

            print(texto_sucesso_decodificacao)
            print(decodificar(mensagem=entrada_mensagem_decodificar, chave=entrada_chave_decodificar))


if __name__ == "__main__":
    main()