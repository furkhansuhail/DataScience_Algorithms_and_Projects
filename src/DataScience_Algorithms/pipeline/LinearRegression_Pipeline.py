from src.DataScience_Algorithms.conponents.LinearRegression import LinearRegression
from src.DataScience_Algorithms.conponents.LogisticRegression import LogisticRegression
from src.DataScience_Algorithms.utils.ImportsModule import *
# from src.DataScience_Algorithms.logging import logger


class LinearRegression_Execution:
    def __init__(self, x, y, ValueTOPredict, weights, bias, learning_rate, epochs):
        self.x_inputs = np.array(x)    # [1, 2, 3, 4, 5]
        self.y_inputs = np.array(y)    # [3, 5, 7, 9, 11]
        self.ValueTOPredict = ValueTOPredict
        self.weights = weights
        self.bias = bias
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.predicted_value = None
        self.main()

    def main(self):
        print(self.x_inputs, self.y_inputs, self.ValueTOPredict)
        LogisticRegressionObj  = LogisticRegression(self.x_inputs, self.y_inputs, self.ValueTOPredict, self.weights,
                                                 self.bias, self.learning_rate, self.epochs)
        LogisticRegressionObj.train()
        self.predicted_value = LogisticRegressionObj.predict(self.ValueTOPredict)
        return self.predicted_value