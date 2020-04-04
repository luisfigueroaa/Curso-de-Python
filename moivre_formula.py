import cmath
import math


def sacarRaices(c, n):
    """
    sacar_raices(complejo, indice) -> [raiz_1, raiz_2, ... , raiz_n]
    Devuelve todas las raíces de un radicando complejo con indice n
    Argumentos:
    c: radicando complejo
    n: indice de la raíz
    """

    plr = cmath.polar(c)

    angulo = plr[1]
    if angulo < 0:
        angulo += math.pi * 2

    raices = []
    raiz_radio = plr[0] ** (1. / n)

    for i in range(n):
        i_theta = (angulo + 2 * math.pi * i) / n
        raices.append(cmath.rect(raiz_radio, i_theta))

    return raices
# Fin función sacar_raices


print(sacarRaices(3, 4))
