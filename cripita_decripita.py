#%%
'''Função que criptografar a mensagem.'''
def codificar(mensagem : str, chave : str):
    mensagem_codificada = ""

    '''Garante que a chave e a mensagem tenham o mesmo tamanho.'''
    if len(chave) < len(mensagem):
        while len(chave) < len(mensagem):
            chave += chave
    
    chave = chave[:len(mensagem)]

    for car_chave, car_mensagem in zip(chave, mensagem):
        offset = transforma_chave(car_chave)
        mensagem_codificada += chr((ord(car_mensagem) + offset) % ascii_extensao())
    
    return mensagem_codificada

'''Função que descriptografa a mensagem.'''
def decodificar(mensagem : str, chave : str):
    mensagem_decodificada = ""

    '''Garante que a chave e a mensagem tenham o mesmo tamanho.'''
    if len(chave) < len(mensagem):
        while len(chave) < len(mensagem):
            chave += chave
    
    chave = chave[:len(mensagem)]

    for car_chave, car_mensagem in zip(chave, mensagem):
        offset = transforma_chave(car_chave)
        mensagem_decodificada += chr((ord(car_mensagem) - offset) % ascii_extensao())

    
    return mensagem_decodificada

'''Função que transforma a chave.'''
def transforma_chave(chave : str):
    chave = str(chave)
    chave_numerica = 0

    for caractere in str(chave):
        chave_numerica += ord(caractere)
    
    return chave_numerica % alfabeto_extensao()

'''Define o intervalo válido da funação chr().'''
def ascii_extensao():
    invervalo = 1114112
    return invervalo

'''Define o intervalo do alfabeto português-BR.'''
def alfabeto_extensao():
    extensao = 26
    return extensao

'''Função principal que interage com o usuário.'''
def main():
    while True:
        modo = input('Digite C para codificar, D para decodificar ou S para sair? ').strip(' ')

        if modo.lower() not in ['c', 'd', 's']:
            print("Modo inválido. Tente novamente.")
            continue

        if modo.lower() == 's':
            break

        mensagem = input('Digite uma mensagem: ')
        chave = input('Digite uma chave: ')
        
        if modo.lower() == 'c':
            print(codificar(mensagem=mensagem, chave=chave))
        
        else:
            print(decodificar(mensagem=mensagem, chave=chave))

'''Garante que a função principal será executada apenas se este script for executado diretamente (não quando importado como um módulo).'''
if __name__ == "__main__":
    main()
# %%
