import math, pygame, random, time

pygame.init()

width = 800
height = 600
running = True
trainings = 10000
tests = 1000
correct = 0
wrong = {}

class NeuralNetwork:
    def __init__(self, n): # has [number of neurons in the layer]
        self.n = len(n)
        self.all_neurons = n
        self.n_i_neurons = n[0]
        self.n_h_layers = self.n - 2
        self.n_h_neurons = n[1: -1]
        self.n_o_neurons = n[-1]
        self.weights = [] # has [layer_num][neuron_num][prev_layer_neuron_num]
        self.biases = [] # has [layer_num][neuron_num]
        self.z_lst = []
        self.activations = [] # of all the layers
        self.costs = []
        self.change_weights = []
        self.change_biases = []

        for i in range(self.n):
            if i != 0:
                temp_lst_1 = []
                temp_lst_2 = []
                for j in range(n[i]):
                    temp_lst_1.append([random.randint(-100, 100) / 100 for k in range(n[i - 1])])
                    temp_lst_2.append([0 for k in range(n[i - 1])])
                self.weights.append(temp_lst_1.copy())
                self.change_weights.append(temp_lst_2.copy())
                temp_lst_1.clear()
                temp_lst_2.clear()

                self.biases.append([random.randint(-100, 100) / 100 for j in range(n[i])])
                self.change_biases.append([0 for j in range(n[i])])
                self.z_lst.append([0 for j in range(n[i])])
            self.activations.append([0 for j in range(n[i])])
            if i == self.n - 1:
                self.costs = [0 for j in range(n[i])]

    def show(self, screen, canvas):
        for i in range(self.n):
            for j in range(self.all_neurons[i]):
                temp_coor_1 = (canvas[0] * (i + 1 / 2) / self.n, canvas[1] * (j + 1 / 2) / self.all_neurons[i])
                if i != 0:
                    for k in range(self.all_neurons[i - 1]):
                        temp_coor_2 = (canvas[0] * (i - 1 / 2) / self.n, canvas[1] * (k + 1 / 2) / self.all_neurons[i - 1])
                        temp_clr = 255 * (2 * sigmoid(abs(self.weights[i - 1][j][k])) - 1)
                        if self.weights[i - 1][j][k] < 0:
                            pygame.draw.line(screen, (temp_clr, 0, 0), temp_coor_1, temp_coor_2, 2)
                        else:
                            pygame.draw.line(screen, (0, temp_clr, 0), temp_coor_1, temp_coor_2, 2)
        for i in range(self.n):
            for j in range(self.all_neurons[i]):
                shade = 255 * self.activations[i][j]
                pygame.draw.circle(screen, (shade, shade, shade), (canvas[0] * (i + 1 / 2) / self.n, canvas[1] * (j + 1 / 2) / self.all_neurons[i]), 20)

        for i in range(1, self.n):
            for j in range(self.all_neurons[i]):
                temp_clr = 255 * (2 * sigmoid(abs(self.biases[i - 1][j])) - 1)
                if self.biases[i - 1][j] < 0:
                    pygame.draw.circle(screen, (temp_clr, 0, temp_clr), (canvas[0] * (i + 1 / 2) / self.n, canvas[1] * (j + 1 / 2) / self.all_neurons[i] - 32), 10)
                else:
                    pygame.draw.circle(screen, (temp_clr, temp_clr, 0), (canvas[0] * (i + 1 / 2) / self.n, canvas[1] * (j + 1 / 2) / self.all_neurons[i] - 32), 10)

    def feedForward(self, input_lst):
        for i in range(self.all_neurons[0]):
            self.activations[0][i] = sigmoid(input_lst[i])

        for i in range(1, self.n):
            for j in range(self.all_neurons[i]):
                temp = 0
                for k in range(self.all_neurons[i - 1]):
                    temp += self.activations[i - 1][k] * self.weights[i - 1][j][k] + self.biases[i - 1][j]
                self.z_lst[i - 1][j] = temp
                self.activations[i][j] = sigmoid(self.z_lst[i - 1][j])

    def calcCosts(self, ans):
        for i in range(self.all_neurons[-1]):
            self.costs[i] = (ans[i] - self.activations[-1][i]) ** 2

    def backProp(self, ans, learning_rate):
        for i in range(1, self.n): # layer num
            for j in range(self.all_neurons[i]): # "i" layer's neuron num
                for k in range(self.all_neurons[i - 1]): # "i - 1" layer's neuron num
                    self.change_weights[i - 1][j][k] = self.pD_C_w(i, j, k, ans)
                self.change_biases[i - 1][j] = self.pD_C_b(i, j, ans)

        for i in range(1, self.n): # layer num
            for j in range(self.all_neurons[i]): # "i" layer's neuron num
                for k in range(self.all_neurons[i - 1]): # "i - 1" layer's neuron num
                    self.weights[i - 1][j][k] -= learning_rate * self.change_weights[i - 1][j][k]
                self.biases[i - 1][j] -= learning_rate * self.change_biases[i - 1][j]

    def pD_C_a(self, m, k, ans): # pD_C_a ==> partial differential of cost with respect to activation
        if m < self.n - 1:
            temp = 0
            for i in range(self.all_neurons[m + 1]):
                temp += self.pD_C_a(m + 1, i, ans) * sigmoid(self.z_lst[m][i]) * sigmoid(-self.z_lst[m][i]) * self.weights[m][i][k]
            return temp
        else:
            return 2 * (self.activations[-1][k] - ans[k])

    def pD_C_w(self, m, k, j, ans): # pD_C_w ==> partial differential of cost with respect to weight
        return self.pD_C_a(m, k, ans) * sigmoid(self.z_lst[m - 1][k]) * sigmoid(-self.z_lst[m - 1][k]) * self.activations[m - 1][j]

    def pD_C_b(self, m, k, ans): # pD_C_b ==> partial differential of cost with respect to bias
        return self.pD_C_a(m, k, ans) * sigmoid(self.z_lst[m - 1][k]) * sigmoid(-self.z_lst[m - 1][k])

    def best(self):
        temp = 0
        for i in range(self.all_neurons[-1]):
            if self.activations[-1][i] > self.activations[-1][temp]:
                temp = i
        return temp

scrn = pygame.display.set_mode((width, height))

def sigmoid(x):
    try:
        return 1 / (1 + math.e ** (-x))
    except:
        return 0

def relu(x):
    return (x + abs(x)) / 2

# ann_1 = NeuralNetwork([1, 3])
ann_1 = NeuralNetwork([1, 3, 3, 3])
# print("weights", ann_1.weights)
# print("biases", ann_1.biases)
# print("z", ann_1.z_lst)
# print("a", ann_1.activations)
# print("costs", ann_1.costs)
# print("change_weights", ann_1.change_weights)
# print("change_biases", ann_1.change_biases)

for i in range(trainings):
    test_num = random.randint(-100, 100)
    ann_1.feedForward([test_num])
    if test_num < 0:
        ann_1.calcCosts([1, 0, 0])
        ann_1.backProp([1, 0, 0], 0.1)
    elif test_num == 0:
        ann_1.calcCosts([0, 1, 0])
        ann_1.backProp([0, 1, 0], 0.1)
    else:
        ann_1.calcCosts([0, 0, 1])
        ann_1.backProp([0, 0, 1], 0.1)

for i in range(tests):
    test_num = random.randint(-100, 100)
    ann_1.feedForward([test_num])
    if ann_1.activations[-1][0] > ann_1.activations[-1][1] and ann_1.activations[-1][0] > ann_1.activations[-1][2]:
        if test_num < 0:
            correct += 1
        else:
            wrong[test_num] = ann_1.activations[-1]
    elif ann_1.activations[-1][2] > ann_1.activations[-1][0] and ann_1.activations[-1][2] > ann_1.activations[-1][1]:
        if test_num > 0:
            correct += 1
        else:
            wrong[test_num] = ann_1.activations[-1]
    else:
        if test_num == 0:
            correct += 1
        else:
            wrong[test_num] = ann_1.activations[-1]

print(correct, "/", tests)
# for i in wrong:
#     print(i, wrong[i])

while running:
    scrn.fill((200, 200, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ann_1.show(scrn, (width, height))

    pygame.display.update()
    time.sleep(1)

pygame.quit()
print("weights", ann_1.weights)
print("biases", ann_1.biases)