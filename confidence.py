import distributions as dst


def isBinomCalc(n, p):
    return n * p <= 5 or n * (1 - p) <= 5


class confInterval:
    def __init__(self, left, right, cp):
        self.scopes = (left, right)
        self.level = cp


# расчёт довертельного интервала доли по форм. Бернулли
# возвращает объект confInterval
# n - размер выборки
# p - доля в выборке
# cp - заданная дов. вероятность
def bernInterval(n, p, cp):
    cumul = cumulNext = 0
    upperScope = 0
    while cumulNext < cp:
        cumul = cumulNext
        cumulNext += dst.bernoulli(n, int(n * p), p)
        upperScope += p

    upperScope -= p
    return confInterval(0, upperScope, cumul)