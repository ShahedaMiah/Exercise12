import random
lottoSet = set()
while len(lottoSet) < 6:
    lottoSet.add(random.randint(1, 50))
    lottery = list(lottoSet)
print(lottery)

