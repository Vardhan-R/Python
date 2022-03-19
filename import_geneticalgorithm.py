import random
import import_ann as ann

def rep(a, b, average = False):
    new_org = ann.NeuralNetwork(a.all_neurons)
    if average:
        for i in range(len(a.weights)):
            for j in range(len(a.weights[i])):
                for k in range(len(a.weights[i][j])):
                    new_org.weights[i][j][k] = (a.weights[i][j][k] + b.weights[i][j][k]) / 2
        for i in range(len(a.biases)):
            for j in range(len(a.biases[i])):
                new_org.biases[i][j] = (a.biases[i][j] + b.biases[i][j]) / 2
    else:
        for i in range(len(a.weights)):
            for j in range(len(a.weights[i])):
                for k in range(len(a.weights[i][j])):
                    if random.choice([0, 1]):
                        new_org.weights[i][j][k] = a.weights[i][j][k]
                    else:
                        new_org.weights[i][j][k] = b.weights[i][j][k]
        for i in range(len(a.biases)):
            for j in range(len(a.biases[i])):
                if random.choice([0, 1]):
                    new_org.biases[i][j] = a.biases[i][j]
                else:
                    new_org.biases[i][j] = b.biases[i][j]
    return new_org

def mutate(a, r):
    mutated_org = ann.NeuralNetwork(a.all_neurons)
    for i in range(len(a.weights)):
        for j in range(len(a.weights[i])):
            for k in range(len(a.weights[i][j])):
                c = random.randrange(0, 10 ** 10) / 10 ** 10
                if c < r:
                    mutated_org.weights[i][j][k] = random.randint(-100, 100) / 100
                else:
                    mutated_org.weights[i][j][k] = a.weights[i][j][k]

    for i in range(len(a.biases)):
        for j in range(len(a.biases[i])):
            c = random.randrange(0, 10 ** 10) / 10 ** 10
            if c < r:
                mutated_org.biases[i][j] = random.randint(-100, 100) / 100
            else:
                mutated_org.biases[i][j] = a.biases[i][j]

    return mutated_org