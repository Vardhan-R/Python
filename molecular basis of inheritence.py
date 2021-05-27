import random

alleles = ["t", "T"]
genotypes = ["tt", "Tt", "Tt", "TT"]
parents = []
gametes = []
for i in range(2):
    parents.append(genotypes[random.randrange(0, len(genotypes))])
parents.sort()
print(parents)

def rep():
    for i in range(4 * len(parents)):
        gametes.append(parents[random.randrange(0, len(parents))][random.randrange(0, 2)])
    for i in range(0, len(gametes), 2):
        parents.append(gametes[i] + gametes[i + 1])
    for i in range(2):
        parents.pop(0)
    parents.sort()
    print(parents)

for i in range(2):
    rep()