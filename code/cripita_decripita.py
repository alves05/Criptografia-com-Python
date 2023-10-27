# %%

# Importa constantes de texto a partir de arquivo auxiliar
from constantes_texto import *

# Função que criptografar a mensagem.
def codificar(mensagem: str, chave: str):
    mensagem_codificada = ""

    # Garante que a chave e a mensagem tenham o mesmo tamanho.
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

def monta_cabecalho():
    cabecalho = TEXTO_CABECALHO.format(
        TEXTO_BARRA, 
        "*"+TEXTO_NOME_PROGRAMA.center(len(TEXTO_BARRA)-2)+"*", 
        TEXTO_BARRA
    )
    return cabecalho

# Função principal que interage com o usuário.
def main():

    print(monta_cabecalho())
    continua_programa = True
    
    while continua_programa:
        modo = input(f"{TEXTO_ENTRADA_OPCOES} {TEXTO_OPCOES}").strip()

        if modo not in ['1', '2', '3']:
            print(TEXTO_ENTRADA_INVALIDA)
        else:
            if modo == '3':
                print(TEXTO_ENCERRADO)
                continua_programa = False

            elif modo == '1':
                mensagem_entrada = input(TEXTO_PEDIDO_MENSAGEM.format("codificada"))
                chave = input(TEXTO_PEDIDO_CHAVE.format("codificar") + TEXTO_LEMBRETE_CODIFICACAO)

                mensagem_codificada = codificar(mensagem=mensagem_entrada, chave=chave)
                print(TEXTO_SUCESSO_PROCESSAMENTO.format("codificada") + mensagem_codificada)

            elif modo == '2':
                entrada_mensagem_decodificar = input(TEXTO_PEDIDO_MENSAGEM.format("decodificada"))
                entrada_chave_decodificar = input(TEXTO_PEDIDO_CHAVE.format("decodificar") + TEXTO_LEMBRETE_DECODIFICACAO)

                mensagem_decodificada = decodificar(mensagem=entrada_mensagem_decodificar, chave=entrada_chave_decodificar)
                print(TEXTO_SUCESSO_PROCESSAMENTO.format("decodificada") + mensagem_decodificada)

if __name__ == "__main__":
    main()