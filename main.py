pizza_1 = 'pepperoni'
pizza_2 = 'queijo'
pizza_3 = 'calabresa'

preco_1 = 80
preco_2 = 50
preco_3 = 70

pedido1 = ''
pedido2 = ''

pedido1 = input('Digite o seu pedido: ')

valor_total = 0

if pedido1 == pizza_1 or pedido1 == pizza_2 or pedido1 == pizza_3:
    
    if pedido1 == pizza_1:
        valor_total += preco_1
    elif pedido1 == pizza_2:
        valor_total += preco_2
    elif pedido2 == pizza_3:
        valor_total += preco_3
    nova_pizza = input('Deseja pedir outra pizza? [S/N] ').upper()
    if nova_pizza == 'S':
        
        pedido2 = input('Digite o seu pedido: ')
        
        if pedido2 == pizza_1 or pedido2 == pizza_2 or pedido2 == pizza_3:
            if pedido2 == pizza_1:
                valor_total += preco_1
            elif pedido2 == pizza_2:
                valor_total += preco_2
            elif pedido2 == pizza_3:
                valor_total += preco_3
        
        print(f'As pizzas pedidas foram: {pedido1} e {pedido2}, custaram o total R$ {valor_total}')

    else:
        
        print(f'A pizza pedida foi: {pedido1}, custou R$ {valor_total}')

else:
    print('Pedido inválido\nEncerrando o chat!')