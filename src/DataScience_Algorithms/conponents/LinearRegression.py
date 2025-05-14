from src.DataScience_Algorithms.constants import *
from src.DataScience_Algorithms.utils.ImportsModule import *


class LinearRegression():
    def __init__(self, x, y, targetValue):
        self.x = x
        self.y = y
        self.n = None
        self.sum_x = None
        self.sum_y = None
        self.sum_xy = None
        self.sum_x_square = None
        self.Intercept = None


    def RequiredCalculations(self):
        self.n = len(self.x)
        self.sum_x = np.sum(self.x)
        self.sum_y = np.sum(self.y)
        self.sum_xy = np.sum(self.x * self.y)
        self.sum_x_square = np.sum(self.x ** 2)
        self.slope = None

    def CalculatingSlope_Intercept(self):
        "m = n(sum(xy)- sum(x).sum(y)) / n(sum(x)^2 - (sum_x^2))"\
        # Calculating Slope
        numerator = self.n * self.sum_xy - self.sum_x * self.sum_y
        denominator = self.n * self.sum_x_square - (self.sum_x ** 2)
        self.slope = numerator/denominator

        # CalculatingIntercept
        "c = sumy - m * sumx / n "
        self.intercept = (self.sum_y - self.slope * self.sum_x) / self.n
        # print(self.slope)
        # print(self.intercept)

    def Prediction(self, targetValue):
        # now that we have m and c we can predict a value i.e y = mx + c
        return self.slope * targetValue + self.intercept


