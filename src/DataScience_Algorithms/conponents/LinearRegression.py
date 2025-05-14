from src.DataScience_Algorithms.constants import *
from src.DataScience_Algorithms.utils.ImportsModule import *

class LinearRegression:
    def __init__(self, x, y, targetValue):
        self.x = np.array(x)
        self.y = np.array(y)
        self.n = None
        self.sum_x = None
        self.sum_y = None
        self.sum_xy = None
        self.sum_x_square = None
        self.Intercept = None
        self.RequiredCalculations()
        self.CalculatingSlope_Intercept()

    def RequiredCalculations(self):
        self.n = len(self.x)
        self.sum_x = np.sum(self.x)
        self.sum_y = np.sum(self.y)
        self.sum_xy = np.sum(self.x * self.y)
        self.sum_x_square = np.sum(self.x ** 2)
        self.slope = None

    def CalculatingSlope_Intercept(self):
        # Calculating Slope
        numerator = self.n * self.sum_xy - self.sum_x * self.sum_y
        denominator = self.n * self.sum_x_square - (self.sum_x ** 2)
        self.slope = numerator / denominator

        # Calculating Intercept
        self.intercept = (self.sum_y - self.slope * self.sum_x) / self.n

    def predict(self, targetValue):
        targetValue = np.array(targetValue)  # Ensure it's a numpy array
        if targetValue.ndim > 0:
            return self.slope * targetValue + self.intercept  # Vectorized operation for multiple values
        return self.slope * targetValue + self.intercept  # Scalar prediction for single value

