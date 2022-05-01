weight = [2,-2]
sum = 0


class Perceptron:
    def __init__(self):
        self.sum    = sum
        self.weight = weight


    def sign(self, n):
        self.n = n
        return 1 if n >= 0 else -1
    
    
    def output_perc(self, input_=[2]):
        for i in range(len(self.weight)):
            self.sum += input_[i] * self.weight[i]
        
        return self.sign(self.sum)


    def train(self, input_, output, target):
        lr    = 0.106
        error = target - output
        for i in range(len(self.weight)):
            self.weight[i] += error * input_[i] * lr
