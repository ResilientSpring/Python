def generate_batches(train, batch_size= 32, lookback = 100):
    num_samples = train.shape[0]
    