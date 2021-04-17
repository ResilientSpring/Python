import numpy as np
import sigmoid as s

def compute_prediction(X, weights):
    """Compute the prediction y_hat based on current weights"""

    z = np.dot(X, weights);
    predictions = s.sigmoid(z);

    return predictions;

def update_weights_gd(X_train, y_train, weights, learning_rate):
    """Update weights by one step"""

    predictions = compute_prediction(X=X_train, weights=weights);