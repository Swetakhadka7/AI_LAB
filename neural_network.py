import numpy as np

# Step function
def step_function(x):
    return 1 if x >= 0 else 0

# Perceptron class
class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.randn(input_size + 1)  # Initialize weights randomly (including bias)
    
    def predict(self, inputs):
        # Add bias input (always 1)
        inputs = np.insert(inputs, 0, 1)
        # Weighted sum and activation
        weighted_sum = np.dot(self.weights, inputs)
        return step_function(weighted_sum)
    
    def train(self, training_inputs, labels, epochs=100, learning_rate=0.1):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                # Add bias input (always 1)
                inputs = np.insert(inputs, 0, 1)
                prediction = self.predict(inputs[1:])
                error = label - prediction
                # Update weights
                self.weights += learning_rate * error * inputs

# Training data for AND logic gate
training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])  # Output for AND gate

# Initialize perceptron with 2 inputs (for the AND gate)
perceptron = Perceptron(input_size=2)

# Train the perceptron
perceptron.train(training_inputs, labels, epochs=100)

# Test the perceptron on the same data
for inputs in training_inputs:
    prediction = perceptron.predict(inputs)
    print(f"Input: {inputs}, Prediction: {prediction}")
