# 'dataset' tem os dados de entrada para este script
import pandas as pd
import os


def find_quartile(lista: list) -> dict:
    amostragem = sorted(lista)
    indice_principal = int(len(amostragem)/2)
    # Declara lista Inferior, geral e superior para calcular o quartil
    consolidado = [amostragem[: indice_principal],
                   amostragem, amostragem[indice_principal:]]
    dicionario = {}
    for idx, lista in enumerate(consolidado):
        i = int(len(lista)/2)
        if len(lista) % 2 == 0:
            q = (lista[i] + lista[i + 1]) / 2
        else:
            q = lista[i]

        dicionario[f'{idx + 1}º Quartil'] = q

    return dicionario


if __name__ == '__main__':
    # amostragem = [73, 74, 77, 52, 85, 59, 73, 84, 92]
    amostragem = [6, 47, 49, 15, 42, 41, 7, 39, 43, 40, 36]
    
    dicionario = encontra_quartil(amostragem)
    quartil = []
    for valor in amostragem:
        if valor < dicionario['1º Quartil']:
            quartil.append('1º Quartil')
        elif valor < dicionario['2º Quartil']:
            quartil.append('2º Quartil')
        elif valor < dicionario['3º Quartil']:
            quartil.append('3º Quartil')
        else:
            quartil.append('4º Quartil')
    df['Quartil'] = quartil
