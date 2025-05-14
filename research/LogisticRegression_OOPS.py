import numpy as np


class LogisticRegression:
    def __init__(self):
        self.x = np.array([1, 2, 3, 4, 5])
        self.y = np.array([0, 0, 0, 1, 1])
        self.n = len(self.x)

        # Initialize weights (slope and intercept)
        self.w = 0.0  # weight
        self.b = 0.0  # bias/intercept
        self.learning_rate = 0.1
        self.epochs = 1000

        self.train()

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def compute_loss(self, y_true, y_pred):
        # Binary Cross-Entropy Loss
        return -np.mean(y_true * np.log(y_pred + 1e-9) + (1 - y_true) * np.log(1 - y_pred + 1e-9))

    def train(self):
        for epoch in range(self.epochs):
            linear_model = self.w * self.x + self.b
            predictions = self.sigmoid(linear_model)

            # Compute gradients
            dw = np.mean((predictions - self.y) * self.x)
            db = np.mean(predictions - self.y)

            # Update weights
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

            # Print loss every 100 epochs
            if epoch % 100 == 0:
                loss = self.compute_loss(self.y, predictions)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict_proba(self, x_input):
        linear_model = self.w * x_input + self.b
        return self.sigmoid(linear_model)

    def predict(self, x_input):
        proba = self.predict_proba(x_input)
        return [1 if p >= 0.5 else 0 for p in proba]


# Run the logistic regression model
logreg = LogisticRegression()

# Make a prediction for a new input
x_test = np.array([1, 2, 3, 4, 5, 6])
probas = logreg.predict_proba(x_test)
predictions = logreg.predict(x_test)

print("\nProbabilities:", probas)
print("Predicted Classes:", predictions)