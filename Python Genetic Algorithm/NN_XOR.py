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


# Create a Keras model
model = Sequential([InputLayer(input_shape=(2, )),
                    Dense(units=2, use_bias=True, bias_initializer=Ones(), activation=sigmoid),
                    Dense(units=1, use_bias=True, bias_initializer=Ones(), activation=sigmoid)])

# Create an instance of the pygad.kerasga.KerasGA class.
kerasGA = KerasGA(model=model, num_solutions=9)

# Prepare the Training Data
# XOR problem inputs
data_inputs = numpy.array([[0.0, 0.0],
                           [0.0, 1.0],
                           [1.0, 0.0],
                           [1.0, 1.0]])

# XOR problem outputs
data_outputs = numpy.array([[0.0],
                            [1.0],
                            [1.0],
                            [0.0]])

# Build the fitness function
def fitness_func(solution, sol_idx):
    global data_inputs, data_outputs, kerasGA, model

    predictions = predict(model=model, solution=solution, data=data_inputs)

    mae = MeanAbsoluteError()
    abs_error = mae(y_true=data_outputs, y_pred=predictions).numpy() + 0.00000001
    solution_fitness = 1.0 / abs_error

    return solution_fitness

# Create a callback
def callback_generation(ga_instance):
    print('Generation = {generation}'.format(generation=ga_instance.generations_completed))
    print('Fitness = {fitness}'.format(fitness=ga_instance.best_solution()[1]))


# Create an instance of the pygad.GA Class
ga_instance = pygad.GA(num_generations=250,
                       num_parents_mating=2,
                       parent_selection_type='random',
                       fitness_func=fitness_func,
                       sol_per_pop=9, num_genes=9, init_range_low=0.01, init_range_high=10.00,
                       crossover_type='two_points', mutation_type='swap',
                       mutation_num_genes=1, save_best_solutions=True, save_solutions=True,
                       allow_duplicate_genes=True, stop_criteria='saturate_10',
                       on_generation=callback_generation)

# Run the Genetic algorithm
ga_instance.run()

# Plot the fitness value
ga_instance.plot_fitness(title='Iteration vs. Fitness', xlabel='Generation', ylabel='Fitness',
                         linewidth=4)

# To get the details about the best solution found by PyGAD
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f'Fitness value of the best solution = '
      f'{solution_fitness}'.format(solution_fitness=solution_fitness))
print(f'Index of the best solution: {solution_idx}'.format(solution_idx=solution_idx))

# Make prediction based on the trained model's best solution.
predictions = predict(model=model, solution=solution, data=data_inputs)

print('Predictions: \n', predictions)

# Measure the trained model error.
mae = MeanAbsoluteError()
abs_error = mae(y_true=data_outputs, y_pred=predictions).numpy()
print('Absolute Error:', abs_error)
