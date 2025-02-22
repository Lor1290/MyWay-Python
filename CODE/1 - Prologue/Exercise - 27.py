def remove_double(lista):
    lista_nuova = []
    _set_ = set()
    for i in lista:
        _set_.add(i)
    lista_nuova.append(_set_)
    return lista_nuova

squadra = ["palla", "palla", "palla", "pallonetto", "calcetto", "corso"]
definizione = remove_double(squadra)
for i in definizione:
    print(i)


