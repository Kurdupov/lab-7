while True:
    while True:
        try:
          y=int(input('Введіть вартість 1 товара'))
          x=int(input('Введіть вартість  2 товара'))
          break
        except ValueError:
            print('Введіть число')
    d=input('Введіть продавця 1 ')
    v=input('Введіть продавця 2 ')
    p=input('Введіть товар 1 ')
    m=input('Введіть товар 2 ')
    keys=['Продавець','Назва','Кількість','Ціна','Дата']
    a=[d,p,input('Введіть кількість товара 1 '),y,input('Введіть число ')]
    b=[v,m,input('Введіть кількість товара 2 '),x,input('Введіть число ')]
    slov={keys:a for(keys,a) in zip(keys,a) if d=='Иванов'}
    slov2={keys:b for(keys,b) in zip(keys,b) if v=='Иванов'}
    print(slov,slov2)
    if y<x:
        print('максимальна вартість у',m)
    else:
        print('максимальная вартість у',p)
    result = input('Хотите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break