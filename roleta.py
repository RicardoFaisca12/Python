import random
print('--== ROLETA ==--')

carteira = int(input('Quando dinheiro tens para apostar: €'))
vermelho = 0
preto = 1
verde = 2
historico = [] #coming soon

while carteira > 0:
    
    cor = int(input('Queres apostar em que cor?  Vermelho [0]  Preto [1]  Verde [2]: '))
    aposta = int(input('Quanto dinheiro queres apostar: '))
    while aposta <= carteira:
        if cor == random.randint(0,2):
            carteira = carteira+aposta
            print('Ganhaste!  Dinheiro: ', carteira, '€')
            print('Historico de apostas', historico)
        else:
            carteira = carteira-aposta
            print('Perdeste!  Dinheiro: ', carteira, '€')
            print('Historico de apostas', historico)
if carteira <= 0:
    print('Nao tens mais dinheiro para apostar!')
