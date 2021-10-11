# Implementação simplificada do map


def mapear(funcao, lista):
    for elemento in lista:
        print('passando por aqui...')
        yield funcao(elemento)


if __name__ == '__main__':
    # primos = [2, 3, 5, 7, 11]
    # print(mapear(lambda x: x ** 3, primos))
    # print(map(lambda x: x ** 3, primos))

    # print(list(mapear(lambda x: x ** 3, primos)))

    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(list(resultado))
