import math, pygame, random

pygame.init()

width = 800
height = 600
running = True



class NeuralNetwork():
    def __init__(self, ip, h, op): # h will be a list with a length of the num of hidden layers and the items in h will be the num of neurons of that hidden layer
        self.n_inputs = ip
        self.n_h_layers = len(h)
        self.n_neurons_h_layers = h
        self.n_outputs = op
        self.h_layers = []
        self.weights = [] # has [layer_num][neuron_num][neuron_value]
        self.biases = []
        self.inputs = []
        self.activations = [] # of the hidden layers and the output layer

    def init_wb(self):
        for m in range(self.n_h_layers): # adds weights and biases of each hidden layer
            temp_lst = []
            for n in range(self.n_neurons_h_layers[m]): # adds weights of each neuron of the hidden layer
                temp_lst.append([])
            self.weights.append(temp_lst.copy())
            self.biases.append([])
            self.activations.append([])
        temp_lst = []
        for m in range(self.n_outputs): # adds weights and biases of the output layer
            temp_lst.append([])
        self.weights.append(temp_lst.copy())
        self.biases.append([])
        self.activations.append([])

        for m in range(len(self.weights[0])): # neuron count of the hidden layer right after the input layer
            for n in range(self.n_inputs): # neuron count of the input layer
                self.weights[0][m].append(random.randint(-100, 100))
            self.biases[0].append(random.randint(-100, 100))
            self.activations[0].append(0)
        for m in range(1, len(self.weights)): # layer num
            for n in range(len(self.weights[m])): # neuron num of the layer
                for o in range(len(self.weights[m - 1])): # num of neurons of the prev layer (num of weights connected to this neuron)
                    self.weights[m][n].append(random.randint(-100, 100))
                self.biases[m].append(random.randint(-100, 100))
                self.activations[m].append(0)

    def show(self):
        # show weights
        for m in range(self.n_inputs):
            for n in range(len(self.weights[0])): # neuron of the layer
                for o in range(len(self.weights[0][n])): # pos of weight of a neuron
                    if self.weights[0][n][o] < 0:
                        clr = (2 * abs(self.weights[0][n][o]), 0, 0)
                    else:
                        clr = (0, 2 * self.weights[0][n][o], 0)
                    x_pos_2 = 2 * width / (len(self.weights) + 2) # width / (num of layers + 1)
                    y_pos_2 = (n + 1) * height / (len(self.weights[0]) + 1)
                    pygame.draw.line(scrn, clr, (width / (len(self.weights) + 2), (o + 1) * height / (self.n_inputs + 1)), (x_pos_2, y_pos_2), 4)

        for m in range(1, len(self.weights)):
            for n in range(len(self.weights[m])):
                for o in range(len(self.weights[m][n])):
                    if self.weights[m][n][o] < 0:
                        clr = (2 * abs(self.weights[m][n][o]), 0, 0)
                    else:
                        clr = (0, 2 * self.weights[m][n][o], 0)
                    x_pos_2 = (m + 2) * width / (len(self.weights) + 2) # width / (num of layers + 1)
                    y_pos_2 = (n + 1) * height / (len(self.weights[m]) + 1)
                    pygame.draw.line(scrn, clr, ((m + 1) * width / (len(self.weights) + 2), (o + 1) * height / (len(self.weights[m - 1]) + 1)), (x_pos_2, y_pos_2), 4)

        # show neurons
        for m in range(self.n_inputs):
            pygame.draw.circle(scrn, (255, 255, 255),(width / (len(self.weights) + 2), (m + 1) * height / (self.n_inputs + 1)) , 20) # the x pos is width / (num of layers + 1)

        for m in range(len(self.weights)):
            for n in range(len(self.weights[m])):
                clr = (255, 255, 255)
                x_pos = (m + 2) * width / (len(self.weights) + 2) # width / (num of layers + 1)
                y_pos = (n + 1) * height / (len(self.weights[m]) + 1)
                pygame.draw.circle(scrn, clr, (x_pos, y_pos), 20)

    def sigmoid(self, x):
        return 1 / (1 + math.e ** (-x))

    def relu(self, x):
        return (x + abs(x)) / 2

    def feedForward(self, a):
        self.inputs = a
        for m in range(len(self.weights[0])): # neuron of the layer right after the input layer
            z = 0
            for n in range(len(self.weights[0][m])): # each weight pos
                z += self.weights[0][m][n] * self.inputs[n]
            z += self.biases[0][m]
            self.activations[0][m] = self.relu(z)
        for m in range(1, len(self.weights)): # layer
            for n in range(len(self.weights[m])): # neuron of that layer
                z = 0
                for o in range(len(self.weights[m][n])): # weight pos of the neuron
                    z += self.weights[m][n][o] * self.activations[m - 1][o]
                z += self.biases[m][n]
                self.activations[m][n] = self.relu(z)
        print("weights:", self.weights, '\n', "biases:", self.biases)
        return self.activations



scrn = pygame.display.set_mode((width, height))

ann = NeuralNetwork(2, [4, 4], 3)
ann.init_wb()
print(ann.feedForward([1, 2]))

while running:
    scrn.fill((100, 100, 255))
    ann.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
