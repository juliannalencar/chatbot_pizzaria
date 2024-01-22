pizza_1 = 'pepperoni'
pizza_2 = 'queijo'
pizza_3 = 'calabresa'

preco_1 = 80
preco_2 = 50
preco_3 = 70

pedido = ''
compras = ''
valor_total = 0

resposta = 'S'

while resposta == 'S':

    pedido = input('\nPedido do Cliente: ')

    if pedido == pizza_1 or pedido == pizza_2 or pedido == pizza_3:

        if pedido == pizza_1:
            valor_total += preco_1
        elif pedido == pizza_2:
            valor_total += preco_2
        elif pedido == pizza_3:
            valor_total += preco_3

        compras += pedido + ', '
    
    resposta = input('Deseja pedir outra pizza? [S/N] ').upper()

print(f'As pizzas pedidas foram: {compras[:-2]}, custaram o total R$ {valor_total}')
