import numpy as np

def generate_time_series(batch_size, number_of_steps):
    frequency1, frequency2, offsets1, offsets2 = np.random.rand(4, batch_size, 1)
    time = np.linspace(0, 1, number_of_steps)

    series = 0.5 * np.sin((time - offsets1) * (frequency1 * 10 + 10))  # wave 1
    series += 0.2 * np.sin((time - offsets2) * (frequency2 * 20 + 20)) # + wave 2
    series += 0.1 * (np.random.rand(batch_size, number_of_steps) - 0.5) # + noise

    return series[..., np.newaxis].astype(np.float32)

