weight = [2,-2]
sum = 0
class Perceptron:
    def __init__(self):
        self.sum = sum
        self.weight = weight


    def sign(self, n):
        self.n = n
        if n >=0:
            return 1
        else:
            return -1
    
    
    def output_perc(self, input=[2]):
        for i in range(len(self.weight)):
            self.sum += input[i]*self.weight[i]
        output = self.sign(self.sum)
        return output

    def train(self, input, output, target):
        lr = 0.106
        error = target - output
        for i in range(len(self.weight)):
            self.weight[i] += error * input[i] * lr

            




