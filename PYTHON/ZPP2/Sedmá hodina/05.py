def computation(n, m):
    if n < 0:
        raise ValueError('n musí být kladné')
    if m < 0:
        raise ValueError('m musí být kladné')
    return n // m

def user_computation(n, m):
    print('Začátek výpočtu pro:', n, m)
    result = None
    try:
        result = computation(n, m)
    except ZeroDivisionError as e:
        print('Chyba dělení nulou:', e)
    except ValueError as e:
        print('Chyba hodnoty:', e)
   # except Exception as e:
   #     print('Jiná chyba:', e)
    else:
        print('Výsledek je:', result)
    finally:
        print('Konec výpočtu.')