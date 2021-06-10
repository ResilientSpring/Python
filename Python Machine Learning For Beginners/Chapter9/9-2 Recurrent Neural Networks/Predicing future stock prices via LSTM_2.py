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

# Training feature set contains the opening stock price of the past 60 days.
fb_training_feature_set = []
for i in range(60, len(fb_training_scaled)):
    fb_training_feature_set.append(fb_training_scaled[i - 60:i, 0])

fb_training_label_set = []
for i in range(60, len(fb_training_scaled)):
    fb_training_label_set.append(fb_training_scaled[i, 0])

