from sklearn.feature_extraction import DictVectorizer

X_dict = [{"interest": "tech", "occupation": "professional"},
          {"interest": "fashion", "occupation": "student"},
          {"interest": "fashion", "occupation": "professional"},
          {"interest": "sports", "occupation": "student"},
          {"interest": "tech", "occupation": "student"},
          {"interest": "tech", "occupation": "retired"},
          {"interest": "sports", "occupation": "professional"}];

# Dict_Vectorizer converts/transforms dictionary objects({categorical feature: value})
# into one-hot encoded vectors.
dict_one_hot_encoder = DictVectorizer(sparse=False);

X_encoded = dict_one_hot_encoder.fit_transform(X=X_dict);

print(X_encoded);

## See the mapping by executing the following:
print(dict_one_hot_encoder.vocabulary_);

# When it comes to new data, we can transform it with the following:
new_dict = [{"interest": "sports", "occupation": "retired"}];

## Because {'interest=sports': 1} and {'occupation=retired': 4} have already been fitted,
## transform(), as opposed to fit_transform(), should suffice.
new_encoded = dict_one_hot_encoder.transform(new_dict);
print(new_encoded);

# We can inversely transform the encoded features back to the original features like this:
inverse_the_encoded = dict_one_hot_encoder.inverse_transform(X=new_encoded);
print(inverse_the_encoded);

## Again, here, inverse_fit is not needed since fit() means to extract a function
# describing the relation between X and y.