pizzas_disponiveis = 'pepperoni, queijo e calabresa'
preco_calabresa = 70.0
preco_queijo = 50.0
preco_pepperoni = 80.0

quantidade_calabresa = 0
quantidade_queijo = 0
quantidade_pepperoni = 0

print('Bem vindo a pizzaria da Ada')
deseja_prosseguir = input('Gostaria de realizar um pedido? (S/N)')


while deseja_prosseguir.lower() == 's':
    print("""
    ----------------------------------------
    Pizzas Disponíveis:
        1. Calabresa: R$ 70,00
        2. Queijo: R$ 50,00
        3. Pepperoni: R$ 80,00
    """)
    pedido = input('Qual pizza você gostaria?')

    # Validar o input das pizzas disponiveis
    if pedido in pizzas_disponiveis:
        if pedido == 'calabresa':
            quantidade_calabresa += 1
        elif pedido == 'queijo':
            quantidade_queijo += 1
        else:
            quantidade_pepperoni += 1
    else:
        print('Pedido inválido!')

    deseja_prosseguir = input('Gostaria de realizar mais um pedido? (S/N)')


preco_total = (quantidade_calabresa * preco_calabresa +
               quantidade_queijo * preco_queijo +
               quantidade_pepperoni * preco_pepperoni)
if preco_total > 0:
    print('Pedido realizado: ')
    if quantidade_calabresa > 0:
        print(f'{quantidade_calabresa}x Pizza de calabresa: '
              + f'R$ {quantidade_calabresa * preco_calabresa}')
    if quantidade_queijo > 0:
        print(f'{quantidade_queijo}x Pizza de queijo: '
              + f'R$ {quantidade_queijo * preco_queijo}')
    if quantidade_pepperoni > 0:
        print(f'{quantidade_pepperoni}x Pizza de pepperoni: '
              + f'R$ {quantidade_pepperoni * preco_pepperoni}')
    print('----------------------------------------')
    print('Preço total: R$', preco_total)

else:
    print('Nenhum pedido realizado! Fim do programa')
    print('----------------------------------------')