import numpy as np


class Perceptron:
    def __init__(self, eta, epochs):
        self.weights = np.random.randn(3) * 1e-4  # NEED 3 WEIGHTS RANDOM_NORMAL SMALL VALUE
        self.eta = eta  # LEARNING RATE
        self.epochs = epochs
        print(f"Initial weights before training: {self.weights}")  
    
    def activationFunction(self, inputs, weights):
        z = np.dot(inputs, weights)  # z = w1x1 + w2x2 + w3x3 || z = W * X

        return np.where(z > 0, 1, 0)  # CONDITION, IF TRUE, ELSE
    
    def fit(self, x, y):
        self.x = x
        self.y = y

        # Concatenate x with bias (-1)
        self.x_with_bias = np.c_[self.x, -np.ones((len(self.x), 1))]
        print(f"x with bias: \n{self.x_with_bias}")

        for epoch in range(1, self.epochs+1):    # Start counting from 1
            print("--" * 10)
            print(f"For epoch: {epoch}/{self.epochs}")
            print("--" * 10)

            y_hat = self.activationFunction(self.x_with_bias, self.weights)  # forward propagation
            print(f"Predicted value after forward pass: {y_hat}")

            self.error = self.y - y_hat
            print(f"Error: \n{self.error}")

            initial_weights = self.weights
            self.weights = self.weights + self.eta * np.dot(self.x_with_bias.T, self.error)  # backward propagation
            final_weights = self.weights

            print("--" * 10)
            print(f"Total loss: {self.totalLoss()}")

            if(np.array_equal (initial_weights, final_weights)):
                break

            print(f"Updated weights after epoch{epoch}/{self.epochs}: {self.weights}")
            print("###" * 10)


    def predict(self, x):
        # Prediction is same as forward propagation. Just data varies

        # Predict on new set of x_with_bias
        # Use just 'x' and not 'self.x'. 'self.x' will refer to x input in fit() which might have diff val & dim
        # Concatenate x with bias (-1)
        self.x_with_bias = np.c_[x, -np.ones((len(x), 1))]  

        return self.activationFunction(self.x_with_bias, self.weights)  # Final updated weights after fit()

    def totalLoss(self):
        total_loss = np.sum(self.error)

        return total_loss