import sys

import numpy as np


class Particle_Swarm_Optimization(object):

    def __init__(self, number_of_units_in_the_hidden_layer=2, l2=0., iterations=100, velocity=0.001,
                 shuffle=True, minibatch_size=1, seed=None):
        self.random = np.random.RandomState(seed)
        self.number_of_hidden_units = number_of_units_in_the_hidden_layer
        self.l2 = l2
        self.iterations = iterations
        self.velocity = velocity
        self.shuffle = shuffle
        self.minibatch_size = minibatch_size


    def _onehot(self, y, n_classes):
        """Encode labels into one-hot representation
        Parameters
        ------------
        y : array, shape = [n_examples]
            Target values.
        _classes : int
            Number of classes
        Returns
        -----------
        onehot : array, shape = (n_examples, n_labels)
        """
        onehot = np.zeros((n_classes, y.shape[0]))

        for idx, val in enumerate(y.astype(int)):
            onehot[val, idx] = 1.

        return onehot.T


    def sigmoid(self, z):
        return 1.0 / (1 + np.exp(-z))


    def _forward(self, X):
        X0 = 1
        X1 = X[0]
        X2 = X[1]

        weight_X0_a12 = np.random.rand()
        weight_X0_a22 = np.random.rand()
        weight_X1_a12 = np.random.rand()
        weight_X1_a22 = np.random.rand()
        weight_X2_a12 = np.random.rand()
        weight_X2_a22 = np.random.rand()

        a02 = 1
        weight_a02_a13 = np.random.rand()
        weight_a12_a13 = np.random.rand()
        weight_a22_a13 = np.random.rand()

        input_a12 = (X1 * weight_X1_a12) + (X2 * weight_X2_a12) + (X0 * weight_X0_a12)
        output_a12 = self.sigmoid(input_a12)

        input_a22 = (X1 * weight_X1_a22) + (X2 * weight_X2_a22) + (X0 * weight_X0_a22)
        output_a22 = self.sigmoid(input_a22)

        input_a13 = (a02 * weight_a02_a13) + (output_a12 * weight_a12_a13) + (output_a22 * weight_a22_a13)
        output_a13 = self.sigmoid(input_a13)

        return input_a12, output_a12, input_a22, output_a22, input_a13, output_a13


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
            Regularized cost
        """

        L2_term = (self.l2 * (np.sum(self.w_h ** 2.) + np.sum(self.w_out ** 2.)))

        term1 = -y_true * (np.log(output))
        term2 = (1. - y_true) * np.log(1. - output)
        cost = np.sum(term1 - term2) + L2_term

        # If you are applying this cost function to other
        # datasets where activation
        # values maybe become more extreme (closer to zero or 1)
        # you may encounter "ZeroDivisionError"s due to numerical
        # instabilities in Python & NumPy for the current implementation.
        # I.e., the code tries to evaluate log(0), which is undefined.
        # To address this issue, you could add a small constant to the
        # activation values that are passed to the log function.
        #
        # For example:
        #
        # term1 = -y_enc * (np.log(output + 1e-5))
        # term2 = (1. - y_enc) * np.log(1. - output + 1e-5)

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
        input_a12, output_a12, input_a22, output_a22, input_a13, output_a13 = self._forward(X)

        y_pred = np.argmax(input_a13, axis=1)
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
        n_output = np.unique(y_train).shape[0]  # number of class labels
        n_features = X_train.shape[1]

        ########################
        # Weight initialization
        ########################

        # weights for input -> hidden
        self.b_h = np.zeros(self.number_of_hidden_units)
        self.w_h = self.random.normal(loc=0.0, scale=0.1,
                                      size=(n_features, self.number_of_hidden_units))

        # weights for hidden -> output
        self.b_out = np.zeros(n_output)
        self.w_out = self.random.normal(loc=0.0, scale=0.1,
                                        size=(self.number_of_hidden_units, n_output))

        epoch_strlen = len(str(self.iterations))  # for progress formatting
        self.eval_ = {'cost': [], 'train_acc': [], 'valid_acc': []}

        y_train = self._onehot(y_train, n_output)

        # iterate over training epochs
        for i in range(1, self.iterations + 1):

            # iterate over minibatches
            indices = np.arange(X_train.shape[0])

            if self.shuffle:
                self.random.shuffle(indices)

            for start_idx in range(0, indices.shape[0] - self.minibatch_size +
                                      1, self.minibatch_size):
                batch_idx = indices[start_idx:start_idx + self.minibatch_size]

                # forward propagation
                z_h, a_h, z_out, a_out = self._forward(X_train[batch_idx])

                ##################
                # Backpropagation
                ##################

                # [n_examples, n_classlabels]
                delta_out = a_out - y_train[batch_idx]

                # [n_examples, n_hidden]
                sigmoid_derivative_h = a_h * (1. - a_h)

                # [n_examples, n_classlabels] dot [n_classlabels, n_hidden]
                # -> [n_examples, n_hidden]
                delta_h = (np.dot(delta_out, self.w_out.T) *
                           sigmoid_derivative_h)

                # [n_features, n_examples] dot [n_examples, n_hidden]
                # -> [n_features, n_hidden]
                grad_w_h = np.dot(X_train[batch_idx].T, delta_h)
                grad_b_h = np.sum(delta_h, axis=0)

                # [n_hidden, n_examples] dot [n_examples, n_classlabels]
                # -> [n_hidden, n_classlabels]
                grad_w_out = np.dot(a_h.T, delta_out)
                grad_b_out = np.sum(delta_out, axis=0)

                # Regularization and weight updates
                delta_w_h = (grad_w_h + self.l2 * self.w_h)
                delta_b_h = grad_b_h  # bias is not regularized
                self.w_h -= self.velocity * delta_w_h
                self.b_h -= self.velocity * delta_b_h

                delta_w_out = (grad_w_out + self.l2 * self.w_out)
                delta_b_out = grad_b_out  # bias is not regularized
                self.w_out -= self.velocity * delta_w_out
                self.b_out -= self.velocity * delta_b_out

            #############
            # Evaluation
            #############

            # Evaluation after each epoch during training
            z_h, a_h, z_out, a_out = self._forward(X_train)

            cost = self._compute_cost(y_true=y_train,
                                      output=a_out)

            y_train_pred = self.predict(X_train)
            y_valid_pred = self.predict(X_valid)

            train_acc = ((np.sum(y_train == y_train_pred)).astype(np.float) /
                         X_train.shape[0])
            valid_acc = ((np.sum(y_valid == y_valid_pred)).astype(np.float) /
                         X_valid.shape[0])

            sys.stderr.write('\r%0*d/%d | Cost: %.2f '
                             '| Train/Valid Acc.: %.2f%%/%.2f%% ' %
                             (epoch_strlen, i + 1, self.iterations, cost,
                              train_acc * 100, valid_acc * 100))
            sys.stderr.flush()

            self.eval_['cost'].append(cost)
            self.eval_['train_acc'].append(train_acc)
            self.eval_['valid_acc'].append(valid_acc)

        return self

