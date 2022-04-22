import perceptron
perc = perceptron.Perceptron()
input = []
dataset_x = [9, 2, 9.1, 3.2, 8.4, 1.6, 8, 3.1, 6.3, 3.4]
dataset_y = [70, 50, 74.6, 49.4, 74.6, 48.3, 72.8, 45.8, 91.4, 56.6]

for i in range(len(dataset_x)):
    input = [dataset_x[i], dataset_y[i]]
    if dataset_y[i] >= 60:
        target = -1
    else:
        target = 1
    output = perc.output_perc(input)
    perc.train(input, output, target)

input = [3, 30]
print(perc.output_perc(input))




