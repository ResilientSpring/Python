import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

fb_complete_data = pd.read_csv('FB.csv')
print(fb_complete_data)

fb_training_processed = fb_complete_data['Open']
print(fb_training_processed)

fb_training_processed = fb_training_processed.values
print(fb_training_processed)

X_train, X_test = train_test_split(fb_training_processed, test_size=0.3,
                                   shuffle=False, random_state=1)

print(X_train, X_test)

scaler = MinMaxScaler(feature_range=(0, 1))

fb_training_scaled = scaler.fit_transform(X=X_train)
print(len(fb_training_scaled))