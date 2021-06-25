import tensorflow.keras
import pygad.kerasga
import numpy
import pygad
from pygad.kerasga import predict
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy, MeanAbsoluteError


# Build the keras model using the functional API.
input_layer  = tensorflow.keras.layers.Input(2)
dense_layer = tensorflow.keras.layers.Dense(2, activation="sigmoid", use_bias=True)(input_layer)
output_layer = tensorflow.keras.layers.Dense(1, activation="sigmoid", use_bias=True)(dense_layer)

model = tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)

# Create an instance of the pygad.kerasga.KerasGA class to build the initial population.
keras_ga = pygad.kerasga.KerasGA(model=model, num_solutions=9)

# XOR problem inputs
data_inputs = numpy.array([[0, 0],
                           [0, 1],
                           [1, 0],
                           [1, 1]])

# XOR problem outputs
data_outputs = numpy.array([[0],
                            [1],
                            [1],
                            [0]])

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


# Create an instance of the pygad.GA class
ga_instance = pygad.GA(num_generations=250,# Number of generations.
                       num_parents_mating=5,# Number of solutions to be selected as parents in the mating pool.
                       initial_population=keras_ga.population_weights,# Initial population of network weights.
                       fitness_func=fitness_func,
                       on_generation=callback_generation)

# Start the genetic algorithm evolution.
ga_instance.run()

# After the generations complete, some plots are showed that summarize how the outputs/fitness values evolve over generations.
ga_instance.plot_fitness(title="PyGAD & Keras - Iteration vs. Fitness", linewidth=4)

# Returning the details of the best solution.
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

# Make predictions based on the best solution.
predictions = pygad.kerasga.predict(model=model,
                                    solution=solution,
                                    data=data_inputs)
print("Predictions : \n", predictions)

# Calculate the binary crossentropy for the trained model.
bce = tensorflow.keras.losses.BinaryCrossentropy()
print("Binary Crossentropy : ", bce(data_outputs, predictions).numpy())

# Calculate the classification accuracy for the trained model.
ba = tensorflow.keras.metrics.BinaryAccuracy()
ba.update_state(data_outputs, predictions)
accuracy = ba.result().numpy()
print("Accuracy : ", accuracy)
