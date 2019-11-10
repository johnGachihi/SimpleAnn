import numpy as np


class ANN:
    def __init__(self, learning_rate, weights):
        self.weights = weights
        self.learning_rate = learning_rate

    def train(self, input_data, output_target_data):
        for row, t in zip(input_data, output_target_data):
            output = self.__feedfoward(row)
            error = self.__outputerror(*output, t)

    def __feedfoward(self, input_data_row):
        outputs = input_data_row
        for w in self.weights:
            print(w, outputs)
            outputs = np.dot(w, outputs)
            outputs = [self.__sigmoid(x) for x in outputs]
        print(outputs, '\n')
        return outputs

    def __outputerror(self, modeloutput, actualoutput):
        return (actualoutput - modeloutput) * modeloutput * (1 - modeloutput)

    def __adjust_weights(self, output_error):


    @staticmethod
    def __sigmoid(num):
        return 1/(1 + np.exp(-num))