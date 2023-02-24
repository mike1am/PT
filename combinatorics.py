from math import factorial


# возвращает число сочетаний selNum из totalNum
def combNum(totalNum, selNum):
    return int(factorial(totalNum) / factorial(selNum) / factorial(totalNum - selNum))


# возвращает число размещений selNum в totalNum
def placeNum(totalNum, selNum):
    return int(factorial(totalNum) / factorial(totalNum - selNum))


# возвращает число перестановок в totalNum
def permNum(totalNum):
    return factorial(totalNum)


# возвращает вероятность, рассчитанную по формуле Байеса
def bayes(p_ba, p_a, p_b):
    return p_ba * p_a / p_b


# возвращает полную вероятность при xNum равновероятных связанных событиях
# xList - список вероятностей зависимых событий
def symFullProb(xNum, xList):
    res = 0
    for i in range(xNum):
        res += (1 / xNum) * xList[i]

    return res