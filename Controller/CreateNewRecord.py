def createNewRecord():
    print('\n - - - - ->  Добавление новой строки расхода')
    category = input('Введите категорию: ')
    product = input('Введите название продукта: ')
    price = input('Введите цену: ')
    dateBuy = input('Введите дату: ')
    return (f'{category}, {product}, {price}, {dateBuy}')