import perceptron


perc      = perceptron.Perceptron()
input_    = []
dataset_x = [9, 2, 9.1, 3.2, 8.4, 1.6, 8, 3.1, 6.3, 3.4]
dataset_y = [70, 50, 74.6, 49.4, 74.6, 48.3, 72.8, 45.8, 91.4, 56.6]


for i in range(len(dataset_x)):
    input_ = [dataset_x[i], dataset_y[i]]
    target = -1 if dataset_y[i] >= 60 else 1
    output = perc.output_perc(input_)
    
    perc.train(input_, output, target)


input_ = [3, 30]
print(perc.output_perc(input_))
