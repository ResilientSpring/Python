import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

fb_complete_data = pd.read_csv('FB.csv')
print(fb_complete_data)

fb_training_processed = fb_complete_data['Open']
print(fb_training_processed)

fb_training_processed = fb_training_processed.values
print(fb_training_processed)

scaler = MinMaxScaler(feature_range=(0, 1))

fb_training_processed = fb_training_processed.reshape((-1, 1))

fb_training_scaled = scaler.fit_transform(X=fb_training_processed)
print(len(fb_training_scaled))
