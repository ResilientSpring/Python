from sklearn.model_selection import cross_val_score
import KNN

scores = cross_val_score(estimator=KNN.knn, X=KNN.train_data, y=KNN.train_label, cv=5,
                         scoring="accuracy")

print("score: ", scores)
print("mean: ", scores.mean())