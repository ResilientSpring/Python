import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, InputLayer, Input
import tensorflow.keras
import pygad.kerasga
from pygad.kerasga import KerasGA
import numpy
import pygad
from tensorflow.keras.initializers import Ones, ones
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy, MeanAbsoluteError
from tensorflow.keras import Model
from tensorflow.keras.utils import plot_model, pack_x_y_sample_weight
from tensorflow.keras.models import Sequential
from tensorflow.keras.activations import sigmoid
from pygad.kerasga import predict


def smooth_L1_loss(y_true, y_pred):
    error = y_true - y_pred
    is_small_error = tf.abs(error) < 1
    squared_loss = tf.square(error) / 2
    linear_loss = tf.abs(error) - 0.5

    return tf.where(is_small_error, squared_loss, linear_loss)


def error(current_position):
    a12 = current_position[0]
    a22 = current_position[1]
    a13 = current_position[2]

    return 1.0 / (1.0 + np.exp(-current_position))


# Create a Keras model
model = Sequential([InputLayer(input_shape=(2, )),
                    Dense(units=2, use_bias=True, bias_initializer=Ones(), activation=sigmoid),
                    Dense(units=1, use_bias=True, bias_initializer=Ones(), activation=sigmoid)])

model.compile(loss=smooth_L1_loss)


def error(current_pos):
    x = current_pos[0]
    y = current_pos[1]

    return (x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y)) + 20


def grad_error(current_pos):
    x = current_pos[0]
    y = current_pos[1]

    return np.array(
        [2 * x + 10 * 2 * np.pi * x * np.sin(2 * np.pi * x),
         2 * y + 10 * 2 * np.pi * y * np.sin(2 * np.pi * y)])


class Particle:

    def __init__(self, dim, minx, maxx):
        self.position = np.random.uniform(low=minx, high=maxx, size=dim)
        self.velocity = np.random.uniform(low=minx, high=maxx, size=dim)
        self.best_part_pos = self.position.copy()

        self.error = error(self.position)
        self.best_part_err = self.error.copy()

    def setPos(self, pos):
        self.position = pos
        self.error = error(pos)
        if self.error < self.best_part_err:
            self.best_part_err = self.error
            self.best_part_pos = pos

class PSO:

    w = 0.729
    c1 = 1.49445
    c2 = 1.49445
    lr = 0.01

    def __init__(self, dims, numOfBoids, numOfEpochs):
        self.swarm_list = [Particle(dims, -500, 500) for i in range(numOfBoids)]
        self.numOfEpochs = numOfEpochs

        self.best_swarm_position = np.random.uniform(low=-500, high=500, size=dims)
        self.best_swarm_error = 1e80  # Set high value to best swarm error


    def optimize(self):
        for i in range(self.numOfEpochs):

            for j in range(len(self.swarm_list)):

                current_particle = self.swarm_list[j]  # get current particle

                Vcurr = grad_error(current_particle.position)  # calculate current velocity of the particle

                deltaV = self.w * Vcurr \
                         + self.c1 * (current_particle.best_part_pos - current_particle.position) \
                         + self.c2 * (self.best_swarm_position - current_particle.position)  # calculate delta V

                new_position = self.swarm_list[j].position - self.lr * deltaV  # calculate the new position

                self.swarm_list[j].setPos(new_position)  # update the position of particle

                if error(new_position) < self.best_swarm_error:  # check the position if it's best for swarm
                    self.best_swarm_position = new_position
                    self.best_swarm_error = error(new_position)

            print('Epoch: {0} | Best position: [{1},{2}] | Best known error: {3}'.format(i,
                                                                                         self.best_swarm_position[0],
                                                                                         self.best_swarm_position[1],
                                                                                         self.best_swarm_error))


pso = PSO(dims=2, numOfBoids=30, numOfEpochs=500)
pso.optimize()


class PSOptimizer(tensorflow.keras.optimizers.Optimizer):
    def __init__(self, learning_rate=0.01, name="PSOptimizer", **kwargs):
        """Call super().__init__() and use _set_hyper() to store hyperparameters"""
        super().__init__(name, **kwargs)
        self._set_hyper("learning_rate", kwargs.get("lr", learning_rate)) # handle lr=learning_rate
        self._is_first = True

    def _create_slots(self, var_list):
        """For each model variable, create the optimizer variable associated with it.
        TensorFlow calls these optimizer variables "slots".
        For momentum optimization, we need one momentum slot per model variable.
        """
        for var in var_list:
            self.add_slot(var, "previous_weight") #previous variable i.e. weight or bias
        for var in var_list:
            self.add_slot(var, "previous_gradient") #previous gradient

    @tf.function
    def _resource_apply_dense(self, grad, var):
        """Update the slots and perform one optimization step for one model variable
        """
        var_dtype = var.dtype.base_dtype
        lr_t = self._decayed_lr(var_dtype) # handle learning rate decay

        # Compute the new weight using the traditional gradient descent method
        new_var_m = var - grad * lr_t

        # Extract the previous values of Variables and Gradients
        pv_var = self.get_slot(var, "pv")
        pg_var = self.get_slot(var, "pg")

        # If it first time, use just the traditional method
        if self._is_first:
            self._is_first = False
            new_var = new_var_m
        else:
            # create a boolean tensor contain true and false
            # True will be where the gradient haven't changed the sign and False will be the case where the gradients have changed sign
            cond = grad*pg_var >= 0

            # Compute the average of previous weight and current. Though we will be using only few of these.
            #Of course, it is prone to overflow. We can also compute the avg using a + (b -a)/2.0
            avg_weights = (pv_var + var)/2.0

            # tf.where picks the value from new_var_m where the cond is True otherwise it takes from avg_weights
            # We must avoid the for loops
            new_var = tf.where(cond, new_var_m, avg_weights)
        # Finally we are saving current values in the slots.
        pv_var.assign(var)
        pg_var.assign(grad)

        # We are updating weight here. We don't need to return anything
        var.assign(new_var)

    def _resource_apply_sparse(self, grad, var):
        raise NotImplementedError

    def get_config(self):
        base_config = super().get_config()
        return {
            **base_config,
            "learning_rate": self._serialize_hyperparameter("learning_rate"),
        }


    def _resource_apply_sparse(self, grad, var):
        raise NotImplementedError

    def get_config(self):
        base_config = super().get_config()
        return {
            **base_config,
            "learning_rate": self._serialize_hyperparameter("learning_rate"),
            "decay": self._serialize_hyperparameter("decay"),
            "momentum": self._serialize_hyperparameter("momentum"),
        }


# References:
# 1. https://stackoverflow.com/a/56255595/14900011
# 2. https://zhuanlan.zhihu.com/p/48426076
# 3. https://archive.ph/MbzAm
# 4. https://cloudxlab.com/blog/writing-custom-optimizer-in-tensorflow-and-keras/
