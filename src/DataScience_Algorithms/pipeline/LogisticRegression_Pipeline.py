from src.DataScience_Algorithms.conponents.LinearRegression import LinearRegression
from src.DataScience_Algorithms.conponents.LogisticRegression import LogisticRegression
from src.DataScience_Algorithms.utils.ImportsModule import *
# from src.DataScience_Algorithms.logging import logger


class LogisticRegression_Execution:
    def __init__(self, x, y, ValueTOPredict, weight_LogReg, bias_LogReg,
                    LearningRate, Epochs):
        self.x_inputs = np.array(x)    # [1, 2, 3, 4, 5]
        self.y_inputs = np.array(y)    # [3, 5, 7, 9, 11]
        # Initialize weights (slope and intercept)
        self.w = weight_LogReg#0.0  # weight
        self.b = bias_LogReg # 0.0  # bias/intercept
        self.learning_rate = LearningRate # 0.1
        self.epochs = Epochs #1000

        self.ValueTOPredict = ValueTOPredict
        self.predicted_value = None
        self.main()

    def main(self):
        print(self.x_inputs, self.y_inputs, self.ValueTOPredict)
        LinearRegressionObj = LogisticRegression(self.x_inputs, self.y_inputs, self.ValueTOPredict,
                                                 self.w, self.b, self.learning_rate, self.epochs)

        self.predicted_value = LogisticRegression.train(self.ValueTOPredict[0])
        print(self.predicted_value)
        return self.predicted_value