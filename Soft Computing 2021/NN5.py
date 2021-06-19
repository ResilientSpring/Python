import sys
import numpy as np


class Particle_Swarm_Optimization(object):

    def __init__(self, number_of_units_in_the_hidden_layer=2, iterations=100, seed=None):
        self.random = np.random.RandomState(seed)
        self.number_of_hidden_units = number_of_units_in_the_hidden_layer
        self.iterations = iterations

    def _sigmoid(self, z):
        return 1.0 / (1 + np.exp(-z))

    def _forward(self, X):

        # step 1: net input of hidden layer
        # [n_examples, n_features] dot [n_features, n_hidden]
        # -> [n_examples, n_hidden]
        z_h = np.dot(X, self.w_h) + self.b_h

        # step 2: activation of hidden layer
        a_h = self._sigmoid(z_h)

        # step 3: net input of output layer
        # [n_examples, n_hidden] dot [n_hidden, n_classlabels]
        # -> [n_examples, n_classlabels]
        z_out = np.dot(a_h, self.w_out) + self.b_out

        # step 4: activation output layer
        a_out = self._sigmoid(z_out)

        return a_out

    def _compute_cost(self, y_true, output):
        """Compute cost function.
        Parameters
        ----------
        y_true : array, shape = (n_examples, n_labels)
            one-hot encoded class labels.
        output : array, shape = [n_examples, n_output_units]
            Activation of the output layer (forward propagation)
        Returns
        ---------
        cost : float
            cost
        """
        term1 = - y_true * (np.log(output + 1e-5))
        term2 = (1. - y_true) * np.log(1. - output + 1e-5)
        cost = np.sum(term1 - term2)

        return cost

    def predict(self, X):
        """Predict class labels
        Parameters
        -----------
        X : array, shape = [n_examples, n_features]
            Input layer with original features.
        Returns:
        ----------
        y_pred : array, shape = [n_examples]
            Predicted class labels.
        """
        chance = self._forward(X)

        y_pred = np.where(chance >= 0.5, 0, 1)
        return y_pred

    def fit(self, X_train, y_train, X_valid, y_valid):
        """ Learn weights from training data.
        Parameters
        -----------
        X_train : array, shape = [n_examples, n_features]
            Input layer with original features.
        y_train : array, shape = [n_examples]
            Target class labels.
        X_valid : array, shape = [n_examples, n_features]
            Sample features for validation during training
        y_valid : array, shape = [n_examples]
            Sample labels for validation during training
        Returns:
        ----------
        self
        """
        # n_output = np.unique(y_train).shape[0]  # number of class labels
        n_output = 1
        n_features = X_train.shape[1]

        ########################
        # Weight initialization
        ########################

        # weights for input -> hidden
        self.b_h = self.random.uniform(low=0.01, high=10.00, size=self.number_of_hidden_units)
        self.w_h = self.random.uniform(low=0.01, high=10.00,
                                       size=(n_features, self.number_of_hidden_units))

        # weights for hidden -> output
        self.b_out = self.random.uniform(low=0.01, high=10.00, size=n_output)
        self.w_out = self.random.uniform(low=0.01, high=10.00,
                                         size=(self.number_of_hidden_units, n_output))

        epoch_strlen = len(str(self.iterations))  # for progress formatting
        self.eval_ = {'cost': [], 'train_acc': [], 'valid_acc': []}

        # iterate over training epochs
        for i in range(1, self.iterations + 1):

            # forward propagation
            likelihood = self._forward(X_train)

            train_cost = self._compute_cost(y_true=y_train, output=likelihood)

            ##############################
            # Particle Swarm Optimization
            ##############################
            velocity_train = self.random.uniform(low=0.01, high=10.00,
                                                 size=[X_train.shape[0], X_train.shape[1]])

            c1 = c2 = 2


            #############
            # Evaluation
            #############

            # Evaluation after each epoch during training
            probability = self._forward(X_train)

            cost = self._compute_cost(y_true=y_train,
                                      output=probability)

            y_train_pred = self.predict(X_train)
            y_valid_pred = self.predict(X_valid)

            train_acc = ((np.sum(y_train == y_train_pred)).astype(np.float) /
                         X_train.shape[0])
            valid_acc = ((np.sum(y_valid == y_valid_pred)).astype(np.float) /
                         X_valid.shape[0])

            sys.stderr.write('\r%0*d/%d | Train Cost: %.2f '' | Cost: %.2f ''| Train/Valid Acc.: %.2f%%/%.2f%% ' %
                             (epoch_strlen, i + 1, self.iterations, train_cost, cost,
                              train_acc * 100, valid_acc * 100))

            sys.stderr.flush()

            self.eval_['cost'].append(cost)
            self.eval_['train_acc'].append(train_acc)
            self.eval_['valid_acc'].append(valid_acc)

        return self


X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 1, 1, 0])

nn = Particle_Swarm_Optimization(number_of_units_in_the_hidden_layer=2, iterations=1000)
nn.fit(X_train=X, y_train=y, X_valid=X, y_valid=y)

y_prediction = nn.predict(X=[0, 1])
print(y_prediction)

y_prediction = nn.predict(X=[1, 0])
print(y_prediction)

y_prediction = nn.predict(X=[1, 1])
print(y_prediction)

y_prediction = nn.predict(X=[0, 0])
print(y_prediction)
