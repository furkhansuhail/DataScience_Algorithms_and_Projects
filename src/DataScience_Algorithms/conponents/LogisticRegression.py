from src.DataScience_Algorithms.constants import *
from src.DataScience_Algorithms.utils.ImportsModule import *

class LogisticRegression:
    def __init__(self, x, y, targetValue, weight, bias, learning_rate, epochs):
        self.x = np.array(x)
        self.y = np.array(y)
        self.n = len(self.x)
        self.targetValue = np.array(targetValue)
        self.w = weight  # initial weight
        self.b = bias    # initial bias
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.train()
        # self.result = self.predict(targetValue)  # Save result, don't return in __init__

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def compute_loss(self, y_true, y_pred):
        # Binary Cross-Entropy Loss
        return -np.mean(y_true * np.log(y_pred + 1e-9) + (1 - y_true) * np.log(1 - y_pred + 1e-9))

    def train(self):
        print("Training started...")
        for epoch in range(self.epochs):
            # Linear model: z = w * x + b
            linear_model = np.dot(self.x, self.w) + self.b
            predictions = self.sigmoid(linear_model)

            # Compute gradients
            dw = np.mean((predictions - self.y) * self.x, axis=0)  # For multiple features
            db = np.mean(predictions - self.y)

            # Update weights
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

            if epoch % 100 == 0:
                loss = self.compute_loss(self.y, predictions)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict_proba(self, x_input):
        x_input = np.array(x_input)
        linear_model = np.dot(x_input, self.w) + self.b
        return self.sigmoid(linear_model)

    def predict(self, targetValue):
        proba = self.predict_proba(targetValue)
        print(proba)
        return 1 if proba >= 0.5 else 0


