import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, a teoria das cores no design é o estudo da combinação e aplicação das cores para criar efeitos visuais desejados, seja para transmitir uma mensagem, evocar emoções ou simplesmente tornar um design mais atraente.')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, cores complementares são aquelas que se encontram em posições opostas no círculo cromático. Quando combinadas, elas criam um alto contraste e um forte impacto visual. Exemplos incluem azul e laranja, vermelho e verde, e amarelo e violeta.')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, cores análogas são aquelas que estão próximas umas das outras no círculo cromático. Elas criam uma sensação de harmonia e suavidade.')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, a temperatura da cor refere-se à sensação visual de calor ou frieza que uma cor transmite. Cores quentes (como vermelho, laranja e amarelo) são associadas a sentimentos de excitação e energia, enquanto cores frias (como azul, verde e violeta) são associadas a sentimentos de calma e serenidade.')
    elif resposta == '5':
        exit()
    else:
        print('Digite apenas 1, 2, 3, 4 ou 5 para sair.')

def start():
    print('Olá! Sou o chatbot da teoria das cores. :)')
    nome = input('Digite o seu nome: ')

    while True:
        resposta = input(
        f'O que voce quer saber hj? {os.linesep}'
        f'[1] - O que é a teoria das cores no design? {os.linesep}'
        f'[2] O que são cores complementares? {os.linesep}'
        f'[3] - O que são cores análogas? {os.linesep}'
        f'[4] - O que é a temperatura da cor? {os.linesep}'
        f'[5] - Sair {os.linesep}')
        
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()