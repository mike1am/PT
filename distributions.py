from math import factorial, exp
import combinatorics as cmb


# расчёт вероятности по формуле Бернулли
# n - общее число испытаний
# k - число наступлений события
# p - вероятность наступления события
def bernoulli(n, k, p):
    return cmb.combNum(n, k) * p**k * (1 - p)**(n - k)


# расчёт вероятности в распределении Пуассона
# n - общее число испытаний
# lmb - интенсивность наступления события
def poisson(lmb, n):
    return lmb**n / factorial(n) * exp(-lmb)


# возвращает картеж из 1 или 2 наиболее вероятных значений в биномиальном распределении
# n - общее число испытаний
# p - вероятность наступления события
def mostLikely(n, p):
    gt = n * p + p
    if gt % 1 != 0:
        return (int(gt // 1),)
    else:
        return (int(gt - 1), int(gt))   