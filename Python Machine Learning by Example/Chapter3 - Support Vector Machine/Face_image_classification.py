from sklearn.datasets import fetch_lfw_people

face_data = fetch_lfw_people(min_faces_per_person=80)

X = face_data.data
y = face_data.target
print('Input data size: ', X.shape)
print('Output data size: ', y.shape)
print('Label names: ', face_data.target_names)
