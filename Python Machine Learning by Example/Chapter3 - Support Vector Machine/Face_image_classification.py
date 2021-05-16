from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

face_data = fetch_lfw_people(min_faces_per_person=80)

X = face_data.data
y = face_data.target
print('Input data size: ', X.shape)
print('Output data size: ', y.shape)
print('Label names: ', face_data.target_names)

# Analyze the label distribution (Determine if the data distribution among the dataset is balanced.)
for i in range(5):
    print(f'Class {i} has {(y == i).sum()} samples.')


fig, ax = plt.subplots(3, 4)
for i, axi in enumerate(ax.flat):
    axi.imshow(face_data.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[], xlabel=face_data.target_names[face_data.target[i]])


plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

