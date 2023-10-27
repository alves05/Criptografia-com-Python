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

'''Função que testa as funções codificar() e decodificar().'''
def teste_cripita_decripita(mensagem : str, chave : str):
    mensagem_codificada = codificar(mensagem=mensagem, chave=chave)
    mensagem_decodificada = decodificar(mensagem=mensagem_codificada, chave=chave)

    return mensagem == mensagem_decodificada

'''Função que testa a função transfoma_chave().'''
def teste_transforma_chave(chave : str):
    return transforma_chave(chave) % 26 == 0

def main():
    # Teste com palavras simples
    mensagem = 'olá'
    chave = '123'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'mundo'
    chave = '456'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Jorge'
    chave = '558'

    print(teste_cripita_decripita(mensagem, chave))

    # Teste com frases
    mensagem = 'Olá, mundo!'
    chave = '10'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Esta é uma mensagem criptografada.'
    chave = '745'

    print(teste_cripita_decripita(mensagem, chave))
    
    mensagem = 'Eu sempre ficava animado para os nossos telefonemas, por motivos egoístas no princípio. Um dos meus principais interesses como escritor é a ciência de como desenvolver bons hábitos e romper com os ruins. Alguém como Scott, que dominou tão claramente seus próprios hábitos, era exatamente o tipo de pessoa que poderia me ensinar uma ou duas coisinhas. E foi precisamente isso que aconteceu. É difícil me lembrar de alguma ocasião em que, ao desligar depois de algumas horas, eu não tenha aprendido algo com Scott.'
    chave = '890'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Tudo o que um sonho precisa para ser realizado é alguém que acredite que ele possa ser realizado.'
    chave = '90'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Imagine uma nova história para sua vida e acredite nela.'
    chave = '3'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Não espere por uma crise para descobrir o que é importante em sua vida.'
    chave = '1080'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Nas dificuldades da vida, descobrimos a nossa verdadeira força interior.'
    chave = '128'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'A verdadeira riqueza está nas experiências que acumulamos e não nos bens materiais que possuímos.'
    chave = '2850'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'A vida é curta demais para gastar tempo se preocupando com coisas que estão além do nosso controle. Viva! Sonhe!'
    chave = '15'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Acredite em si e chegará um dia em que os outros não terão outra escolha senão acreditar com você.'
    chave = '58'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Pessimismo leva à fraqueza, otimismo ao poder.'
    chave = '78'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'O otimismo é a fé em ação. Nada se pode levar a efeito sem otimismo.'
    chave = '85'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'O pessimismo, depois de você se acostumar a ele, é tão agradável quanto o otimismo.'
    chave = '32'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'A vida é uma balança entre aceitar o que não podemos mudar e ter coragem para mudar o que podemos.'
    chave = '1'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Amar alguém é aceitá-lo com todas as suas imperfeições e ainda assim vê-lo como perfeito.'
    chave = '8'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Não tenha medo das conquistas. Tenha medo de não tentar.'
    chave = '45'

    print(teste_cripita_decripita(mensagem, chave))
    
    mensagem = 'O amor não é medido pelo tempo que passamos juntos, mas pela qualidade dos momentos compartilhados.'
    chave = '99'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Não são as nossas ideias que nos fazem otimistas ou pessimistas, mas o otimismo e o pessimismo de origem fisiológica que fazem as nossas ideias.'
    chave = '33'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Se estivermos atentos, a presença de Deus se revela nas pequenas coisas.'
    chave = '22'

    print(teste_cripita_decripita(mensagem, chave))

    mensagem = 'Sim, meu caro. A vida é curta, então não desperdice tempo se preocupando com o que não pode mudar.'
    chave = '55'

    print(teste_cripita_decripita(mensagem, chave))

    def teste_transforma_chave(chave):
        return transforma_chave(chave) % 26 == 0


main()
# %%
