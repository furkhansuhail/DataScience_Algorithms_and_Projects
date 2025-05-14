from src.DataScience_Algorithms.conponents.LinearRegression import LinearRegression
from src.DataScience_Algorithms.utils.ImportsModule import *
# from src.DataScience_Algorithms.logging import logger


class LinearRegression_Execution:
    def __init__(self, x, y, ValueTOPredict):
        self.x_inputs = np.array(x)    # [1, 2, 3, 4, 5]
        self.y_inputs = np.array(y)    # [3, 5, 7, 9, 11]
        self.ValueTOPredict = ValueTOPredict
        self.predicted_value = None
        self.main()

    def main(self):
        print(self.x_inputs, self.y_inputs, self.ValueTOPredict)
        LinearRegressionObj = LinearRegression(self.x_inputs, self.y_inputs, self.ValueTOPredict)
        LinearRegressionObj.RequiredCalculations()
        LinearRegressionObj.CalculatingSlope_Intercept()
        self.predicted_value = LinearRegressionObj.Prediction(self.ValueTOPredict[0])
        # PredictedValue = LinearRegressionObj.Prediction(self.ValueTOPredict[0])
        # print(PredictedValue)
        # return self.predicted_value