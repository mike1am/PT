import math


# расчёт среднего значения для выборки
# valList - выборка сл. величины
def meanVal(valList):
    res = 0
    for val in valList:
        res += val
    res /= len(valList)
    return res


# расчёт дисперсии для выборки
# valList - выборка сл. величины
# isShifted - признак смещённой (True) либо несмещённой (False) дисперсии
def dispersion(valList, isShifted=False):
    res = 0
    mean = meanVal(valList)
    for val in valList:
        res += (val - mean)**2
    res /= len(valList) - int(not isShifted)
    return res


# расчёт несмещённого СКО для выборки
# valList - выборка сл. величины
def stdDev(valList):
    return math.sqrt(dispersion(valList))